from __future__ import annotations

import pytest

from corva_api_client import CorvaConfig


def test_public_imports() -> None:
    from corva_api_client import CorvaClient

    assert CorvaClient is not None
    assert CorvaConfig is not None


def test_from_env_uses_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CORVA_API_KEY", "secret")
    monkeypatch.delenv("CORVA_ENVIRONMENT", raising=False)
    monkeypatch.delenv("CORVA_API_URL", raising=False)
    monkeypatch.delenv("CORVA_DATA_API_URL", raising=False)
    monkeypatch.delenv("CORVA_AUTH_KIND", raising=False)
    monkeypatch.delenv("CORVA_APP_KEY", raising=False)

    config = CorvaConfig.from_env()

    assert config.base_api_url == "https://api.corva.ai"
    assert config.base_data_api_url == "https://data.corva.ai"
    assert config.api_key == "secret"
    assert config.auth_kind == "api_key"
    assert config.app_key == "corva-api-client"


def test_from_env_uses_overrides(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("CORVA_API_KEY", "secret")
    monkeypatch.setenv("CORVA_ENVIRONMENT", "qa")
    monkeypatch.setenv("CORVA_API_URL", "https://example-api")
    monkeypatch.setenv("CORVA_DATA_API_URL", "https://example-data")
    monkeypatch.setenv("CORVA_AUTH_KIND", "jwt")
    monkeypatch.setenv("CORVA_APP_KEY", "custom-app")

    config = CorvaConfig.from_env()

    assert config.base_api_url == "https://example-api"
    assert config.base_data_api_url == "https://example-data"
    assert config.auth_kind == "jwt"
    assert config.app_key == "custom-app"


def test_from_env_requires_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("CORVA_API_KEY", raising=False)

    with pytest.raises(RuntimeError, match="CORVA_API_KEY is not set."):
        CorvaConfig.from_env()
