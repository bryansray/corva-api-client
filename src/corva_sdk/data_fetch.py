from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from jsonschema import Draft7Validator

from corva_sdk.dataset_names import normalize_data_api_target

DEFAULT_DATASET_SORT: dict[str, int] = {"timestamp": -1}

DATA_FETCH_REQUEST_SCHEMA: dict[str, Any] = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Data Fetch Request",
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "provider": {"type": "string", "minLength": 1},
        "dataset": {"type": "string", "minLength": 1},
        "query": {"type": "object"},
        "sort": {
            "type": "object",
            "additionalProperties": {"type": "integer"},
        },
        "limit": {"type": "integer", "minimum": 0},
        "skip": {"type": "integer", "minimum": 0},
        "fields": {
            "type": "array",
            "items": {"type": "string"},
        },
    },
    "required": ["provider", "dataset", "query"],
}


@dataclass(frozen=True)
class QueryValidationIssue:
    path: str
    message: str


def validate_data_fetch_request(
    request_json: dict[str, Any],
) -> list[QueryValidationIssue]:
    validator = Draft7Validator(DATA_FETCH_REQUEST_SCHEMA)
    issues: list[QueryValidationIssue] = []

    for error in sorted(validator.iter_errors(request_json), key=lambda item: list(item.path)):
        path = ".".join(str(part) for part in error.path) or "<root>"
        issues.append(QueryValidationIssue(path=path, message=error.message))

    return issues


def normalize_data_fetch_request(request_json: dict[str, Any]) -> dict[str, Any]:
    provider, dataset = normalize_data_api_target(
        str(request_json["provider"]),
        str(request_json["dataset"]),
    )

    query = request_json.get("query")
    query_filter = dict(query) if isinstance(query, dict) else {}

    sort = request_json.get("sort")
    effective_sort = dict(sort) if isinstance(sort, dict) and sort else DEFAULT_DATASET_SORT

    fields = request_json.get("fields")
    cleaned_fields = None
    if isinstance(fields, list):
        cleaned_fields = [
            field.strip() for field in fields if isinstance(field, str) and field.strip()
        ]
        if not cleaned_fields:
            cleaned_fields = None

    return {
        "provider": provider,
        "dataset": dataset,
        "query": query_filter,
        "sort": effective_sort,
        "limit": int(request_json.get("limit", 100)),
        "skip": request_json.get("skip"),
        "fields": cleaned_fields,
    }


def build_data_fetch_http_request(request_json: dict[str, Any]) -> dict[str, Any]:
    normalized = normalize_data_fetch_request(request_json)
    params: dict[str, Any] = {}

    params["query"] = json.dumps(normalized["query"])
    params["sort"] = json.dumps(normalized["sort"])
    params["limit"] = str(normalized["limit"])

    if normalized["skip"] is not None:
        params["skip"] = int(normalized["skip"])

    if normalized["fields"]:
        params["fields"] = ",".join(normalized["fields"])

    return {
        "path": f"/api/v1/data/{normalized['provider']}/{normalized['dataset']}/",
        "params": params,
        "normalized": normalized,
    }
