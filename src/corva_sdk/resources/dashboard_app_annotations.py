from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_sdk.client import CorvaClient


class DashboardAppAnnotationsClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def get_v2_dashboard_app_annotations(self, query_parameters=None):
        path = "/v2/dashboard_app_annotations"
        return self._client.get(path, params=query_parameters)

    def post_v2_dashboard_app_annotations(self, body=None, query_parameters=None):
        path = "/v2/dashboard_app_annotations"
        return self._client.post(path, body=body, params=query_parameters)

    def get_v2_dashboard_app_annotations_last_annotations(self, query_parameters=None):
        path = "/v2/dashboard_app_annotations/last_annotations"
        return self._client.get(path, params=query_parameters)

    def get_v2_dashboard_app_annotations_app_annotation_id_comments(
        self, appAnnotationId, query_parameters=None
    ):
        path = f"/v2/dashboard_app_annotations/{appAnnotationId}/comments/"
        return self._client.get(path, params=query_parameters)

    def post_v2_dashboard_app_annotations_app_annotation_id_comments(
        self, appAnnotationId, body=None, query_parameters=None
    ):
        path = f"/v2/dashboard_app_annotations/{appAnnotationId}/comments/"
        return self._client.post(path, body=body, params=query_parameters)

    def get_v2_dashboard_app_annotations_app_annotation_id_comments_comment_id_likes(
        self, appAnnotationId, commentId, query_parameters=None
    ):
        path = f"/v2/dashboard_app_annotations/{appAnnotationId}/comments/{commentId}/likes"
        return self._client.get(path, params=query_parameters)

    def post_v2_dashboard_app_annotations_app_annotation_id_comments_comment_id_likes_toggle(
        self, appAnnotationId, commentId, body=None, query_parameters=None
    ):
        path = f"/v2/dashboard_app_annotations/{appAnnotationId}/comments/{commentId}/likes/toggle"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_dashboard_app_annotations_app_annotation_id_comments_id(
        self, appAnnotationId, id, body=None, query_parameters=None
    ):
        path = f"/v2/dashboard_app_annotations/{appAnnotationId}/comments/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_dashboard_app_annotations_app_annotation_id_comments_id(
        self, appAnnotationId, id, query_parameters=None
    ):
        path = f"/v2/dashboard_app_annotations/{appAnnotationId}/comments/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_dashboard_app_annotations_app_annotation_id_comments_id(
        self, appAnnotationId, id, body=None, query_parameters=None
    ):
        path = f"/v2/dashboard_app_annotations/{appAnnotationId}/comments/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def get_v2_dashboard_app_annotations_app_annotation_id_likes(
        self, appAnnotationId, query_parameters=None
    ):
        path = f"/v2/dashboard_app_annotations/{appAnnotationId}/likes"
        return self._client.get(path, params=query_parameters)

    def post_v2_dashboard_app_annotations_app_annotation_id_likes_toggle(
        self, appAnnotationId, body=None, query_parameters=None
    ):
        path = f"/v2/dashboard_app_annotations/{appAnnotationId}/likes/toggle"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_dashboard_app_annotations_id(self, id, body=None, query_parameters=None):
        path = f"/v2/dashboard_app_annotations/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_dashboard_app_annotations_id(self, id, query_parameters=None):
        path = f"/v2/dashboard_app_annotations/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_dashboard_app_annotations_id(self, id, body=None, query_parameters=None):
        path = f"/v2/dashboard_app_annotations/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def get_v2_dashboard_app_annotations_id_close(self, id, query_parameters=None):
        path = f"/v2/dashboard_app_annotations/{id}/close"
        return self._client.get(path, params=query_parameters)
