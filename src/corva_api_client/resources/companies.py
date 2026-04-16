from __future__ import annotations

import builtins
from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING:
    from corva_api_client.client import CorvaClient


class CompaniesClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters: dict[str, Any] | None = None) -> builtins.list[dict[str, Any]]:
        response = self._client.get("/v1/companies", params=query_parameters)
        return cast(builtins.list[dict[str, Any]], response)

    def get(self, company_id: int) -> dict[str, Any]:
        response = self._client.get(f"/v1/company?id={company_id}")
        return cast(dict[str, Any], response)
