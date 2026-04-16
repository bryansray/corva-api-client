from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_api_client.client import CorvaClient


class ColumnMapperTemplatesClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters=None):
        path = "/v2/column_mapper_templates"
        return self._client.get(path, params=query_parameters)

    def post_v2_column_mapper_templates(self, body=None, query_parameters=None):
        path = "/v2/column_mapper_templates"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_column_mapper_templates_id(self, id, body=None, query_parameters=None):
        path = f"/v2/column_mapper_templates/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_column_mapper_templates_id(self, id, query_parameters=None):
        path = f"/v2/column_mapper_templates/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_column_mapper_templates_id(self, id, body=None, query_parameters=None):
        path = f"/v2/column_mapper_templates/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def put_v2_column_mapper_templates_id_add_asset(self, id, body=None, query_parameters=None):
        path = f"/v2/column_mapper_templates/{id}/add_asset"
        return self._client.put(path, body=body, params=query_parameters)

    def put_v2_column_mapper_templates_id_remove_asset(self, id, body=None, query_parameters=None):
        path = f"/v2/column_mapper_templates/{id}/remove_asset"
        return self._client.put(path, body=body, params=query_parameters)
