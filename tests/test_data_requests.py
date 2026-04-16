from __future__ import annotations

from corva_api_client.data_aggregate import (
    build_data_aggregate_http_request,
    validate_data_aggregate_request,
)
from corva_api_client.data_fetch import build_data_fetch_http_request, validate_data_fetch_request
from corva_api_client.dataset_names import normalize_data_api_target


def test_normalize_data_api_target_supports_qualified_dataset() -> None:
    provider, dataset = normalize_data_api_target("corva", "custom#events")

    assert provider == "custom"
    assert dataset == "events"


def test_build_data_fetch_http_request_normalizes_fields_and_dataset() -> None:
    request = build_data_fetch_http_request(
        {
            "provider": "corva",
            "dataset": "custom#events",
            "query": {"asset_id": 123},
            "sort": {"timestamp": -1},
            "limit": 50,
            "skip": 10,
            "fields": [" timestamp ", "", "asset_id"],
        }
    )

    assert request["path"] == "/api/v1/data/custom/events/"
    assert request["params"]["limit"] == "50"
    assert request["params"]["skip"] == 10
    assert request["params"]["fields"] == "timestamp,asset_id"
    assert request["normalized"]["provider"] == "custom"
    assert request["normalized"]["dataset"] == "events"


def test_validate_data_fetch_request_reports_missing_dataset() -> None:
    issues = validate_data_fetch_request({"provider": "corva", "query": {}})

    assert len(issues) == 1
    assert issues[0].path == "<root>"


def test_build_data_aggregate_http_request_serializes_match_group_and_project() -> None:
    request = build_data_aggregate_http_request(
        {
            "provider": "corva",
            "dataset": "wits.summary-1ft",
            "match": {"asset_id": 123},
            "group": {"_id": "$asset_id"},
            "project": {"asset_id": 1},
            "sort": {"timestamp": -1},
            "limit": 25,
            "skip": 5,
        }
    )

    assert request["path"] == "/api/v1/data/corva/wits.summary-1ft/aggregate/"
    assert request["params"]["limit"] == "25"
    assert request["params"]["skip"] == 5
    assert request["params"]["match"] == '{"asset_id": 123}'
    assert request["params"]["group"] == '{"_id": "$asset_id"}'
    assert request["params"]["project"] == '{"asset_id": 1}'


def test_validate_data_aggregate_request_requires_match_identifier() -> None:
    issues = validate_data_aggregate_request(
        {"provider": "corva", "dataset": "wits.summary-1ft", "match": {}}
    )

    assert any(issue.path == "match" for issue in issues)
