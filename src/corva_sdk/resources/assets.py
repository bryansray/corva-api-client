from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from corva_sdk.client import CorvaClient


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
        status: str | None = None,
        company_id: int | None = None,
        fields: str | None = "*",
        start: int | None = None,
        end: int | None = None,
        sort: str | None = "-last_active_at",
        page: int | None = None,
        per_page: int | None = None,
        order: str | None = None,
    ):
        params: dict[str, Any] = {}

        if query:
            params["search"] = query
        if types:
            params["types"] = types
        if status:
            params["status"] = status
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
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page

        return self.list(params or None)
