from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from corva_api_client.client import CorvaClient


class WellsClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters: dict[str, Any] | None = None):
        return self._client.get("/v2/wells", params=query_parameters)

    def get(
        self,
        id: int | None = None,
        query_parameters: dict[str, Any] | None = None,
    ):
        return self._client.get(f"/v2/wells/{id}", params=query_parameters)

    def search(
        self,
        *,
        ids: str | None = None,
        company_id: int | None = None,
        fields: str | None = "*",
        sort: str | None = None,
        pad: int | None = None,
        status: str | None = None,
        state: str | None = None,
        identifier: str | None = None,
        area: str | None = None,
        search: str | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ):
        params: dict[str, Any] = {}

        if ids:
            params["ids"] = ids
        if company_id is not None:
            params["company"] = company_id
        if fields:
            params["fields"] = fields
        if sort:
            params["sort"] = sort
        if pad is not None:
            params["pad"] = pad
        if status:
            params["status"] = status
        if state:
            params["state"] = state
        if identifier:
            params["identifier"] = identifier
        if area:
            params["area"] = area
        if search:
            params["search"] = search
        if per_page is not None:
            params["per_page"] = per_page
        if page is not None:
            params["page"] = page

        return self.list(params or None)
