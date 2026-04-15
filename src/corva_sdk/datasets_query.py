from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

from jsonschema import Draft7Validator

from corva_sdk.data_fetch import DEFAULT_DATASET_SORT


@dataclass(frozen=True)
class QueryValidationIssue:
    path: str
    message: str


@dataclass(frozen=True)
class GraphSettings:
    y_fields: list[str]
    x_field: str = "timestamp"
    scale: str = "raw"
    mode: str = "static"
    poll_interval_seconds: float = 2.0
    window_size: int = 200
    incremental: bool = False
    incremental_field: str = "timestamp"


@dataclass(frozen=True)
class TableSettings:
    columns: list[str]
    sort_by: str | None = None
    sort_order: str = "asc"


def _schema_path() -> Path:
    return Path(__file__).resolve().parent / "schemas" / "datasets-query-schema.json"


def load_dataset_query_schema() -> dict[str, Any]:
    schema_path = _schema_path()
    return cast(dict[str, Any], json.loads(schema_path.read_text(encoding="utf-8")))


def validate_dataset_query_json(
    query_json: dict[str, Any],
) -> list[QueryValidationIssue]:
    validator = Draft7Validator(load_dataset_query_schema())
    issues: list[QueryValidationIssue] = []

    for error in sorted(validator.iter_errors(query_json), key=lambda item: list(item.path)):
        path = ".".join(str(part) for part in error.path) or "<root>"
        issues.append(QueryValidationIssue(path=path, message=error.message))

    return issues


def build_dataset_fetch_params(
    query_json: dict[str, Any],
    asset_id: int | None = None,
    page: int | None = None,
    per_page: int | None = None,
) -> dict[str, Any]:
    query_filter = dict(query_json.get("query") or {})
    resolved_asset_id = asset_id if asset_id is not None else query_json.get("assetId")
    if resolved_asset_id is not None:
        query_filter["asset_id"] = resolved_asset_id

    resolved_page = page if page is not None else query_json.get("page")
    resolved_per_page = per_page if per_page is not None else query_json.get("perPage")
    resolved_limit = query_json.get("limit", 100)
    resolved_skip = query_json.get("skip")

    if resolved_per_page is not None:
        resolved_limit = max(0, int(resolved_per_page))

    if resolved_page is not None:
        normalized_page = max(1, int(resolved_page))
        page_size = max(0, int(resolved_limit))
        resolved_skip = (normalized_page - 1) * page_size

    return {
        "provider": query_json.get("provider", "corva"),
        "dataset": query_json["dataset"],
        "query": query_filter or None,
        "sort": dict(query_json.get("sort") or DEFAULT_DATASET_SORT),
        "limit": resolved_limit,
        "skip": resolved_skip,
        "fields": query_json.get("fields"),
    }


def resolve_query_output_format(query_json: dict[str, Any]) -> str:
    settings = query_json.get("settings")
    if not isinstance(settings, dict):
        return "table"
    format_value = settings.get("format")
    return str(format_value) if format_value is not None else "table"


def build_graph_settings(query_json: dict[str, Any]) -> GraphSettings | None:
    if resolve_query_output_format(query_json) != "graph":
        return None

    settings = query_json.get("settings")
    if not isinstance(settings, dict):
        return None

    graph_settings = settings.get("graph")
    if not isinstance(graph_settings, dict):
        return None

    raw_y_field = graph_settings.get("yField")
    y_fields: list[str] = []
    if isinstance(raw_y_field, str) and raw_y_field.strip():
        y_fields = [raw_y_field.strip()]
    elif isinstance(raw_y_field, list):
        y_fields = [
            str(item).strip() for item in raw_y_field if isinstance(item, str) and item.strip()
        ]

    if not y_fields:
        return None

    x_field = graph_settings.get("xField")
    if not isinstance(x_field, str) or not x_field.strip():
        x_field = "timestamp"

    scale = graph_settings.get("scale")
    if not isinstance(scale, str) or not scale.strip():
        scale = "raw"

    mode = graph_settings.get("mode")
    if not isinstance(mode, str) or not mode.strip():
        mode = "static"

    poll_interval_seconds = graph_settings.get("pollIntervalSeconds")
    if not isinstance(poll_interval_seconds, (int, float)) or isinstance(
        poll_interval_seconds, bool
    ):
        poll_interval_seconds = 2.0
    else:
        poll_interval_seconds = float(poll_interval_seconds)

    window_size = graph_settings.get("windowSize")
    if not isinstance(window_size, int) or isinstance(window_size, bool):
        window_size = 200

    incremental = graph_settings.get("incremental")
    if not isinstance(incremental, bool):
        incremental = False

    incremental_field = graph_settings.get("incrementalField")
    if not isinstance(incremental_field, str) or not incremental_field.strip():
        incremental_field = "timestamp"

    return GraphSettings(
        y_fields=y_fields,
        x_field=x_field.strip(),
        scale=scale.strip(),
        mode=mode.strip(),
        poll_interval_seconds=poll_interval_seconds,
        window_size=window_size,
        incremental=incremental,
        incremental_field=incremental_field.strip(),
    )


def build_table_settings(query_json: dict[str, Any]) -> TableSettings:
    settings = query_json.get("settings")
    if not isinstance(settings, dict):
        return TableSettings(columns=[])

    table_settings = settings.get("table")
    if not isinstance(table_settings, dict):
        return TableSettings(columns=[])

    raw_columns = table_settings.get("columns")
    columns: list[str] = []
    if isinstance(raw_columns, list):
        columns = [
            str(item).strip() for item in raw_columns if isinstance(item, str) and item.strip()
        ]

    sort_by = table_settings.get("sortBy")
    if not isinstance(sort_by, str) or not sort_by.strip():
        sort_by = None
    else:
        sort_by = sort_by.strip()

    sort_order = table_settings.get("sortOrder")
    if not isinstance(sort_order, str) or not sort_order.strip():
        sort_order = "asc"
    else:
        sort_order = sort_order.strip()

    return TableSettings(columns=columns, sort_by=sort_by, sort_order=sort_order)
