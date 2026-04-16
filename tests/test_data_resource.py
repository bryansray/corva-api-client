from __future__ import annotations

from datetime import UTC, date, datetime
from typing import Any, cast

from bson import Decimal128, Int64, ObjectId

from corva_api_client.resources.data import DataClient, serialize_for_api, with_default_version


class StubClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, str, dict[str, Any]]] = []

    def get(self, path: str, **kwargs: Any) -> list[dict[str, Any]]:
        self.calls.append(("get", path, kwargs))
        return [{"ok": True}]

    def post(self, path: str, **kwargs: Any) -> dict[str, Any]:
        self.calls.append(("post", path, kwargs))
        return {"ok": True}

    def put(self, path: str, **kwargs: Any) -> dict[str, Any]:
        self.calls.append(("put", path, kwargs))
        return {"ok": True}


def test_data_client_fetch_builds_expected_request() -> None:
    stub = StubClient()
    client = DataClient(cast(Any, stub))

    result = client.fetch(
        provider=" corva ",
        dataset=" custom#events ",
        query={"status": "active"},
        asset_id=123,
        fields=["timestamp", "asset_id"],
        limit=10,
        skip=20,
    )

    assert result == [{"ok": True}]
    method, path, kwargs = stub.calls[-1]
    assert method == "get"
    assert path == "/api/v1/data/custom/events/"
    assert kwargs["params"]["limit"] == "10"
    assert kwargs["params"]["skip"] == 20
    assert kwargs["params"]["fields"] == "timestamp,asset_id"
    assert '"asset_id": 123' in kwargs["params"]["query"]


def test_data_client_aggregate_builds_expected_request() -> None:
    stub = StubClient()
    client = DataClient(cast(Any, stub))

    result = client.aggregate(
        provider="corva",
        dataset="wits.summary-1ft",
        match={"company_id": 456},
        group={"_id": "$asset_id"},
        asset_id=123,
        limit=5,
    )

    assert result == [{"ok": True}]
    method, path, kwargs = stub.calls[-1]
    assert method == "get"
    assert path == "/api/v1/data/corva/wits.summary-1ft/aggregate/"
    assert kwargs["params"]["limit"] == "5"
    assert '"asset_id": 123' in kwargs["params"]["match"]
    assert '"company_id": 456' in kwargs["params"]["match"]


def test_data_client_create_serializes_records_and_sets_default_version() -> None:
    stub = StubClient()
    client = DataClient(cast(Any, stub))

    payload = {
        "_id": ObjectId("507f1f77bcf86cd799439011"),
        "timestamp": datetime(2026, 4, 16, 12, 0, tzinfo=UTC),
        "date": date(2026, 4, 16),
        "decimal": Decimal128("12.5"),
        "count": Int64(42),
    }

    result = client.create("corva", "wits.summary-1ft", [payload])

    assert result == {"ok": True}
    method, path, kwargs = stub.calls[-1]
    assert method == "post"
    assert path == "/api/v1/data/corva/wits.summary-1ft/"
    body = kwargs["body"]
    assert body[0]["_id"] == "507f1f77bcf86cd799439011"
    assert body[0]["timestamp"] == "2026-04-16T12:00:00+00:00"
    assert body[0]["date"] == "2026-04-16"
    assert body[0]["decimal"] == "12.5"
    assert body[0]["count"] == 42
    assert body[0]["version"] == 1


def test_data_client_replace_serializes_record() -> None:
    stub = StubClient()
    client = DataClient(cast(Any, stub))

    result = client.replace("corva", "wits.summary-1ft", "abc123", {"value": 10})

    assert result == {"ok": True}
    method, path, kwargs = stub.calls[-1]
    assert method == "put"
    assert path == "/api/v1/data/corva/wits.summary-1ft/abc123/"
    assert kwargs["body"]["value"] == 10
    assert kwargs["body"]["version"] == 1


def test_serialize_for_api_handles_nested_values() -> None:
    payload = {
        "nested": [{"count": Int64(7)}],
        "object_id": ObjectId("507f1f77bcf86cd799439011"),
    }

    serialized = serialize_for_api(payload)

    assert serialized == {
        "nested": [{"count": 7}],
        "object_id": "507f1f77bcf86cd799439011",
    }


def test_with_default_version_preserves_existing_version() -> None:
    record = with_default_version({"version": 3, "value": 10})

    assert record == {"version": 3, "value": 10}
