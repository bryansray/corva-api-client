from __future__ import annotations

from unittest.mock import Mock

from corva_api_client.resources import RigsClient


def test_search_serializes_company_id_as_company() -> None:
    client = Mock()
    client.get.return_value = {"data": []}
    rigs = RigsClient(client)

    result = rigs.search(company_id=80)

    assert result == {"data": []}
    client.get.assert_called_once_with(
        "/v2/rigs",
        params={"company": 80, "fields": "*", "sort": "-last_active_at"},
    )
