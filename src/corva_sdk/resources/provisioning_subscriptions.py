from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_sdk.client import CorvaClient


class ProvisioningSubscriptionsClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters=None):
        path = "/v2/provisioning_subscriptions"
        return self._client.get(path, params=query_parameters)

    def post_v2_provisioning_subscriptions(self, body=None, query_parameters=None):
        path = "/v2/provisioning_subscriptions"
        return self._client.post(path, body=body, params=query_parameters)

    def get_v2_provisioning_subscriptions_id_app_streams(self, id, query_parameters=None):
        path = f"/v2/provisioning_subscriptions/{id}/app_streams"
        return self._client.get(path, params=query_parameters)

    def post_v2_provisioning_subscriptions_id_approve(self, id, body=None, query_parameters=None):
        path = f"/v2/provisioning_subscriptions/{id}/approve"
        return self._client.post(path, body=body, params=query_parameters)

    def post_v2_provisioning_subscriptions_id_deny(self, id, body=None, query_parameters=None):
        path = f"/v2/provisioning_subscriptions/{id}/deny"
        return self._client.post(path, body=body, params=query_parameters)

    def post_v2_provisioning_subscriptions_id_resume(self, id, body=None, query_parameters=None):
        path = f"/v2/provisioning_subscriptions/{id}/resume"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_provisioning_subscriptions_uuid(self, uuid, body=None, query_parameters=None):
        path = f"/v2/provisioning_subscriptions/{uuid}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_provisioning_subscriptions_uuid(self, uuid, query_parameters=None):
        path = f"/v2/provisioning_subscriptions/{uuid}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_provisioning_subscriptions_uuid(self, uuid, body=None, query_parameters=None):
        path = f"/v2/provisioning_subscriptions/{uuid}"
        return self._client.patch(path, body=body, params=query_parameters)

    def post_v2_provisioning_subscriptions_uuid_cancel(
        self, uuid, body=None, query_parameters=None
    ):
        path = f"/v2/provisioning_subscriptions/{uuid}/cancel"
        return self._client.post(path, body=body, params=query_parameters)
