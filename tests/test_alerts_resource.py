from __future__ import annotations

from unittest.mock import Mock

from corva_api_client.resources import AlertsClient


def test_instances_list_uses_v2_filters() -> None:
    client = Mock()
    client.get.return_value = {"data": []}
    alerts = AlertsClient(client)
    filters = {"status": "open", "page": 2, "per_page": 50}

    result = alerts.instances.list(filters)

    assert result == {"data": []}
    client.get.assert_called_once_with("/v2/alerts", params=filters)


def test_instances_get_supports_sparse_fields() -> None:
    client = Mock()
    alerts = AlertsClient(client)

    alerts.instances.get(42, {"fields": "alert.status,alert.alert_at"})

    client.get.assert_called_once_with(
        "/v2/alerts/42",
        params={"fields": "alert.status,alert.alert_at"},
    )


def test_instances_list_activities_uses_v2_history_endpoint() -> None:
    client = Mock()
    alerts = AlertsClient(client)

    alerts.instances.list_activities(42, {"page": 3, "per_page": 25})

    client.get.assert_called_once_with(
        "/v2/alerts/42/activities",
        params={"page": 3, "per_page": 25},
    )


def test_instances_list_occurrences_uses_v2_history_endpoint() -> None:
    client = Mock()
    alerts = AlertsClient(client)

    alerts.instances.list_occurrences(42, {"start": 100, "end": 200})

    client.get.assert_called_once_with(
        "/v2/alerts/42/occurrences",
        params={"start": 100, "end": 200},
    )


def test_definitions_list_uses_v2_filters() -> None:
    client = Mock()
    alerts = AlertsClient(client)
    filters = {"search": "pressure", "segment": "drilling"}

    alerts.definitions.list(filters)

    client.get.assert_called_once_with("/v2/alerts/definitions", params=filters)


def test_definitions_get_uses_v2_endpoint() -> None:
    client = Mock()
    alerts = AlertsClient(client)

    alerts.definitions.get(73)

    client.get.assert_called_once_with("/v2/alerts/definitions/73")


def test_definitions_list_templates_uses_requested_shelf() -> None:
    client = Mock()
    alerts = AlertsClient(client)

    alerts.definitions.list_templates("standard", {"scope": "corva", "page": 2})

    client.get.assert_called_once_with(
        "/v2/alerts/definitions/templates/standard",
        params={"scope": "corva", "page": 2},
    )


def test_definitions_list_notification_types_uses_v2_endpoint() -> None:
    client = Mock()
    alerts = AlertsClient(client)

    alerts.definitions.list_notification_types()

    client.get.assert_called_once_with("/v2/alerts/notifications/types")


def test_legacy_alert_methods_remain_v1() -> None:
    client = Mock()
    alerts = AlertsClient(client)

    alerts.list_definitions({"type": "personal"})

    client.get.assert_called_once_with(
        "/v1/alerts/definitions",
        params={"type": "personal"},
    )
