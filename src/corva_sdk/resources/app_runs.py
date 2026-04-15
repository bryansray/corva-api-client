from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_sdk.client import CorvaClient


class AppRunsClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list_for_parent(self, appId, query_parameters=None):
        path = f"/v2/apps/{appId}/app_runs"
        return self._client.get(path, params=query_parameters)

    def post_v2_apps_app_id_app_runs(self, appId, body=None, query_parameters=None):
        path = f"/v2/apps/{appId}/app_runs"
        return self._client.post(path, body=body, params=query_parameters)

    def get_v2_apps_app_id_app_runs_duplicate_check(self, appId, query_parameters=None):
        path = f"/v2/apps/{appId}/app_runs/duplicate_check"
        return self._client.get(path, params=query_parameters)

    def delete_v2_apps_app_id_app_runs_id(self, appId, id, body=None, query_parameters=None):
        path = f"/v2/apps/{appId}/app_runs/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_apps_app_id_app_runs_id(self, appId, id, query_parameters=None):
        path = f"/v2/apps/{appId}/app_runs/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_apps_app_id_app_runs_id(self, appId, id, body=None, query_parameters=None):
        path = f"/v2/apps/{appId}/app_runs/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def patch_v2_apps_app_id_app_runs_id_stop(self, appId, id, body=None, query_parameters=None):
        path = f"/v2/apps/{appId}/app_runs/{id}/stop"
        return self._client.patch(path, body=body, params=query_parameters)
