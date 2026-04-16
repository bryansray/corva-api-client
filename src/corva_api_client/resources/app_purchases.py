from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_api_client.client import CorvaClient


class AppPurchasesClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters=None):
        path = "/v2/app_purchases"
        return self._client.get(path, params=query_parameters)

    def post_v2_app_purchases(self, body=None, query_parameters=None):
        path = "/v2/app_purchases"
        return self._client.post(path, body=body, params=query_parameters)

    def get_v2_app_purchases_id(self, id, query_parameters=None):
        path = f"/v2/app_purchases/{id}"
        return self._client.get(path, params=query_parameters)

    def post_v2_app_purchases_id_approve(self, id, body=None, query_parameters=None):
        path = f"/v2/app_purchases/{id}/approve"
        return self._client.post(path, body=body, params=query_parameters)

    def post_v2_app_purchases_id_deny(self, id, body=None, query_parameters=None):
        path = f"/v2/app_purchases/{id}/deny"
        return self._client.post(path, body=body, params=query_parameters)

    def post_v2_app_purchases_id_resume(self, id, body=None, query_parameters=None):
        path = f"/v2/app_purchases/{id}/resume"
        return self._client.post(path, body=body, params=query_parameters)
