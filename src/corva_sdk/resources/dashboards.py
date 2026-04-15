from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_sdk.client import CorvaClient


class DashboardsClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list_for_user(self, userId, query_parameters=None):
        path = f"/v1/users/{userId}/dashboards"
        return self._client.get(path, params=query_parameters)

    def post_v1_users_user_id_dashboards_dashboard_id_dashboard_apps_bulk_create(
        self, userId, dashboardId, body=None, query_parameters=None
    ):
        path = f"/v1/users/{userId}/dashboards/{dashboardId}/dashboard_apps/bulk_create"
        return self._client.post(path, body=body, params=query_parameters)

    def get_v1_users_user_id_dashboards_id(self, userId, id, query_parameters=None):
        path = f"/v1/users/{userId}/dashboards/{id}"
        return self._client.get(path, params=query_parameters)

    def get_v2_dashboard_folder_shares(self, query_parameters=None):
        path = "/v2/dashboard_folder_shares"
        return self._client.get(path, params=query_parameters)

    def post_v2_dashboard_folder_shares(self, body=None, query_parameters=None):
        path = "/v2/dashboard_folder_shares"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_dashboard_folder_shares_id(self, id, body=None, query_parameters=None):
        path = f"/v2/dashboard_folder_shares/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def patch_v2_dashboard_folder_shares_id(self, id, body=None, query_parameters=None):
        path = f"/v2/dashboard_folder_shares/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def post_v2_dashboard_folder_shares_id_use(self, id, body=None, query_parameters=None):
        path = f"/v2/dashboard_folder_shares/{id}/use"
        return self._client.post(path, body=body, params=query_parameters)

    def get_v2_dashboards(self, query_parameters=None):
        path = "/v2/dashboards"
        return self._client.get(path, params=query_parameters)

    def get_v2_dashboards_templates(self, query_parameters=None):
        path = "/v2/dashboards/templates"
        return self._client.get(path, params=query_parameters)

    def get_v2_dashboards_id_available_timezones(self, id, query_parameters=None):
        path = f"/v2/dashboards/{id}/available_timezones"
        return self._client.get(path, params=query_parameters)

    def get_v2_users_user_id_dashboard_folders(self, userId, query_parameters=None):
        path = f"/v2/users/{userId}/dashboard_folders"
        return self._client.get(path, params=query_parameters)

    def post_v2_users_user_id_dashboard_folders(self, userId, body=None, query_parameters=None):
        path = f"/v2/users/{userId}/dashboard_folders"
        return self._client.post(path, body=body, params=query_parameters)

    def get_v2_users_user_id_dashboard_folders_dashboard_folder_id_dashboard_shares(
        self, userId, dashboardFolderId, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboard_folders/{dashboardFolderId}/dashboard_shares"
        return self._client.get(path, params=query_parameters)

    def post_v2_users_user_id_dashboard_folders_dashboard_folder_id_dashboard_shares(
        self, userId, dashboardFolderId, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboard_folders/{dashboardFolderId}/dashboard_shares"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_users_user_id_dashboard_folders_dashboard_folder_id_dashboard_shares_id(
        self, userId, dashboardFolderId, id, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboard_folders/{dashboardFolderId}/dashboard_shares/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def patch_v2_users_user_id_dashboard_folders_dashboard_folder_id_dashboard_shares_id(
        self, userId, dashboardFolderId, id, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboard_folders/{dashboardFolderId}/dashboard_shares/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def delete_v2_users_user_id_dashboard_folders_id(
        self, userId, id, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboard_folders/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def patch_v2_users_user_id_dashboard_folders_id(
        self, userId, id, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboard_folders/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def get_v2_users_user_id_dashboards(self, userId, query_parameters=None):
        path = f"/v2/users/{userId}/dashboards"
        return self._client.get(path, params=query_parameters)

    def post_v2_users_user_id_dashboards(self, userId, body=None, query_parameters=None):
        path = f"/v2/users/{userId}/dashboards"
        return self._client.post(path, body=body, params=query_parameters)

    def post_v2_users_user_id_dashboards_dashboard_id_dashboard_apps(
        self, userId, dashboardId, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboards/{dashboardId}/dashboard_apps"
        return self._client.post(path, body=body, params=query_parameters)

    def put_v2_users_user_id_dashboards_dashboard_id_dashboard_apps_batch_update(
        self, userId, dashboardId, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboards/{dashboardId}/dashboard_apps/batch_update"
        return self._client.put(path, body=body, params=query_parameters)

    def delete_v2_users_user_id_dashboards_dashboard_id_dashboard_apps_id(
        self, userId, dashboardId, id, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboards/{dashboardId}/dashboard_apps/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_users_user_id_dashboards_dashboard_id_dashboard_apps_id(
        self, userId, dashboardId, id, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboards/{dashboardId}/dashboard_apps/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_users_user_id_dashboards_dashboard_id_dashboard_apps_id(
        self, userId, dashboardId, id, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboards/{dashboardId}/dashboard_apps/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def get_v2_users_user_id_dashboards_dashboard_id_data_filters(
        self, userId, dashboardId, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboards/{dashboardId}/data_filters"
        return self._client.get(path, params=query_parameters)

    def post_v2_users_user_id_dashboards_dashboard_id_data_filters(
        self, userId, dashboardId, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboards/{dashboardId}/data_filters"
        return self._client.post(path, body=body, params=query_parameters)

    def post_v2_users_user_id_dashboards_dashboard_id_data_filters2(
        self, userId, dashboardId, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboards/{dashboardId}/data_filters#2"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_users_user_id_dashboards_dashboard_id_data_filters_id(
        self, userId, dashboardId, id, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboards/{dashboardId}/data_filters/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_users_user_id_dashboards_dashboard_id_data_filters_id(
        self, userId, dashboardId, id, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboards/{dashboardId}/data_filters/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_users_user_id_dashboards_dashboard_id_data_filters_id(
        self, userId, dashboardId, id, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboards/{dashboardId}/data_filters/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def delete_v2_users_user_id_dashboards_id(self, userId, id, body=None, query_parameters=None):
        path = f"/v2/users/{userId}/dashboards/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_users_user_id_dashboards_id(self, userId, id, query_parameters=None):
        path = f"/v2/users/{userId}/dashboards/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_users_user_id_dashboards_id(self, userId, id, body=None, query_parameters=None):
        path = f"/v2/users/{userId}/dashboards/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def post_v2_users_user_id_dashboards_id_clone(
        self, userId, id, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboards/{id}/clone"
        return self._client.post(path, body=body, params=query_parameters)

    def post_v2_users_user_id_dashboards_id_use_template(
        self, userId, id, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboards/{id}/use_template"
        return self._client.post(path, body=body, params=query_parameters)
