from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_sdk.client import CorvaClient


class AppConnectionClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def post_v1_app_connections(self, body=None, query_parameters=None):
        path = "/v1/app_connections"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v1_app_connections_id(self, id, body=None, query_parameters=None):
        path = f"/v1/app_connections/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v1_app_connections_id(self, id, query_parameters=None):
        path = f"/v1/app_connections/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v1_app_connections_id(self, id, body=None, query_parameters=None):
        path = f"/v1/app_connections/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def patch_v1_app_connections_id_update_package(self, id, body=None, query_parameters=None):
        path = f"/v1/app_connections/{id}/update_package"
        return self._client.patch(path, body=body, params=query_parameters)
