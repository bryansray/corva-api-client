from __future__ import annotations

from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from corva_api_client.client import CorvaClient


class WorkflowsClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list(self, userId, dashboardId, query_parameters=None):
        path = f"/v2/users/{userId}/dashboards/{dashboardId}/dashboard_workflows"
        return self._client.get(path, params=query_parameters)

    def post_v2_users_user_id_dashboards_dashboard_id_dashboard_workflows_ungroup_all(
        self, userId, dashboardId, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboards/{dashboardId}/dashboard_workflows/ungroup_all"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_users_user_id_dashboards_dashboard_id_dashboard_workflows_id(
        self, userId, dashboardId, id, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboards/{dashboardId}/dashboard_workflows/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_users_user_id_dashboards_dashboard_id_dashboard_workflows_id(
        self, userId, dashboardId, id, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboards/{dashboardId}/dashboard_workflows/{id}"
        return self._client.get(path, params=query_parameters)

    def put_v2_users_user_id_dashboards_dashboard_id_dashboard_workflows_id_change_asset(
        self, userId, dashboardId, id, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboards/{dashboardId}/dashboard_workflows/{id}/change_asset"
        return self._client.put(path, body=body, params=query_parameters)

    def post_v2_users_user_id_dashboards_dashboard_id_dashboard_workflows_id_ungroup(
        self, userId, dashboardId, id, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/dashboards/{dashboardId}/dashboard_workflows/{id}/ungroup"
        return self._client.post(path, body=body, params=query_parameters)

    def get_v2_workflows(self, query_parameters=None):
        path = "/v2/workflows"
        return self._client.get(path, params=query_parameters)

    def list_workflows(
        self,
        query_parameters: dict[str, Any] | None = None,
    ):
        return self.get_v2_workflows(query_parameters=query_parameters)

    def post_v2_workflows(self, body=None, query_parameters=None):
        path = "/v2/workflows"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_workflows_id(self, id, body=None, query_parameters=None):
        path = f"/v2/workflows/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_workflows_id(self, id, query_parameters=None):
        path = f"/v2/workflows/{id}"
        return self._client.get(path, params=query_parameters)

    def get_workflow(
        self,
        workflow_id: int,
        query_parameters: dict[str, Any] | None = None,
    ):
        return self.get_v2_workflows_id(workflow_id, query_parameters=query_parameters)

    def patch_v2_workflows_id(self, id, body=None, query_parameters=None):
        path = f"/v2/workflows/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def get_v2_workflow_id_workflow_apps(self, workflowId, query_parameters=None):
        path = f"/v2/workflows/{workflowId}/workflow_apps"
        return self._client.get(path, params=query_parameters)

    def list_workflow_apps(
        self,
        workflow_id: int,
        query_parameters: dict[str, Any] | None = None,
    ):
        return self.get_v2_workflow_id_workflow_apps(workflow_id, query_parameters=query_parameters)

    def put_v2_workflow_id_workflow_apps(self, workflowId, body=None, query_parameters=None):
        path = f"/v2/workflows/{workflowId}/workflow_apps"
        return self._client.put(path, body=body, params=query_parameters)

    def get_v2_workflow_id_workflow_apps_id(self, workflowId, id, query_parameters=None):
        path = f"/v2/workflows/{workflowId}/workflow_apps/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_workflow_id_workflow_apps_id(
        self, workflowId, id, body=None, query_parameters=None
    ):
        path = f"/v2/workflows/{workflowId}/workflow_apps/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def get_v2_workflow_id_workflow_content_blocks(self, workflowId, query_parameters=None):
        path = f"/v2/workflows/{workflowId}/workflow_content_blocks"
        return self._client.get(path, params=query_parameters)

    def post_v2_workflow_id_workflow_content_blocks(
        self, workflowId, body=None, query_parameters=None
    ):
        path = f"/v2/workflows/{workflowId}/workflow_content_blocks"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_workflow_id_workflow_content_blocks_id(
        self, workflowId, id, body=None, query_parameters=None
    ):
        path = f"/v2/workflows/{workflowId}/workflow_content_blocks/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_workflow_id_workflow_content_blocks_id(self, workflowId, id, query_parameters=None):
        path = f"/v2/workflows/{workflowId}/workflow_content_blocks/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_workflow_id_workflow_content_blocks_id(
        self, workflowId, id, body=None, query_parameters=None
    ):
        path = f"/v2/workflows/{workflowId}/workflow_content_blocks/{id}"
        return self._client.patch(path, body=body, params=query_parameters)
