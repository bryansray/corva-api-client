from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_sdk.client import CorvaClient


class AppSettingsTemplatesClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list_for_parent(self, appKey, query_parameters=None):
        path = f"/v2/apps/{appKey}/app_settings_templates"
        return self._client.get(path, params=query_parameters)

    def post_v2_apps_app_key_app_settings_templates(self, appKey, body=None, query_parameters=None):
        path = f"/v2/apps/{appKey}/app_settings_templates"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_apps_app_key_app_settings_templates_id(
        self, appKey, id, body=None, query_parameters=None
    ):
        path = f"/v2/apps/{appKey}/app_settings_templates/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_apps_app_key_app_settings_templates_id(self, appKey, id, query_parameters=None):
        path = f"/v2/apps/{appKey}/app_settings_templates/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_apps_app_key_app_settings_templates_id(
        self, appKey, id, body=None, query_parameters=None
    ):
        path = f"/v2/apps/{appKey}/app_settings_templates/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def post_v2_apps_app_key_app_settings_templates_id_copy(
        self, appKey, id, body=None, query_parameters=None
    ):
        path = f"/v2/apps/{appKey}/app_settings_templates/{id}/copy"
        return self._client.post(path, body=body, params=query_parameters)

    def post_v2_apps_app_key_app_settings_templates_id_publish(
        self, appKey, id, body=None, query_parameters=None
    ):
        path = f"/v2/apps/{appKey}/app_settings_templates/{id}/publish"
        return self._client.post(path, body=body, params=query_parameters)

    def post_v2_apps_app_key_app_settings_templates_id_share(
        self, appKey, id, body=None, query_parameters=None
    ):
        path = f"/v2/apps/{appKey}/app_settings_templates/{id}/share"
        return self._client.post(path, body=body, params=query_parameters)

    def post_v2_apps_app_key_app_settings_templates_id_unshare(
        self, appKey, id, body=None, query_parameters=None
    ):
        path = f"/v2/apps/{appKey}/app_settings_templates/{id}/unshare"
        return self._client.post(path, body=body, params=query_parameters)
