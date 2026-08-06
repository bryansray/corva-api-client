from __future__ import annotations

from typing import Any, cast
from unittest.mock import Mock

import httpx
import pytest

from corva_api_client.resources import AssetsClient, AssetStatus


def test_search_includes_visibility() -> None:
    client = Mock()
    client.get.return_value = {"data": []}
    assets = AssetsClient(client)

    result = assets.search(visibility="company")

    assert result == {"data": []}
    client.get.assert_called_once_with(
        "/v2/assets",
        params={
            "fields": "*",
            "sort": "-last_active_at",
            "visibility": "company",
        },
    )


@pytest.mark.parametrize(
    ("status", "expected"),
    [
        (AssetStatus.ACTIVE, ["active"]),
        ([AssetStatus.ACTIVE, AssetStatus.PAUSED], ["active", "paused"]),
        ("active, paused", ["active", "paused"]),
    ],
)
def test_search_serializes_statuses(status, expected: list[str]) -> None:
    client = Mock()
    assets = AssetsClient(client)

    assets.search(status=status)

    params = client.get.call_args.kwargs["params"]
    assert params["status[]"] == expected


def test_search_encodes_multiple_statuses_as_repeated_array_parameters() -> None:
    client = Mock()
    assets = AssetsClient(client)

    assets.search(status=[AssetStatus.ACTIVE, AssetStatus.PAUSED])

    params = httpx.QueryParams(client.get.call_args.kwargs["params"])
    assert params.multi_items() == [
        ("status[]", "active"),
        ("status[]", "paused"),
        ("fields", "*"),
        ("sort", "-last_active_at"),
    ]


def test_search_rejects_invalid_status_before_request() -> None:
    client = Mock()
    assets = AssetsClient(client)

    with pytest.raises(ValueError, match="Invalid asset status 'all'"):
        assets.search(status=cast(Any, "all"))

    client.get.assert_not_called()


def test_search_omits_empty_status_collection() -> None:
    client = Mock()
    assets = AssetsClient(client)

    assets.search(status=[])

    assert "status[]" not in client.get.call_args.kwargs["params"]
