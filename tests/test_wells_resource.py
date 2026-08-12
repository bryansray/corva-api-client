from __future__ import annotations

from unittest.mock import Mock

from corva_api_client.resources import WellsClient


def test_search_serializes_company_id_as_company() -> None:
    client = Mock()
    client.get.return_value = {"data": []}
    wells = WellsClient(client)

    result = wells.search(company_id=80)

    assert result == {"data": []}
    client.get.assert_called_once_with(
        "/v2/wells",
        params={"company": 80, "fields": "*"},
    )
