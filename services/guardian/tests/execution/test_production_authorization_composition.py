import pytest

from services.guardian.execution.authorization_consumption_store import (
    DatastoreAuthorizationConsumptionStore,
)


def test_production_composition_uses_datastore_store(monkeypatch):
    from services.guardian.execution import production_composition

    sentinel_client = object()

    monkeypatch.setattr(
        production_composition.datastore,
        "Client",
        lambda: sentinel_client,
    )

    store = (
        production_composition
        .build_authorization_consumption_store()
    )

    assert isinstance(
        store,
        DatastoreAuthorizationConsumptionStore,
    )
    assert store._client is sentinel_client


def test_production_execution_layer_receives_datastore_store(
    monkeypatch,
):
    from services.guardian.execution import production_composition

    sentinel_client = object()

    monkeypatch.setattr(
        production_composition.datastore,
        "Client",
        lambda: sentinel_client,
    )

    engine = production_composition.build_execution_layer()

    assert isinstance(
        engine.authorization_consumption,
        DatastoreAuthorizationConsumptionStore,
    )
    assert (
        engine.authorization_consumption._client
        is sentinel_client
    )


def test_production_composition_does_not_fallback_to_memory(
    monkeypatch,
):
    from services.guardian.execution import production_composition

    def fail_client():
        raise RuntimeError("DATASTORE_UNAVAILABLE")

    monkeypatch.setattr(
        production_composition.datastore,
        "Client",
        fail_client,
    )

    with pytest.raises(
        RuntimeError,
        match="DATASTORE_UNAVAILABLE",
    ):
        production_composition.build_execution_layer()
