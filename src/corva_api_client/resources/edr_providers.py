from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_api_client.client import CorvaClient


class EdrProvidersClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters=None):
        path = "/v2/edr_providers"
        return self._client.get(path, params=query_parameters)

    def post_v2_edr_providers(self, body=None, query_parameters=None):
        path = "/v2/edr_providers"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_edr_providers_id(self, id, body=None, query_parameters=None):
        path = f"/v2/edr_providers/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_edr_providers_id(self, id, query_parameters=None):
        path = f"/v2/edr_providers/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_edr_providers_id(self, id, body=None, query_parameters=None):
        path = f"/v2/edr_providers/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def post_v2_edr_providers_id_test_connection(self, id, body=None, query_parameters=None):
        path = f"/v2/edr_providers/{id}/test_connection"
        return self._client.post(path, body=body, params=query_parameters)
