from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_sdk.client import CorvaClient


class AuditsClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters=None):
        path = "/v2/api_key_audits"
        return self._client.get(path, params=query_parameters)

    def get_v2_dataset_audits(self, query_parameters=None):
        path = "/v2/dataset_audits"
        return self._client.get(path, params=query_parameters)

    def get_v2_package_audits(self, query_parameters=None):
        path = "/v2/package_audits"
        return self._client.get(path, params=query_parameters)

    def get_v2_permission_audits(self, query_parameters=None):
        path = "/v2/permission_audits"
        return self._client.get(path, params=query_parameters)

    def get_v2_platform_subscription_audits(self, query_parameters=None):
        path = "/v2/platform_subscription_audits"
        return self._client.get(path, params=query_parameters)

    def get_v2_provisioning_subscription_audits(self, query_parameters=None):
        path = "/v2/provisioning_subscription_audits"
        return self._client.get(path, params=query_parameters)

    def get_v2_purchase_subscription_audits(self, query_parameters=None):
        path = "/v2/purchase_subscription_audits"
        return self._client.get(path, params=query_parameters)
