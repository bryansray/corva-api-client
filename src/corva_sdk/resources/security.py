from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from corva_sdk.client import CorvaClient


class SecurityClient:
    def __init__(self, client: "CorvaClient") -> None:
        self._client = client

    def list_groups(self, companyId, query_parameters=None):
        path = f"/v2/companies/{companyId}/security_policies"
        return self._client.get(path, params=query_parameters)

    def post_v2_companies_company_id_security_policies(
        self, companyId, body=None, query_parameters=None
    ):
        path = f"/v2/companies/{companyId}/security_policies"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_companies_company_id_security_policies_id(
        self, companyId, id, body=None, query_parameters=None
    ):
        path = f"/v2/companies/{companyId}/security_policies/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_companies_company_id_security_policies_id(
        self, companyId, id, query_parameters=None
    ):
        path = f"/v2/companies/{companyId}/security_policies/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_companies_company_id_security_policies_id(
        self, companyId, id, body=None, query_parameters=None
    ):
        path = f"/v2/companies/{companyId}/security_policies/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def get_v2_groups(self, query_parameters=None):
        path = "/v2/groups"
        return self._client.get(path, params=query_parameters)

    def post_v2_groups(self, body=None, query_parameters=None):
        path = "/v2/groups"
        return self._client.post(path, body=body, params=query_parameters)

    def post_v2_groups_copy_users(self, body=None, query_parameters=None):
        path = "/v2/groups/copy_users"
        return self._client.post(path, body=body, params=query_parameters)

    def post_v2_groups_group_id_assign_users(self, groupId, body=None, query_parameters=None):
        path = f"/v2/groups/{groupId}/assign_users"
        return self._client.post(path, body=body, params=query_parameters)

    def get_v2_groups_group_id_permissions(self, groupId, query_parameters=None):
        path = f"/v2/groups/{groupId}/permissions"
        return self._client.get(path, params=query_parameters)

    def post_v2_groups_group_id_permissions(self, groupId, body=None, query_parameters=None):
        path = f"/v2/groups/{groupId}/permissions"
        return self._client.post(path, body=body, params=query_parameters)

    def post_v2_groups_group_id_permissions_bulk_create(
        self, groupId, body=None, query_parameters=None
    ):
        path = f"/v2/groups/{groupId}/permissions/bulk_create"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_groups_group_id_permissions_bulk_destroy(
        self, groupId, body=None, query_parameters=None
    ):
        path = f"/v2/groups/{groupId}/permissions/bulk_destroy"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_groups_group_id_permissions_grouped(self, groupId, query_parameters=None):
        path = f"/v2/groups/{groupId}/permissions/grouped"
        return self._client.get(path, params=query_parameters)

    def delete_v2_groups_group_id_permissions_id(
        self, groupId, id, body=None, query_parameters=None
    ):
        path = f"/v2/groups/{groupId}/permissions/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_groups_group_id_permissions_id(self, groupId, id, query_parameters=None):
        path = f"/v2/groups/{groupId}/permissions/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_groups_group_id_permissions_id(
        self, groupId, id, body=None, query_parameters=None
    ):
        path = f"/v2/groups/{groupId}/permissions/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def delete_v2_groups_id(self, id, body=None, query_parameters=None):
        path = f"/v2/groups/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_groups_id(self, id, query_parameters=None):
        path = f"/v2/groups/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_groups_id(self, id, body=None, query_parameters=None):
        path = f"/v2/groups/{id}"
        return self._client.patch(path, body=body, params=query_parameters)

    def get_v2_groups_id_users(self, id, query_parameters=None):
        path = f"/v2/groups/{id}/users"
        return self._client.get(path, params=query_parameters)

    def delete_v2_groups_user_id_permissions_bulk_destroy(
        self, userId, body=None, query_parameters=None
    ):
        path = f"/v2/groups/{userId}/permissions/bulk_destroy"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_security_policies(self, query_parameters=None):
        path = "/v2/security_policies"
        return self._client.get(path, params=query_parameters)

    def get_v2_security_policies_id(self, id, query_parameters=None):
        path = f"/v2/security_policies/{id}"
        return self._client.get(path, params=query_parameters)

    def get_v2_users_user_id_groups(self, userId, query_parameters=None):
        path = f"/v2/users/{userId}/groups"
        return self._client.get(path, params=query_parameters)

    def post_v2_users_user_id_groups(self, userId, body=None, query_parameters=None):
        path = f"/v2/users/{userId}/groups"
        return self._client.post(path, body=body, params=query_parameters)

    def delete_v2_users_user_id_groups_id(self, userId, id, body=None, query_parameters=None):
        path = f"/v2/users/{userId}/groups/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_users_user_id_permissions(self, userId, query_parameters=None):
        path = f"/v2/users/{userId}/permissions"
        return self._client.get(path, params=query_parameters)

    def post_v2_users_user_id_permissions(self, userId, body=None, query_parameters=None):
        path = f"/v2/users/{userId}/permissions"
        return self._client.post(path, body=body, params=query_parameters)

    def post_v2_users_user_id_permissions_bulk_create(
        self, userId, body=None, query_parameters=None
    ):
        path = f"/v2/users/{userId}/permissions/bulk_create"
        return self._client.post(path, body=body, params=query_parameters)

    def get_v2_users_user_id_permissions_grouped(self, userId, query_parameters=None):
        path = f"/v2/users/{userId}/permissions/grouped"
        return self._client.get(path, params=query_parameters)

    def delete_v2_users_user_id_permissions_id(self, userId, id, body=None, query_parameters=None):
        path = f"/v2/users/{userId}/permissions/{id}"
        return self._client.delete(path, body=body, params=query_parameters)

    def get_v2_users_user_id_permissions_id(self, userId, id, query_parameters=None):
        path = f"/v2/users/{userId}/permissions/{id}"
        return self._client.get(path, params=query_parameters)

    def patch_v2_users_user_id_permissions_id(self, userId, id, body=None, query_parameters=None):
        path = f"/v2/users/{userId}/permissions/{id}"
        return self._client.patch(path, body=body, params=query_parameters)
