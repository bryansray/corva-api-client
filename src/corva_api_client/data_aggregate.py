from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from jsonschema import Draft7Validator

from corva_api_client.dataset_names import normalize_data_api_target

DEFAULT_AGGREGATE_SORT: dict[str, int] = {"timestamp": -1}
DEFAULT_AGGREGATE_LIMIT = 1000

DATA_AGGREGATE_REQUEST_SCHEMA: dict[str, Any] = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Data Aggregate Request",
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "provider": {"type": "string", "minLength": 1},
        "dataset": {"type": "string", "minLength": 1},
        "match": {"type": "object"},
        "group": {"type": "object"},
        "project": {"type": "object"},
        "sort": {
            "type": "object",
            "additionalProperties": {"type": "integer"},
        },
        "limit": {"type": "integer", "minimum": 0},
        "skip": {"type": "integer", "minimum": 0},
    },
    "required": ["provider", "dataset"],
}


@dataclass(frozen=True)
class AggregateValidationIssue:
    path: str
    message: str


def validate_data_aggregate_request(
    request_json: dict[str, Any],
) -> list[AggregateValidationIssue]:
    validator = Draft7Validator(DATA_AGGREGATE_REQUEST_SCHEMA)
    issues: list[AggregateValidationIssue] = []

    for error in sorted(validator.iter_errors(request_json), key=lambda item: list(item.path)):
        path = ".".join(str(part) for part in error.path) or "<root>"
        issues.append(AggregateValidationIssue(path=path, message=error.message))

    match = request_json.get("match")
    if not isinstance(match, dict) or ("asset_id" not in match and "company_id" not in match):
        issues.append(
            AggregateValidationIssue(
                path="match",
                message=(
                    "Aggregate requests require 'asset_id' or 'company_id' in the 'match' object."
                ),
            )
        )

    return issues


def normalize_data_aggregate_request(request_json: dict[str, Any]) -> dict[str, Any]:
    provider, dataset = normalize_data_api_target(
        str(request_json["provider"]),
        str(request_json["dataset"]),
    )

    match = request_json.get("match")
    effective_match = dict(match) if isinstance(match, dict) else {}

    group = request_json.get("group")
    effective_group = dict(group) if isinstance(group, dict) else None

    project = request_json.get("project")
    effective_project = dict(project) if isinstance(project, dict) else None

    sort = request_json.get("sort")
    effective_sort = dict(sort) if isinstance(sort, dict) and sort else DEFAULT_AGGREGATE_SORT

    return {
        "provider": provider,
        "dataset": dataset,
        "match": effective_match,
        "group": effective_group,
        "project": effective_project,
        "sort": effective_sort,
        "limit": int(request_json.get("limit", DEFAULT_AGGREGATE_LIMIT)),
        "skip": request_json.get("skip"),
    }


def build_data_aggregate_http_request(request_json: dict[str, Any]) -> dict[str, Any]:
    normalized = normalize_data_aggregate_request(request_json)
    params: dict[str, Any] = {
        "match": json.dumps(normalized["match"]),
        "limit": str(normalized["limit"]),
        "sort": json.dumps(normalized["sort"]),
    }

    if normalized["group"] is not None:
        params["group"] = json.dumps(normalized["group"])

    if normalized["project"] is not None:
        params["project"] = json.dumps(normalized["project"])

    if normalized["skip"] is not None:
        params["skip"] = int(normalized["skip"])

    return {
        "path": f"/api/v1/data/{normalized['provider']}/{normalized['dataset']}/aggregate/",
        "params": params,
        "normalized": normalized,
    }
