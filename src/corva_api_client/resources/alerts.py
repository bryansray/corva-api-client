from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from corva_api_client.client import CorvaClient


class AlertInstancesClient:
    """Read-only access to V2 alert instances and their history."""

    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters: dict[str, Any] | None = None) -> Any:
        return self._client.get("/v2/alerts", params=query_parameters)

    def get(self, alert_id: int, query_parameters: dict[str, Any] | None = None) -> Any:
        return self._client.get(f"/v2/alerts/{alert_id}", params=query_parameters)

    def list_activities(
        self,
        alert_id: int,
        query_parameters: dict[str, Any] | None = None,
    ) -> Any:
        return self._client.get(
            f"/v2/alerts/{alert_id}/activities",
            params=query_parameters,
        )

    def list_occurrences(
        self,
        alert_id: int,
        query_parameters: dict[str, Any] | None = None,
    ) -> Any:
        return self._client.get(
            f"/v2/alerts/{alert_id}/occurrences",
            params=query_parameters,
        )


class AlertDefinitionsClient:
    """Read-only access to V2 alert definitions and templates."""

    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters: dict[str, Any] | None = None) -> Any:
        return self._client.get("/v2/alerts/definitions", params=query_parameters)

    def get(self, definition_id: int) -> Any:
        return self._client.get(f"/v2/alerts/definitions/{definition_id}")

    def list_templates(
        self,
        template_type: str,
        query_parameters: dict[str, Any] | None = None,
    ) -> Any:
        return self._client.get(
            f"/v2/alerts/definitions/templates/{template_type}",
            params=query_parameters,
        )

    def list_notification_types(self) -> Any:
        return self._client.get("/v2/alerts/notifications/types")


class AlertsClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client
        self.instances = AlertInstancesClient(client)
        self.definitions = AlertDefinitionsClient(client)

    def list(self, query_parameters=None):
        path = "/v1/alerts"
        return self._client.get(path, params=query_parameters)

    def acknowledge(self, body=None, query_parameters=None):
        path = "/v1/alerts/acknowledge"
        return self._client.post(path, body=body, params=query_parameters)

    def list_definitions(self, query_parameters=None):
        path = "/v1/alerts/definitions"
        return self._client.get(path, params=query_parameters)

    def details(self, query_parameters=None):
        path = "/v1/alerts/details"
        return self._client.get(path, params=query_parameters)

    def totals(self, query_parameters=None):
        path = "/v1/alerts/totals"
        return self._client.get(path, params=query_parameters)

    def acknowledge_by_id(self, alertId, body=None, query_parameters=None):
        path = f"/v1/alerts/{alertId}/acknowledge"
        return self._client.post(path, body=body, params=query_parameters)

    def classify(self, alertId, body=None, query_parameters=None):
        path = f"/v1/alerts/{alertId}/classify"
        return self._client.post(path, body=body, params=query_parameters)

    def list_comments(self, alertId, query_parameters=None):
        path = f"/v1/alerts/{alertId}/comments/"
        return self._client.get(path, params=query_parameters)

    def create_comment(self, alertId, body=None, query_parameters=None):
        path = f"/v1/alerts/{alertId}/comments/"
        return self._client.post(path, body=body, params=query_parameters)

    def get_comment(self, alertId, commentId, query_parameters=None):
        path = f"/v1/alerts/{alertId}/comments/{commentId}"
        return self._client.get(path, params=query_parameters)

    def update_comment(self, alertId, commentId, body=None, query_parameters=None):
        path = f"/v1/alerts/{alertId}/comments/{commentId}"
        return self._client.patch(path, body=body, params=query_parameters)

    def delete_comment(self, alertId, commentId, query_parameters=None):
        path = f"/v1/alerts/{alertId}/comments/{commentId}"
        return self._client.delete(path, params=query_parameters)
