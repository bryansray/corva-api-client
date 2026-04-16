from __future__ import annotations

import httpx
import pytest

from corva_api_client import CorvaClient


def test_client_requires_api_key() -> None:
    with pytest.raises(RuntimeError, match="Corva API key is required."):
        CorvaClient()


def test_client_uses_api_key_auth_header() -> None:
    client = CorvaClient(
        api_key="secret",
        base_api_url="https://api.example.com",
        base_data_api_url="https://data.example.com",
    )

    assert client.client.headers["Authorization"] == "API secret"
    client.close()


def test_client_uses_jwt_auth_header() -> None:
    client = CorvaClient(
        api_key="secret",
        auth_kind="jwt",
        base_api_url="https://api.example.com",
        base_data_api_url="https://data.example.com",
    )

    assert client.client.headers["Authorization"] == "Bearer secret"
    client.close()


def test_build_url_routes_data_api_paths() -> None:
    client = CorvaClient(
        api_key="secret",
        base_api_url="https://api.example.com",
        base_data_api_url="https://data.example.com",
    )

    assert client._build_url("/v1/assets") == "https://api.example.com/v1/assets"
    assert (
        client._build_url("/api/v1/data/corva/wits.summary-1ft/")
        == "https://data.example.com/api/v1/data/corva/wits.summary-1ft/"
    )
    assert client._build_url("https://other.example.com/path") == "https://other.example.com/path"
    client.close()


def test_prepare_request_kwargs_only_adds_json_for_non_get() -> None:
    client = CorvaClient(
        api_key="secret",
        base_api_url="https://api.example.com",
        base_data_api_url="https://data.example.com",
    )

    assert client._prepare_request_kwargs("GET", {"a": 1}, {"params": {"x": "1"}}) == {
        "params": {"x": "1"}
    }
    assert client._prepare_request_kwargs("POST", {"a": 1}, {"params": {"x": "1"}}) == {
        "params": {"x": "1"},
        "json": {"a": 1},
    }
    client.close()


def test_request_returns_json(monkeypatch: pytest.MonkeyPatch) -> None:
    client = CorvaClient(
        api_key="secret",
        base_api_url="https://api.example.com",
        base_data_api_url="https://data.example.com",
    )

    def fake_request(method: str, url: str, **kwargs: object) -> httpx.Response:
        request = httpx.Request(method, url)
        return httpx.Response(200, json={"ok": True}, request=request)

    monkeypatch.setattr(client.client, "request", fake_request)

    assert client.get("/v1/assets") == {"ok": True}
    client.close()


def test_request_returns_text_when_json_decode_fails(monkeypatch: pytest.MonkeyPatch) -> None:
    client = CorvaClient(
        api_key="secret",
        base_api_url="https://api.example.com",
        base_data_api_url="https://data.example.com",
    )

    def fake_request(method: str, url: str, **kwargs: object) -> httpx.Response:
        request = httpx.Request(method, url)
        return httpx.Response(200, text="plain text body", request=request)

    monkeypatch.setattr(client.client, "request", fake_request)

    assert client.get("/v1/assets") == {"text": "plain text body"}
    client.close()


def test_request_returns_empty_dict_for_empty_body(monkeypatch: pytest.MonkeyPatch) -> None:
    client = CorvaClient(
        api_key="secret",
        base_api_url="https://api.example.com",
        base_data_api_url="https://data.example.com",
    )

    def fake_request(method: str, url: str, **kwargs: object) -> httpx.Response:
        request = httpx.Request(method, url)
        return httpx.Response(204, content=b"", request=request)

    monkeypatch.setattr(client.client, "request", fake_request)

    assert client.delete("/v1/assets/1") == {}
    client.close()


def test_request_returns_none_on_http_error(monkeypatch: pytest.MonkeyPatch) -> None:
    client = CorvaClient(
        api_key="secret",
        base_api_url="https://api.example.com",
        base_data_api_url="https://data.example.com",
    )

    def fake_request(method: str, url: str, **kwargs: object) -> httpx.Response:
        request = httpx.Request(method, url)
        return httpx.Response(500, json={"detail": "boom"}, request=request)

    monkeypatch.setattr(client.client, "request", fake_request)

    assert client.get("/v1/assets") is None
    client.close()
