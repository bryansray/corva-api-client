from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_api_client.client import CorvaClient


class UsersClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def current(self, query_parameters=None):
        path = "/v1/users/current"
        return self._client.get(path, params=query_parameters)

    def get_jwks(self):
        path = "/v1/.well-known/jwks.json"
        return self._client.get(path)

    def session_schemas(self):
        path = "/v1/sessions/schemas"
        return self._client.get(path)

    def request_verification(self, body=None):
        path = "/v1/sessions/verification/request"
        return self._client.post(path, body=body)

    def list(self, query_parameters=None):
        path = "/v2/users"
        return self._client.get(path, params=query_parameters)

    def get(self, id, query_parameters=None):
        path = f"/v2/users/{id}"
        return self._client.get(path, params=query_parameters)

    def create(self, body=None, query_parameters=None):
        path = "/v2/users"
        return self._client.post(path, body=body, params=query_parameters)

    def update(self, id, body=None, query_parameters=None):
        path = f"/v2/users/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def delete(self, id, query_parameters=None):
        path = f"/v2/users/{id}"
        return self._client.delete(path, params=query_parameters)

    def export(self, query_parameters=None):
        path = "/v2/users/export"
        return self._client.get(path, params=query_parameters)

    def streaks(self, query_parameters=None):
        path = "/v2/users/streaks"
        return self._client.get(path, params=query_parameters)

    def get_settings(self, userId, query_parameters=None):
        path = f"/v2/users/{userId}/settings"
        return self._client.get(path, params=query_parameters)

    def upsert_settings(self, userId, body=None, query_parameters=None):
        path = f"/v2/users/{userId}/settings"
        return self._client.post(path, body=body, params=query_parameters)
