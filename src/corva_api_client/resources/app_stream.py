from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from corva_api_client.client import CorvaClient


class AppStreamClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters=None):
        path = "/v1/app_streams"
        return self._client.get(path, params=query_parameters)

    def post_v1_app_streams(self, body=None, query_parameters=None):
        path = "/v1/app_streams"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v1_app_streams_batch_destroy(self, body=None, query_parameters=None):
        path = "/v1/app_streams/batch_destroy"
        return self._client.delete(path, body=body, params=query_parameters)

    def patch_v1_app_streams_batch_update(self, body=None, query_parameters=None):
        path = "/v1/app_streams/batch_update"
        return self._client.patch(path, body=body, params=query_parameters)

    def delete_v1_app_streams_id(self, id, body=None, query_parameters=None):
        path = f"/v1/app_streams/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v1_app_streams_id(self, id, query_parameters=None):
        path = f"/v1/app_streams/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v1_app_streams_id(self, id, body=None, query_parameters=None):
        path = f"/v1/app_streams/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def post_v1_app_streams_id_clone(self, id, body=None, query_parameters=None):
        path = f"/v1/app_streams/{id}/clone"
        return self._client.post(path, body=body, params=query_parameters)

    def post_v1_app_streams_id_create_backfill_stream(self, id, body=None, query_parameters=None):
        path = f"/v1/app_streams/{id}/create_backfill_stream"
        return self._client.post(path, body=body, params=query_parameters)

    def post_v1_app_streams_id_force_resume(self, id, body=None, query_parameters=None):
        path = f"/v1/app_streams/{id}/force_resume"
        return self._client.post(path, body=body, params=query_parameters)

    def patch_v1_app_streams_id_update_edr_provider_connection_status(
        self, id, body=None, query_parameters=None
    ):
        path = f"/v1/app_streams/{id}/update_edr_provider_connection_status"
        return self._client.patch(path, body=body, params=query_parameters)

    def get_v2_app_streams(self, query_parameters=None):
        path = "/v2/app_streams"
        return self._client.get(path, params=query_parameters)

    def search(
        self,
        *,
        company_id: int | None = None,
        asset_id: int | None = None,
        sort: str | None = None,
        status: str | None = None,
        type: str | None = None,
        log_type: str | None = None,
        source_type: str | None = None,
        data_received_at: str | None = None,
        last_active_at: str | None = None,
        search: str | None = None,
        app_id: int | None = None,
        per_page: int | None = None,
        page: int | None = None,
    ):
        params: dict[str, Any] = {}

        if company_id is not None:
            params["company_id"] = company_id
        if asset_id is not None:
            params["asset_id"] = asset_id
        if sort:
            params["sort"] = sort
        if status:
            params["status"] = status
        if type:
            params["type"] = type
        if log_type:
            params["log_type"] = log_type
        if source_type:
            params["source_type"] = source_type
        if data_received_at:
            params["data_received_at"] = data_received_at
        if last_active_at:
            params["last_active_at"] = last_active_at
        if search:
            params["search"] = search
        if app_id is not None:
            params["app_id"] = app_id
        if per_page is not None:
            params["per_page"] = per_page
        if page is not None:
            params["page"] = page

        return self.get_v2_app_streams(query_parameters=params or None)

    def get_v2_app_streams_idle_worker_stats(self, query_parameters=None):
        path = "/v2/app_streams/idle_worker_stats"
        return self._client.get(path, params=query_parameters)

    def get_v2_app_streams_id(self, id, query_parameters=None):
        path = f"/v2/app_streams/{id}"
        return self._client.get(path, params=query_parameters)
