from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_sdk.client import CorvaClient


class PicklistsClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters=None):
        path = "/v2/picklists"
        return self._client.get(path, params=query_parameters)

    def post_v2_picklists(self, body=None, query_parameters=None):
        path = "/v2/picklists"
        return self._client.post(path, body=body, params=query_parameters)

    def get_v2_picklists_name(self, name, query_parameters=None):
        path = f"/v2/picklists/{name}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_picklists_name(self, name, body=None, query_parameters=None):
        path = f"/v2/picklists/{name}"
        return self._client.patch(path, body=body, params=query_parameters)

    def post_v2_picklists_name_items(self, name, body=None, query_parameters=None):
        path = f"/v2/picklists/{name}/items"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_picklists_name_items_id(self, name, id, body=None, query_parameters=None):
        path = f"/v2/picklists/{name}/items/{id}"
        return self._client.delete(path, body=body, params=query_parameters)
