from __future__ import annotations

from typing import TYPE_CHECKING, Any, cast

if TYPE_CHECKING:
    from corva_sdk.client import CorvaClient


class AppsClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def search(
        self,
        query_parameters: dict[str, Any] | None = None,
        sort: list[str] | None = None,
        type: str | None = None,
    ) -> list[dict[str, Any]]:
        params = dict(query_parameters or {})

        if sort is not None:
            params["sort"] = ",".join(sort)
        elif "sort" not in params:
            params["sort"] = "name"
        if type is not None:
            params["type"] = type

        params["fields"] = "*"

        results = self._client.get("/v2/apps", params=params or None)
        if not isinstance(results, dict):
            return []
        return cast(list[dict[str, Any]], results.get("data", []))

    def list_for_dataset(
        self,
        dataset_id: int,
        fields: list[str] | None = None,
        query_parameters: dict[str, Any] | None = None,
    ):
        merged = dict(query_parameters or {})
        merged["dataset_id"] = dataset_id
        if fields:
            merged["fields[]"] = fields
        return self._client.get("/v2/apps", params=merged)

    def get(self, id: int, query_parameters: dict[str, Any] | None = None) -> dict[str, Any]:
        response = self._client.get(f"/v2/apps/{id}", params=query_parameters)
        return cast(dict[str, Any], response)

    def create(self, body: Any, query_parameters: dict[str, Any] | None = None):
        return self._client.post("/v2/apps", body=body, params=query_parameters)

    def update(self, id: int, body: Any, query_parameters: dict[str, Any] | None = None):
        return self._client.patch(f"/v2/apps/{id}", body=body, params=query_parameters)

    def delete(self, id: int, query_parameters: dict[str, Any] | None = None):
        return self._client.delete(f"/v2/apps/{id}", params=query_parameters)

    def list_packages(self, app_id: int, query_parameters: dict[str, Any] | None = None):
        return self._client.get(f"/v2/apps/{app_id}/packages", params=query_parameters)

    def upload_package(
        self, app_id: int, body: Any, query_parameters: dict[str, Any] | None = None
    ):
        return self._client.post(
            f"/v2/apps/{app_id}/packages/upload", body=body, params=query_parameters
        )

    def list_app_datasets(self, app_id: int, query_parameters: dict[str, Any] | None = None):
        return self._client.get(f"/v2/apps/{app_id}/app_datasets", params=query_parameters)
