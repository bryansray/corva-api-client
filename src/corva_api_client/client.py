from __future__ import annotations

import logging
import re
from pprint import pformat
from typing import Any, cast
from urllib.parse import unquote

import httpx

from .config import CorvaConfig
from .resources import (
    ActivitiesClient,
    AlertsClient,
    ApiKeyClient,
    ApiKeysClient,
    AppConnectionClient,
    AppPurchasesClient,
    AppRunsClient,
    AppScheduleClient,
    AppsClient,
    AppSettingsTemplatesClient,
    AppStoreArticlesClient,
    AppStreamClient,
    AssetsClient,
    AuditsClient,
    ColumnMapperTemplatesClient,
    CompaniesClient,
    DashboardAppAnnotationsClient,
    DashboardsClient,
    DataClient,
    DatasetsClient,
    DocumentsClient,
    EdrProvidersClient,
    FeedClient,
    FilesClient,
    NotificationsClient,
    PadsClient,
    PartialWellRerunsClient,
    PicklistsClient,
    PlatformSubscriptionsClient,
    ProductSubscriptionsClient,
    ProjectsClient,
    ProvisioningSubscriptionsClient,
    RigsClient,
    SecurityClient,
    TasksClient,
    UsersClient,
    WellsClient,
    WellViewClient,
    WorkflowsClient,
)

logger = logging.getLogger(__name__)


class CorvaClient:
    def __init__(
        self,
        config: CorvaConfig | None = None,
        *,
        base_api_url: str | None = None,
        base_data_api_url: str | None = None,
        api_key: str | None = None,
        app_key: str | None = None,
        auth_kind: str = "api_key",
    ):
        if config is not None:
            base_api_url = config.base_api_url
            base_data_api_url = config.base_data_api_url
            api_key = config.api_key
            app_key = config.app_key
            auth_kind = config.auth_kind

        self._api_key = (api_key or "").strip()
        self._base_api_url = (base_api_url or "").strip()
        self._base_data_api_url = (base_data_api_url or "").strip()
        self._app_key = (app_key or "corva-api-client").strip() or "corva-api-client"
        self._auth_kind = auth_kind.strip() or "api_key"

        if not self._api_key:
            raise RuntimeError("Corva API key is required.")

        authorization_header = (
            f"Bearer {self._api_key}" if self._auth_kind == "jwt" else f"API {self._api_key}"
        )

        self.client = httpx.Client(
            headers={
                "Accept": "application/json",
                "Authorization": authorization_header,
            },
        )

        self.activities = ActivitiesClient(self)
        self.alerts = AlertsClient(self)
        self.api_key_management = ApiKeyClient(self)
        self.api_keys = ApiKeysClient(self)
        self.app_connection = AppConnectionClient(self)
        self.app_purchases = AppPurchasesClient(self)
        self.app_runs = AppRunsClient(self)
        self.app_schedule = AppScheduleClient(self)
        self.app_settings_templates = AppSettingsTemplatesClient(self)
        self.app_store_articles = AppStoreArticlesClient(self)
        self.apps = AppsClient(self)
        self.app_stream = AppStreamClient(self)
        self.assets = AssetsClient(self)
        self.audits = AuditsClient(self)
        self.column_mapper_templates = ColumnMapperTemplatesClient(self)
        self.companies = CompaniesClient(self)
        self.dashboard_app_annotations = DashboardAppAnnotationsClient(self)
        self.dashboards = DashboardsClient(self)
        self.data = DataClient(self)
        self.datasets = DatasetsClient(self)
        self.documents = DocumentsClient(self)
        self.edr_providers = EdrProvidersClient(self)
        self.feed = FeedClient(self)
        self.files = FilesClient(self)
        self.notifications = NotificationsClient(self)
        self.pads = PadsClient(self)
        self.partial_well_reruns = PartialWellRerunsClient(self)
        self.picklists = PicklistsClient(self)
        self.platform_subscriptions = PlatformSubscriptionsClient(self)
        self.product_subscriptions = ProductSubscriptionsClient(self)
        self.projects = ProjectsClient(self)
        self.provisioning_subscriptions = ProvisioningSubscriptionsClient(self)
        self.rigs = RigsClient(self)
        self.security = SecurityClient(self)
        self.tasks = TasksClient(self)
        self.users = UsersClient(self)
        self.well_view = WellViewClient(self)
        self.wells = WellsClient(self)
        self.workflows = WorkflowsClient(self)

    def close(self) -> None:
        self.client.close()

    def get(self, path: str, **kwargs) -> Any:
        return self._request("GET", path, **kwargs)

    def post(self, path: str, body: Any = None, **kwargs):
        return self._request("POST", path, body=body, **kwargs)

    def put(self, path: str, body: Any = None, **kwargs):
        return self._request("PUT", path, body=body, **kwargs)

    def patch(self, path: str, body: Any = None, **kwargs):
        return self._request("PATCH", path, body=body, **kwargs)

    def delete(self, path: str, body: Any = None, **kwargs):
        return self._request("DELETE", path, body=body, **kwargs)

    def request_response(
        self,
        method: str,
        path: str,
        body: Any = None,
        *,
        raise_for_status: bool = True,
        **kwargs,
    ) -> httpx.Response:
        url = self._build_url(path)
        request_kwargs = self._prepare_request_kwargs(method, body, kwargs)
        response = self.client.request(method, url, **request_kwargs)
        if raise_for_status:
            response.raise_for_status()
        return response

    def fetch_dataset(
        self,
        provider: str,
        dataset: str,
        query: dict[str, Any] | None = None,
        sort: dict[str, int] | None = None,
        limit: int = 100,
        skip: int | None = None,
        asset_id: int | None = None,
        fields: list[str] | None = None,
    ):
        return self.data.fetch(
            provider=provider,
            dataset=dataset,
            query=query,
            sort=sort,
            limit=limit,
            skip=skip,
            asset_id=asset_id,
            fields=fields,
        )

    def aggregate_dataset(
        self,
        provider: str,
        dataset: str,
        match: dict[str, Any] | None = None,
        group: dict[str, Any] | None = None,
        project: dict[str, Any] | None = None,
        sort: dict[str, int] | None = None,
        limit: int = 100,
        skip: int | None = None,
        asset_id: int | None = None,
    ):
        return self.data.aggregate(
            provider, dataset, match, group, project, sort, limit, skip, asset_id
        )

    def get_asset(
        self,
        asset_id: int,
        *,
        query_parameters: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        payload = self.assets.get(asset_id, query_parameters=query_parameters)
        if isinstance(payload, dict) and isinstance(payload.get("data"), dict):
            return cast(dict[str, Any], payload["data"])
        return payload if isinstance(payload, dict) else {}

    def paginate_dataset(
        self,
        *,
        provider: str = "corva",
        dataset: str,
        query: dict[str, Any] | None = None,
        sort: dict[str, int] | None = None,
        asset_id: int | None = None,
        fields: list[str] | None = None,
        page_size: int = 1000,
        max_records: int = 1_000_000,
    ) -> list[dict[str, Any]]:
        effective_page_size = max(1, page_size)
        all_records: list[dict[str, Any]] = []
        skip = 0

        while len(all_records) < max_records:
            page_records = self.fetch_dataset(
                provider=provider,
                dataset=dataset,
                query=query,
                sort=sort,
                limit=effective_page_size,
                skip=skip,
                asset_id=asset_id,
                fields=fields,
            )
            if not isinstance(page_records, list) or not page_records:
                break

            remaining = max_records - len(all_records)
            all_records.extend(page_records[:remaining])
            if len(page_records) < effective_page_size or len(all_records) >= max_records:
                break
            skip += effective_page_size

        return all_records

    def _request(self, method: str, path: str, body: Any = None, **kwargs):
        url = self._build_url(path)
        request_kwargs = self._prepare_request_kwargs(method, body, kwargs)
        try:
            response = self.client.request(method, url, **request_kwargs)
            response.raise_for_status()
        except httpx.HTTPError as error:
            self._print_request_debug(error, method, url, request_kwargs)
            return None
        except Exception as error:
            logger.debug("Unexpected error during request: %s", error, exc_info=error)
            return None

        if not response.content:
            return {}

        try:
            return response.json()
        except ValueError:
            return {"text": response.text}

    def _prepare_request_kwargs(
        self,
        method: str,
        body: Any,
        kwargs: dict[str, Any],
    ) -> dict[str, Any]:
        request_kwargs = dict(kwargs)
        if body is not None and method.upper() not in {"GET", "HEAD"}:
            request_kwargs["json"] = body
        return request_kwargs

    def _build_url(self, path: str) -> str:
        if path.lower().startswith("http"):
            return path

        normalized_path = path.lstrip("/")
        use_data_api = re.search(r"api/v\d+", normalized_path, re.IGNORECASE)
        selected_base_url = self._base_data_api_url if use_data_api else self._base_api_url

        if not selected_base_url:
            return f"/{normalized_path}" if path.startswith("/") else normalized_path

        if not normalized_path:
            return selected_base_url.rstrip("/")

        return f"{selected_base_url.rstrip('/')}/{normalized_path}"

    def _print_request_debug(
        self,
        error: httpx.HTTPError,
        method: str,
        url: str,
        request_kwargs: dict[str, Any],
    ) -> None:
        request = getattr(error, "request", None)
        response = getattr(error, "response", None)
        request_url = str(request.url) if request is not None else url

        debug_lines = [
            "Corva request failed:",
            f"  method: {method.upper()}",
            f"  url: {request_url}",
            f"  decoded_url: {unquote(request_url)}",
        ]

        if request_kwargs:
            debug_lines.append("  request_kwargs:")
            debug_lines.extend(
                f"    {line}" for line in pformat(request_kwargs, width=100).splitlines()
            )

        if response is not None:
            debug_lines.append(f"  status_code: {response.status_code}")
            try:
                debug_body = response.json()
            except ValueError:
                debug_body = response.text
            debug_lines.append("  response_body:")
            debug_lines.extend(
                f"    {line}" for line in pformat(debug_body, width=100).splitlines()
            )

        logger.debug("\n".join(debug_lines))
