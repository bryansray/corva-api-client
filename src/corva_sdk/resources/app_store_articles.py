from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_sdk.client import CorvaClient


class AppStoreArticlesClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters=None):
        path = "/v2/app_store_articles"
        return self._client.get(path, params=query_parameters)

    def post_v2_app_store_articles(self, body=None, query_parameters=None):
        path = "/v2/app_store_articles"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_app_store_articles_id(self, id, body=None, query_parameters=None):
        path = f"/v2/app_store_articles/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_app_store_articles_id(self, id, query_parameters=None):
        path = f"/v2/app_store_articles/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_app_store_articles_id(self, id, body=None, query_parameters=None):
        path = f"/v2/app_store_articles/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def patch_v2_app_store_articles_id_remove_section(self, id, body=None, query_parameters=None):
        path = f"/v2/app_store_articles/{id}/remove_section"
        return self._client.patch(path, body=body, params=query_parameters)
