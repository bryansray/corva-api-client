from __future__ import annotations

from collections.abc import Sequence
from enum import StrEnum
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from corva_api_client.client import CorvaClient


class AssetStatus(StrEnum):
    UNKNOWN = "unknown"
    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETE = "complete"
    IDLE = "idle"
    DELETING = "deleting"
    DELETION_PAUSED = "deletion_paused"
    ARCHIVED = "archived"


def _serialize_asset_status(
    status: AssetStatus | Sequence[AssetStatus] | None,
) -> list[str]:
    if status is None:
        return []

    raw_statuses = status.split(",") if isinstance(status, str) else status
    statuses: list[str] = []
    for raw_status in raw_statuses:
        value = str(raw_status).strip()
        if not value:
            continue
        try:
            statuses.append(AssetStatus(value).value)
        except ValueError as error:
            valid_values = ", ".join(item.value for item in AssetStatus)
            raise ValueError(
                f"Invalid asset status {value!r}. Expected one or more of: "
                f"{valid_values}. Omit status to search all statuses."
            ) from error

    return statuses


class AssetsClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters: dict[str, Any] | None = None):
        return self._client.get("/v2/assets", params=query_parameters)

    def get(
        self,
        id: int | None = None,
        query_parameters: dict[str, Any] | None = None,
    ):
        return self._client.get(f"/v2/assets/{id}", params=query_parameters)

    def ancestor_ids(self, id: int, query_parameters: dict[str, Any] | None = None):
        return self._client.get(f"/v2/assets/{id}/ancestor_ids", params=query_parameters)

    # Backwards-compatible helper for the current CLI command style.
    def search(
        self,
        query: str | None = None,
        types: str | None = None,
        status: AssetStatus | Sequence[AssetStatus] | None = None,
        company_id: int | None = None,
        fields: str | None = "*",
        start: int | None = None,
        end: int | None = None,
        sort: str | None = "-last_active_at",
        page: int | None = None,
        per_page: int | None = None,
        order: str | None = None,
        visibility: str | None = None,
    ):
        params: dict[str, Any] = {}

        if query:
            params["search"] = query
        if types:
            params["types"] = types
        serialized_status = _serialize_asset_status(status)
        if serialized_status:
            params["status[]"] = serialized_status
        if company_id is not None:
            params["company_id"] = company_id
        if fields:
            params["fields"] = fields
        if start is not None:
            params["start"] = start
        if end is not None:
            params["end"] = end
        if sort:
            params["sort"] = sort
        if order:
            params["order"] = order
        if visibility:
            params["visibility"] = visibility
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page

        return self.list(params or None)
