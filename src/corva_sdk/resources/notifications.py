from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_sdk.client import CorvaClient


class NotificationsClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters=None):
        path = "/v1/notifications"
        return self._client.get(path, params=query_parameters)

    def get(self, id, query_parameters=None):
        path = f"/v1/notifications/{id}"
        return self._client.get(path, params=query_parameters)

    def update(self, id, body=None, query_parameters=None):
        path = f"/v1/notifications/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def acknowledge(self, body=None, query_parameters=None):
        path = "/v1/notifications/acknowledge"
        return self._client.post(path, body=body, params=query_parameters)

    def acknowledge_all(self, body=None, query_parameters=None):
        path = "/v1/notifications/acknowledge_all"
        return self._client.post(path, body=body, params=query_parameters)

    def acknowledge_by_id(self, id, body=None, query_parameters=None):
        path = f"/v1/notifications/{id}/acknowledge"
        return self._client.post(path, body=body, params=query_parameters)

    def unread_count(self, query_parameters=None):
        path = "/v1/notifications/count/unread"
        return self._client.get(path, params=query_parameters)
