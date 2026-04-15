from __future__ import annotations


def normalize_data_api_target(provider: str, dataset: str) -> tuple[str, str]:
    normalized_provider = provider.strip()
    normalized_dataset = dataset.strip()

    if not normalized_provider:
        raise ValueError("Provider is required.")
    if not normalized_dataset:
        raise ValueError("Dataset is required.")

    qualified_provider, separator, qualified_dataset = normalized_dataset.partition("#")
    if not separator:
        return normalized_provider, normalized_dataset

    resolved_provider = qualified_provider.strip() or normalized_provider
    resolved_dataset = qualified_dataset.strip()
    if not resolved_dataset:
        raise ValueError("Dataset is required.")

    return resolved_provider, resolved_dataset
