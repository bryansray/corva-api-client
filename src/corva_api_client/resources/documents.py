from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_api_client.client import CorvaClient


class DocumentsClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, query_parameters=None):
        path = "/v2/documents"
        return self._client.get(path, params=query_parameters)

    def post_v2_documents(self, body=None, query_parameters=None):
        path = "/v2/documents"
        return self._client.post(path, body=body, params=query_parameters)

    def get_v2_documents_document_id_document_sections(self, documentId, query_parameters=None):
        path = f"/v2/documents/{documentId}/document_sections"
        return self._client.get(path, params=query_parameters)

    def post_v2_documents_document_id_document_sections(
        self, documentId, body=None, query_parameters=None
    ):
        path = f"/v2/documents/{documentId}/document_sections"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_documents_document_id_document_sections_id(
        self, documentId, id, body=None, query_parameters=None
    ):
        path = f"/v2/documents/{documentId}/document_sections/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_documents_document_id_document_sections_id(
        self, documentId, id, query_parameters=None
    ):
        path = f"/v2/documents/{documentId}/document_sections/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_documents_document_id_document_sections_id(
        self, documentId, id, body=None, query_parameters=None
    ):
        path = f"/v2/documents/{documentId}/document_sections/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def delete_v2_documents_id(self, id, body=None, query_parameters=None):
        path = f"/v2/documents/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_documents_id(self, id, query_parameters=None):
        path = f"/v2/documents/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_documents_id(self, id, body=None, query_parameters=None):
        path = f"/v2/documents/{id}"
        return self._client.patch(path, body=body, params=query_parameters)
