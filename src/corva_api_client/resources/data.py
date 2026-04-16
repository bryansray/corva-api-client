from __future__ import annotations

from datetime import UTC, date, datetime
from typing import TYPE_CHECKING, Any, cast

from bson import Decimal128, Int64, ObjectId

from corva_api_client.data_aggregate import build_data_aggregate_http_request
from corva_api_client.data_fetch import build_data_fetch_http_request

if TYPE_CHECKING:
    from corva_api_client.client import CorvaClient


class DataClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def fetch(
        self,
        provider: str,
        dataset: str,
        query: dict[str, Any] | None = None,
        sort: dict[str, int] | None = None,
        limit: int = 100,
        skip: int | None = None,
        asset_id: int | None = None,
        fields: list[str] | None = None,
    ) -> list[dict[str, Any]]:
        provider = provider.strip()
        dataset = dataset.strip()
        if not provider:
            raise ValueError("Provider is required.")
        if not dataset:
            raise ValueError("Dataset is required.")

        query_filter = dict(query or {})
        if asset_id is not None:
            query_filter["asset_id"] = asset_id

        if sort is None:
            sort = {"timestamp": -1}

        request = build_data_fetch_http_request(
            {
                "provider": provider,
                "dataset": dataset,
                "query": query_filter,
                "sort": sort,
                "limit": max(0, limit),
                "skip": max(0, skip) if skip is not None else None,
                "fields": fields,
            }
        )

        response = self._client.get(request["path"], params=request["params"])
        return cast(list[dict[str, Any]], response)

    def aggregate(
        self,
        provider: str,
        dataset: str,
        match: dict[str, Any] | None = None,
        group: dict[str, Any] | None = None,
        project: dict[str, Any] | None = None,
        sort: dict[str, int] | None = None,
        limit: int = 100,
        skip: int | None = None,
        asset_id: int | None = None,
    ) -> list[dict[str, Any]]:
        provider = provider.strip()
        dataset = dataset.strip()
        if not provider:
            raise ValueError("Provider is required.")
        if not dataset:
            raise ValueError("Dataset is required.")

        match_filter = dict(match or {})
        if asset_id is not None:
            match_filter["asset_id"] = asset_id

        request = build_data_aggregate_http_request(
            {
                "provider": provider,
                "dataset": dataset,
                "match": match_filter,
                "group": group,
                "project": project,
                "sort": sort,
                "limit": max(0, limit),
                "skip": max(0, skip) if skip is not None else None,
            }
        )

        response = self._client.get(request["path"], params=request["params"])
        return cast(list[dict[str, Any]], response)

    def create(
        self,
        provider: str,
        dataset: str,
        records: list[dict[str, Any]],
    ) -> dict[str, Any]:
        provider = provider.strip()
        dataset = dataset.strip()
        if not provider:
            raise ValueError("Provider is required.")
        if not dataset:
            raise ValueError("Dataset is required.")
        if not isinstance(records, list) or not records:
            raise ValueError("At least one record is required.")

        payload = [with_default_version(record) for record in records if isinstance(record, dict)]
        if not payload:
            raise ValueError("At least one valid record is required.")

        serialized_payload = [serialize_for_api(record) for record in payload]
        result = self._client.post(f"/api/v1/data/{provider}/{dataset}/", body=serialized_payload)
        return result if isinstance(result, dict) else {}

    def replace(
        self,
        provider: str,
        dataset: str,
        record_id: str,
        record: dict[str, Any],
    ) -> dict[str, Any]:
        provider = provider.strip()
        dataset = dataset.strip()
        record_id = record_id.strip()
        if not provider:
            raise ValueError("Provider is required.")
        if not dataset:
            raise ValueError("Dataset is required.")
        if not record_id:
            raise ValueError("Record id is required.")
        if not isinstance(record, dict):
            raise ValueError("A valid record is required.")

        payload = with_default_version(record)
        serialized_payload = serialize_for_api(payload)
        result = self._client.put(
            f"/api/v1/data/{provider}/{dataset}/{record_id}/",
            body=serialized_payload,
        )
        return result if isinstance(result, dict) else {}


def serialize_for_api(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): serialize_for_api(child) for key, child in value.items()}
    if isinstance(value, list):
        return [serialize_for_api(item) for item in value]
    if isinstance(value, datetime):
        normalized = value.astimezone(UTC) if value.tzinfo else value.replace(tzinfo=UTC)
        return normalized.isoformat()
    if isinstance(value, date):
        return value.isoformat()
    if isinstance(value, (ObjectId, Decimal128)):
        return str(value)
    if isinstance(value, Int64):
        return int(value)
    return value


def with_default_version(record: dict[str, Any]) -> dict[str, Any]:
    payload = dict(record)
    if "version" not in payload:
        payload["version"] = 1
    return payload
