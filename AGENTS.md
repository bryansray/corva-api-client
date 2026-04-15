# AGENTS.md

## Purpose

This repository contains `corva-sdk`, a Python package for working with Corva HTTP
and data APIs. The package is intended to be consumed by other internal tools,
jobs, and applications, so changes should favor a stable public API, predictable
packaging behavior, and clear release hygiene.

## Core Expectations

- Use `uv` for dependency management, virtual environment setup, and Python tool
  execution.
- Use `just` recipes when they exist instead of inventing one-off commands.
- Keep the package publishable as a normal Python distribution.
- Preserve the `src/` layout and avoid ad hoc path hacks.
- Treat this as a reusable library, not as an app or script repository.

## Repository Layout

- `src/corva_sdk/`
  - package source
  - `client.py` contains the main `CorvaClient`
  - `config.py` contains environment-driven configuration
  - `resources/` contains resource-specific clients
  - `schemas/` contains packaged JSON schema assets
- `tests/`
  - package smoke tests and future unit tests
- `pyproject.toml`
  - packaging metadata, dependencies, and tool configuration
- `justfile`
  - preferred entry points for common development tasks

## Development Workflow

Set up the environment with:

```bash
uv sync
```

Preferred commands:

```bash
just format
just lint
just typecheck
just test
just check
just build
just check-dist
```

Equivalent direct commands:

```bash
uv run ruff format src tests
uv run ruff check src tests
uv run mypy
uv run pytest
uv build
uv run twine check dist/*
```

## Quality Gates

Before considering work complete, run:

```bash
just check
```

When packaging or release-related files change, also run:

```bash
just check-dist
```

Expectations:

- `ruff format --check` passes
- `ruff check` passes
- `mypy` passes
- `pytest` passes
- distribution metadata validates cleanly

## Packaging Notes

- Python version support starts at 3.11.
- Package metadata lives in `pyproject.toml`.
- Build artifacts should be created with `uv build`.
- Distribution validation should use `twine check` via `just check-dist`.
- `schemas/*.json` under `src/corva_sdk/` are package data and must remain included.
- Keep README content aligned with the actual public API and development workflow.

## Code Guidelines

- Prefer explicit types on public functions and methods.
- Keep resource client behavior thin and predictable.
- When the client returns loosely typed JSON, narrow return values deliberately.
- Avoid introducing unnecessary runtime dependencies.
- If a dependency exists for a concrete serialization or API compatibility reason,
  document or preserve that rationale.
- Preserve compatibility with `uv`, `ruff`, `mypy`, and `pytest` configuration
  already defined in `pyproject.toml`.

## Testing Guidance

- Add tests for new public behavior.
- Prefer focused unit tests over broad integration assumptions.
- For bug fixes, add a regression test when practical.
- Keep tests runnable through `uv run pytest`.

## Commit Conventions

All commits should follow Conventional Commits.

Use forms such as:

- `feat: add dataset pagination helper`
- `fix: narrow data client response typing`
- `docs: rewrite sdk README`
- `refactor: simplify config parsing`
- `test: add smoke coverage for package imports`
- `chore: update dev tooling`

If a change has breaking API impact, use the Conventional Commits breaking-change
signal, for example:

- `feat!: rename CorvaConfig field`
- include a `BREAKING CHANGE:` footer in the commit message body when needed

## Change Discipline

- Do not remove or loosen quality checks just to make CI pass.
- Do not change packaging behavior casually; other repositories may consume this SDK.
- Keep documentation, tooling, and package metadata in sync with code changes.
- If adding new repo workflows, prefer adding them to `justfile` and documenting
  them in `README.md` when they are user-facing.
