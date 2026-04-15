from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_sdk.client import CorvaClient


class WellViewClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def get_v2_integration_wellview_bha(self, query_parameters=None):
        path = "/v2/integration/wellview/bha"
        return self._client.get(path, params=query_parameters)

    def get_v2_integration_wellview_frac(self, query_parameters=None):
        path = "/v2/integration/wellview/frac"
        return self._client.get(path, params=query_parameters)

    def get_v2_integration_wellview_frac_stage_design(self, query_parameters=None):
        path = "/v2/integration/wellview/frac_stage_design"
        return self._client.get(path, params=query_parameters)

    def get_v2_integration_wellview_frac_stage_summary(self, query_parameters=None):
        path = "/v2/integration/wellview/frac_stage_summary"
        return self._client.get(path, params=query_parameters)

    def get_v2_integration_wellview_frac_stage_summary_calculated(self, query_parameters=None):
        path = "/v2/integration/wellview/frac_stage_summary_calculated"
        return self._client.get(path, params=query_parameters)

    def post_v2_integration_wellview_ingest(self, body=None, query_parameters=None):
        path = "/v2/integration/wellview/ingest"
        return self._client.post(path, body=body, params=query_parameters)

    def get_v2_integration_wellview_job_settings(self, query_parameters=None):
        path = "/v2/integration/wellview/job_settings"
        return self._client.get(path, params=query_parameters)

    def get_v2_integration_wellview_plugs(self, query_parameters=None):
        path = "/v2/integration/wellview/plugs"
        return self._client.get(path, params=query_parameters)

    def post_v2_integration_wellview_resolve(self, body=None, query_parameters=None):
        path = "/v2/integration/wellview/resolve"
        return self._client.post(path, body=body, params=query_parameters)
