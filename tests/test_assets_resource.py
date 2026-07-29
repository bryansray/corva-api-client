from __future__ import annotations

from unittest.mock import Mock

from corva_api_client.resources import AssetsClient


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
