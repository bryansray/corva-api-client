from __future__ import annotations

import os
from dataclasses import dataclass

ENVIRONMENT_BASE_URLS = {
    "production": "https://api.corva.ai",
    "qa": "https://api.qa.corva.ai",
    "staging": "https://api.staging.corva.ai",
}

ENVIRONMENT_DATA_BASE_URLS = {
    "production": "https://data.corva.ai",
    "qa": "https://data.qa.corva.ai",
    "staging": "https://data.staging.corva.ai",
}


@dataclass(frozen=True)
class CorvaConfig:
    base_api_url: str
    base_data_api_url: str
    api_key: str
    app_key: str = "corva-api-client"
    auth_kind: str = "api_key"

    @classmethod
    def from_env(cls) -> "CorvaConfig":
        environment = (os.environ.get("CORVA_ENVIRONMENT") or "production").strip()
        base_api_url = os.environ.get("CORVA_API_URL") or ENVIRONMENT_BASE_URLS.get(
            environment, ENVIRONMENT_BASE_URLS["production"]
        )
        base_data_api_url = os.environ.get("CORVA_DATA_API_URL") or ENVIRONMENT_DATA_BASE_URLS.get(
            environment, ENVIRONMENT_DATA_BASE_URLS["production"]
        )
        api_key = (os.environ.get("CORVA_API_KEY") or "").strip()
        auth_kind = (os.environ.get("CORVA_AUTH_KIND") or "api_key").strip() or "api_key"
        app_key = (
            os.environ.get("CORVA_APP_KEY") or "corva-api-client"
        ).strip() or "corva-api-client"

        if not api_key:
            raise RuntimeError("CORVA_API_KEY is not set.")

        return cls(
            base_api_url=base_api_url,
            base_data_api_url=base_data_api_url,
            api_key=api_key,
            app_key=app_key,
            auth_kind=auth_kind,
        )
