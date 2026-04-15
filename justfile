set shell := ["zsh", "-cu"]

default:
    @just --list

sync:
    uv sync

sync-all:
    uv sync --all-groups

lock:
    uv lock

format:
    uv run ruff format src tests

format-check:
    uv run ruff format --check src tests

lint:
    uv run ruff check src tests

lint-fix:
    uv run ruff check --fix src tests

typecheck:
    uv run ty check

test:
    uv run pytest

check:
    uv run ruff format --check src tests
    uv run ruff check src tests
    uv run ty check
    uv run pytest

build:
    rm -rf dist build
    uv build

check-dist: build
    uv run twine check dist/*

publish:
    uv publish

publish-to index-url:
    uv publish --publish-url {{ index-url }}
