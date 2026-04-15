from corva_sdk import CorvaClient, CorvaConfig


def test_public_imports() -> None:
    assert CorvaClient is not None
    assert CorvaConfig is not None


def test_client_requires_api_key() -> None:
    try:
        CorvaClient()
    except RuntimeError as exc:
        assert str(exc) == "Corva API key is required."
    else:
        raise AssertionError("Expected CorvaClient() to require an API key.")
