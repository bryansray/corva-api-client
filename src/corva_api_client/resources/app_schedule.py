from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_api_client.client import CorvaClient


class AppScheduleClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def post_v1_app_schedules(self, body=None, query_parameters=None):
        path = "/v1/app_schedules"
        return self._client.post(path, body=body, params=query_parameters)

    def post_v1_app_schedules_bulk_update_status(self, body=None, query_parameters=None):
        path = "/v1/app_schedules/bulk_update_status"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v1_app_schedules_id(self, id, body=None, query_parameters=None):
        path = f"/v1/app_schedules/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v1_app_schedules_id(self, id, query_parameters=None):
        path = f"/v1/app_schedules/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v1_app_schedules_id(self, id, body=None, query_parameters=None):
        path = f"/v1/app_schedules/{id}"
        return self._client.patch(path, body=body, params=query_parameters)
