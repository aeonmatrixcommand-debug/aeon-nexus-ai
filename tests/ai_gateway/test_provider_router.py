from unittest.mock import Mock

import pytest

from ai_gateway.circuit_breaker import CircuitBreaker
from ai_gateway.router import ProviderRouter


@pytest.mark.parametrize("method", ["generate", "chat"])
def test_legacy_aeonai_positional_breaker_single_provider(method):
    provider = type("Fake", (), {method: Mock(return_value="advisory")})()
    router = ProviderRouter()
    router.register("legacy", provider)
    breaker = CircuitBreaker()
    assert router.execute("prompt", breaker) == {"provider": "legacy", "result": "advisory"}
    getattr(provider, method).assert_called_once_with("prompt")
    assert breaker.allow("legacy")


def test_exact_selection_and_generate_only():
    router = ProviderRouter()
    first, second = Mock(), Mock()
    second.generate.return_value = "advisory"
    router.register("first", first)
    router.register("second", second)
    assert router.execute("prompt", provider_name="second", generate_only=True)["result"] == "advisory"
    second.generate.assert_called_once_with("prompt")
    second.chat.assert_not_called()
    assert first.mock_calls == []


@pytest.mark.parametrize("selection", [None, "missing"])
def test_ambiguous_or_unknown_selection_zero_calls(selection):
    router = ProviderRouter()
    first, second = Mock(), Mock()
    router.register("first", first)
    router.register("second", second)
    assert router.execute("prompt", provider_name=selection)["status"] == "FAILED"
    assert first.mock_calls == second.mock_calls == []


def test_provider_error_never_falls_back_and_opens_breaker():
    router = ProviderRouter()
    first, second = Mock(), Mock()
    first.generate.side_effect = RuntimeError("secret")
    router.register("first", first)
    router.register("second", second)
    breaker = CircuitBreaker(threshold=1)
    result = router.execute("prompt", breaker, provider_name="first", generate_only=True)
    assert result["status"] == "FAILED"
    assert "secret" not in str(result)
    assert not breaker.allow("first")
    assert second.mock_calls == []
    router.execute("prompt", breaker, provider_name="first", generate_only=True)
    first.generate.assert_called_once()


def test_duplicate_registration_rejected():
    router = ProviderRouter()
    router.register("fake", Mock())
    with pytest.raises(ValueError, match="duplicate_provider"):
        router.register("fake", Mock())
