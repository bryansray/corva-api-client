from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_sdk.client import CorvaClient


class PartialWellRerunsClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters=None):
        path = "/v2/partial_reruns"
        return self._client.get(path, params=query_parameters)

    def post_v2_partial_reruns_list(self, body=None, query_parameters=None):
        path = "/v2/partial_reruns/list"
        return self._client.post(path, body=body, params=query_parameters)

    def get_v2_partial_reruns_id(self, id, query_parameters=None):
        path = f"/v2/partial_reruns/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_partial_reruns_id(self, id, body=None, query_parameters=None):
        path = f"/v2/partial_reruns/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def get_v2_partial_reruns_id_app_progress_app_id(self, id, appId, query_parameters=None):
        path = f"/v2/partial_reruns/{id}/app_progress/{appId}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_partial_reruns_id_app_progress_app_id(
        self, id, appId, body=None, query_parameters=None
    ):
        path = f"/v2/partial_reruns/{id}/app_progress/{appId}"
        return self._client.patch(path, body=body, params=query_parameters)

    def patch_v2_partial_reruns_id_cancel(self, id, body=None, query_parameters=None):
        path = f"/v2/partial_reruns/{id}/cancel"
        return self._client.patch(path, body=body, params=query_parameters)

    def patch_v2_partial_reruns_id_fail(self, id, body=None, query_parameters=None):
        path = f"/v2/partial_reruns/{id}/fail"
        return self._client.patch(path, body=body, params=query_parameters)

    def patch_v2_partial_reruns_id_restart(self, id, body=None, query_parameters=None):
        path = f"/v2/partial_reruns/{id}/restart"
        return self._client.patch(path, body=body, params=query_parameters)

    def patch_v2_partial_reruns_id_resume(self, id, body=None, query_parameters=None):
        path = f"/v2/partial_reruns/{id}/resume"
        return self._client.patch(path, body=body, params=query_parameters)

    def patch_v2_partial_reruns_id_start_merging(self, id, body=None, query_parameters=None):
        path = f"/v2/partial_reruns/{id}/start_merging"
        return self._client.patch(path, body=body, params=query_parameters)

    def patch_v2_partial_reruns_id_stop(self, id, body=None, query_parameters=None):
        path = f"/v2/partial_reruns/{id}/stop"
        return self._client.patch(path, body=body, params=query_parameters)

    def post_v2_wells_well_id_partial_reruns(self, wellId, body=None, query_parameters=None):
        path = f"/v2/wells/{wellId}/partial_reruns"
        return self._client.post(path, body=body, params=query_parameters)
