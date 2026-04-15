from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_sdk.client import CorvaClient


class FilesClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def upload(self, body=None, query_parameters=None):
        path = "/v1/file"
        return self._client.post(path, body=body, params=query_parameters)

    def replace(self, body=None, query_parameters=None):
        path = "/v1/file"
        return self._client.put(path, body=body, params=query_parameters)

    def delete(self, body=None, query_parameters=None):
        path = "/v1/file/delete"
        return self._client.delete(path, body=body, params=query_parameters)

    def download(self, query_parameters=None):
        path = "/v1/file/download"
        return self._client.get(path, params=query_parameters)

    def download_link(self, query_parameters=None):
        path = "/v1/file/download_link"
        return self._client.get(path, params=query_parameters)

    def preview(self, query_parameters=None):
        path = "/v1/file/preview"
        return self._client.get(path, params=query_parameters)

    def sign(self, query_parameters=None):
        path = "/v1/file/sign"
        return self._client.get(path, params=query_parameters)

    def delete_v2(self, body=None, query_parameters=None):
        path = "/v2/files"
        return self._client.delete(path, body=body, params=query_parameters)

    def url_v2(self, query_parameters=None):
        path = "/v2/files/url"
        return self._client.get(path, params=query_parameters)
