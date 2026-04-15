from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_sdk.client import CorvaClient


class TasksClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters=None):
        path = "/v2/tasks"
        return self._client.get(path, params=query_parameters)

    def post_v2_tasks(self, body=None, query_parameters=None):
        path = "/v2/tasks"
        return self._client.post(path, body=body, params=query_parameters)

    def get_v2_tasks_id(self, id, query_parameters=None):
        path = f"/v2/tasks/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_tasks_id(self, id, body=None, query_parameters=None):
        path = f"/v2/tasks/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def put_v2_tasks_id_status(self, id, status, body=None, query_parameters=None):
        path = f"/v2/tasks/{id}/{status}"
        return self._client.put(path, body=body, params=query_parameters)
