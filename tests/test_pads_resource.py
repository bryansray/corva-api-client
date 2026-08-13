from __future__ import annotations

from unittest.mock import Mock

from corva_api_client.resources import PadsClient


def test_search_serializes_company_id_as_company() -> None:
    client = Mock()
    client.get.return_value = {"data": []}
    pads = PadsClient(client)

    result = pads.search(company_id=80)

    assert result == {"data": []}
    client.get.assert_called_once_with(
        "/v2/pads",
        params={
            "company": 80,
            "fields": "*",
            "sort": "-last_active_at",
        },
    )
