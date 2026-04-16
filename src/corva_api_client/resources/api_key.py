from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_api_client.client import CorvaClient


class ApiKeyClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters=None):
        path = "/v2/api_keys_management"
        return self._client.get(path, params=query_parameters)

    def post_v2_api_keys_management(self, body=None, query_parameters=None):
        path = "/v2/api_keys_management"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_api_keys_management_id(self, id, body=None, query_parameters=None):
        path = f"/v2/api_keys_management/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_api_keys_management_id(self, id, query_parameters=None):
        path = f"/v2/api_keys_management/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_api_keys_management_id(self, id, body=None, query_parameters=None):
        path = f"/v2/api_keys_management/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def post_v2_api_keys_management_id_activate(self, id, body=None, query_parameters=None):
        path = f"/v2/api_keys_management/{id}/activate"
        return self._client.post(path, body=body, params=query_parameters)

    def post_v2_api_keys_management_id_deactivate(self, id, body=None, query_parameters=None):
        path = f"/v2/api_keys_management/{id}/deactivate"
        return self._client.post(path, body=body, params=query_parameters)
