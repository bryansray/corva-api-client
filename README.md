# corva-api-client

Python SDK for working with Corva HTTP and data APIs.

This repository packages shared client logic for Corva integrations, scripts, jobs,
and internal applications. It provides a configured HTTP client, environment-driven
settings, dataset helpers, and generated resource clients for a broad set of Corva
API endpoints.

## What it provides

- `CorvaConfig` for environment-based configuration
- `CorvaClient` for authenticated HTTP access
- resource clients exposed on `CorvaClient` such as `assets`, `apps`, `datasets`,
  `projects`, `wells`, and `data`
- helpers for dataset fetch, aggregate, and pagination workflows
- request-building utilities for data API queries

## Installation

For local development in this repository:

```bash
uv sync
```

To use this package from another local repository during development:

```bash
uv add --editable /path/to/corva-api-client
```

Published distribution name:

```bash
uv add corva-api-client
```

Python import path:

```python
import corva_api_client
```

## Quick Start

```python
from corva_api_client import CorvaClient, CorvaConfig

config = CorvaConfig.from_env()
client = CorvaClient(config)

asset = client.get_asset(68833811)

records = client.paginate_dataset(
    dataset="wits.summary-1ft",
    asset_id=68833811,
    query={"timestamp": {"$gte": 1776164400, "$lt": 1776250800}},
    fields=["timestamp", "asset_id"],
    page_size=1000,
)

client.close()
```

Direct resource access is also available:

```python
from corva_api_client import CorvaClient, CorvaConfig

client = CorvaClient(CorvaConfig.from_env())
companies = client.companies.list()
apps = client.apps.search(type="drilling")
client.close()
```

## Configuration

`CorvaConfig.from_env()` reads these environment variables:

- `CORVA_API_KEY`
- `CORVA_ENVIRONMENT`
  - `production`, `qa`, or `staging`
- `CORVA_AUTH_KIND`
  - `api_key` or `jwt`
- `CORVA_API_URL`
  - optional override for the main API base URL
- `CORVA_DATA_API_URL`
  - optional override for the data API base URL
- `CORVA_APP_KEY`
  - optional override, defaults to `corva-api-client`

## Development

Common repository tasks are exposed through `just` and run through `uv`:

```bash
just
just format
just lint
just typecheck
just test
just check
just build
just check-dist
```

Equivalent direct commands are:

```bash
uv run ruff format src tests
uv run ruff check src tests
uv run ty check
uv run pytest
uv build
```

## Notes

- The package requires Python 3.11 or newer.
- `CorvaClient` raises `RuntimeError` if no API key is configured.
- The data resource serializer supports BSON-native values such as `ObjectId`,
  `Decimal128`, and `Int64` when creating or replacing dataset records.
