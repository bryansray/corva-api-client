from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_api_client.client import CorvaClient


class ActivitiesClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters=None):
        path = "/v2/activities"
        return self._client.get(path, params=query_parameters)

    def get(self, id, query_parameters=None):
        path = f"/v2/activities/{id}"
        return self._client.get(path, params=query_parameters)

    def create(self, body=None, query_parameters=None):
        path = "/v2/activities"
        return self._client.post(path, body=body, params=query_parameters)

    def update(self, id, body=None, query_parameters=None):
        path = f"/v2/activities/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def delete(self, id, query_parameters=None):
        path = f"/v2/activities/{id}"
        return self._client.delete(path, params=query_parameters)
