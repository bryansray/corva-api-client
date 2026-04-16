from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_api_client.client import CorvaClient


class ApiKeysClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters=None):
        path = "/v2/api_keys"
        return self._client.get(path, params=query_parameters)

    def get(self, id, query_parameters=None):
        path = f"/v2/api_keys/{id}"
        return self._client.get(path, params=query_parameters)

    def create(self, body=None, query_parameters=None):
        path = "/v2/api_keys"
        return self._client.post(path, body=body, params=query_parameters)

    def update(self, id, body=None, query_parameters=None):
        path = f"/v2/api_keys/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def delete(self, id, query_parameters=None):
        path = f"/v2/api_keys/{id}"
        return self._client.delete(path, params=query_parameters)

    def approve(self, id, body=None, query_parameters=None):
        path = f"/v2/api_keys/{id}/approve"
        return self._client.post(path, body=body, params=query_parameters)

    def deactivate(self, id, body=None, query_parameters=None):
        path = f"/v2/api_keys/{id}/deactivate"
        return self._client.post(path, body=body, params=query_parameters)

    def list_managed(self, query_parameters=None):
        path = "/v2/api_keys_management"
        return self._client.get(path, params=query_parameters)

    def get_managed(self, id, query_parameters=None):
        path = f"/v2/api_keys_management/{id}"
        return self._client.get(path, params=query_parameters)

    def create_managed(self, body=None, query_parameters=None):
        path = "/v2/api_keys_management"
        return self._client.post(path, body=body, params=query_parameters)

    def update_managed(self, id, body=None, query_parameters=None):
        path = f"/v2/api_keys_management/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def delete_managed(self, id, query_parameters=None):
        path = f"/v2/api_keys_management/{id}"
        return self._client.delete(path, params=query_parameters)

    def activate_managed(self, id, body=None, query_parameters=None):
        path = f"/v2/api_keys_management/{id}/activate"
        return self._client.post(path, body=body, params=query_parameters)

    def deactivate_managed(self, id, body=None, query_parameters=None):
        path = f"/v2/api_keys_management/{id}/deactivate"
        return self._client.post(path, body=body, params=query_parameters)
