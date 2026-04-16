from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any
from urllib.parse import quote

if TYPE_CHECKING:
    from corva_api_client.client import CorvaClient


class DatasetsClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def get_metadata(self, name: str, provider: str = "corva"):
        escaped_provider = quote(provider.strip(), safe="")
        escaped_name = quote(name.strip(), safe="")
        return self._client.get(f"/api/v1/dataset/{escaped_provider}/{escaped_name}/")

    def get_data(
        self,
        dataset: str,
        provider: str = "corva",
        query_parameters: dict[str, Any] | None = None,
    ):
        escaped_provider = quote(provider.strip(), safe="")
        escaped_dataset = quote(dataset.strip(), safe="")
        return self._client.get(
            f"/api/v1/data/{escaped_provider}/{escaped_dataset}/",
            params=query_parameters or {"sort": {"timestamp": -1}, "limit": 50},
        )

    def list(self, query_parameters: dict[str, Any] | None = None):
        return self._client.get("/api/v1/dataset/", params=query_parameters)

    def get_latest(self, name: str, query: dict[str, Any]):
        escaped_name = quote(name.strip(), safe="")
        params = {
            "query": json.dumps(query),
            "limit": 5,
            "sort": json.dumps({"timestamp": 1}),
        }
        return self._client.get(f"/api/v1/data/corva/{escaped_name}/", params=params)

    def search(self, search: str, query_parameters: dict[str, Any] | None = None):
        merged = dict(query_parameters or {})
        if search:
            merged["search"] = search
        return self._client.get("/api/v1/dataset/", params=merged)
