import pytest


def test_datastore_store_symbol_exists():
    """
    Distributed execution authority requires a dedicated
    persistent store adapter.

    RED until DatastoreAuthorizationConsumptionStore exists.
    """
    from services.guardian.execution import authorization_consumption_store

    assert hasattr(
        authorization_consumption_store,
        "DatastoreAuthorizationConsumptionStore",
    )


def test_datastore_store_requires_client():
    """
    Construction must use an injected client.

    This keeps infrastructure ownership outside the domain
    object and makes the adapter independently testable.
    """
    from services.guardian.execution.authorization_consumption_store import (
        DatastoreAuthorizationConsumptionStore,
    )

    with pytest.raises(ValueError, match="DATASTORE_CLIENT_REQUIRED"):
        DatastoreAuthorizationConsumptionStore(client=None)


def test_datastore_store_validates_authorization_id():
    """
    The distributed adapter must preserve the existing
    authorization-id validation contract.
    """
    from services.guardian.execution.authorization_consumption_store import (
        DatastoreAuthorizationConsumptionStore,
    )

    class Client:
        pass

    store = DatastoreAuthorizationConsumptionStore(
        client=Client()
    )

    with pytest.raises(
        ValueError,
        match="AUTHORIZATION_ID_REQUIRED",
    ):
        store.try_consume("")


def test_datastore_kind_is_explicit():
    """
    Persistence namespace must be deterministic and explicit.
    """
    from services.guardian.execution.authorization_consumption_store import (
        DatastoreAuthorizationConsumptionStore,
    )

    assert (
        DatastoreAuthorizationConsumptionStore.KIND
        == "GuardianAuthorizationConsumption"
    )


class FakeEntity(dict):
    def __init__(self, key):
        super().__init__()
        self.key = key


class FakeTransaction:
    def __init__(self, client):
        self.client = client

    def __enter__(self):
        self.client.transaction_entries += 1
        self.client.active_transaction = self
        return self

    def __exit__(self, exc_type, exc, tb):
        self.client.active_transaction = None
        return False

    def put(self, entity):
        self.client.transaction_puts += 1
        self.client.entities[entity.key] = entity


class FakeDatastoreClient:
    def __init__(self):
        self.entities = {}
        self.transaction_entries = 0
        self.transaction_gets = 0
        self.transaction_puts = 0
        self.active_transaction = None

    def key(self, kind, authorization_id):
        return (kind, authorization_id)

    def transaction(self):
        return FakeTransaction(self)

    def get(self, key, transaction=None):
        if transaction is not None:
            assert transaction is self.active_transaction
            self.transaction_gets += 1

        return self.entities.get(key)


def test_try_consume_uses_transactional_read_and_write(monkeypatch):
    from services.guardian.execution import (
        authorization_consumption_store as module,
    )

    monkeypatch.setattr(
        module.datastore,
        "Entity",
        FakeEntity,
    )

    client = FakeDatastoreClient()

    store = module.DatastoreAuthorizationConsumptionStore(
        client=client
    )

    assert store.try_consume("distributed-auth-001") is True

    assert client.transaction_entries == 1
    assert client.transaction_gets == 1
    assert client.transaction_puts == 1


def test_second_claim_returns_false_without_second_write(monkeypatch):
    from services.guardian.execution import (
        authorization_consumption_store as module,
    )

    monkeypatch.setattr(
        module.datastore,
        "Entity",
        FakeEntity,
    )

    client = FakeDatastoreClient()

    store_a = module.DatastoreAuthorizationConsumptionStore(
        client=client
    )
    store_b = module.DatastoreAuthorizationConsumptionStore(
        client=client
    )

    assert store_a.try_consume("distributed-auth-002") is True
    assert store_b.try_consume("distributed-auth-002") is False

    assert client.transaction_entries == 2
    assert client.transaction_gets == 2
    assert client.transaction_puts == 1


def test_authorization_id_is_used_as_entity_key(monkeypatch):
    from services.guardian.execution import (
        authorization_consumption_store as module,
    )

    monkeypatch.setattr(
        module.datastore,
        "Entity",
        FakeEntity,
    )

    client = FakeDatastoreClient()

    store = module.DatastoreAuthorizationConsumptionStore(
        client=client
    )

    authorization_id = "distributed-auth-key-001"

    assert store.try_consume(authorization_id) is True

    expected_key = (
        store.KIND,
        authorization_id,
    )

    assert expected_key in client.entities


def test_try_consume_retries_aborted_transaction(monkeypatch):
    """
    A Datastore contention abort must be retried.

    After another transaction wins during contention,
    the retry must observe the persisted marker and
    return False rather than leaking Aborted.
    """
    from google.api_core.exceptions import Aborted

    from services.guardian.execution import (
        authorization_consumption_store as module,
    )

    monkeypatch.setattr(
        module.datastore,
        "Entity",
        FakeEntity,
    )

    class ContendedClient(FakeDatastoreClient):
        def __init__(self):
            super().__init__()
            self.get_attempts = 0

        def get(self, key, transaction=None):
            self.get_attempts += 1

            if self.get_attempts == 1:
                # Simulate another distributed claimant
                # winning while our transaction is aborted.
                entity = FakeEntity(key)
                entity["authorization_id"] = key[1]
                entity["consumed"] = True
                self.entities[key] = entity

                raise Aborted(
                    "simulated cross-transaction contention"
                )

            return self.entities.get(key)

    client = ContendedClient()

    store = module.DatastoreAuthorizationConsumptionStore(
        client=client
    )

    result = store.try_consume(
        "contention-retry-auth-001"
    )

    assert result is False
    assert client.get_attempts == 2


def test_try_consume_has_bounded_aborted_retry(monkeypatch):
    """
    Persistent contention must not cause an infinite retry loop.
    """
    from google.api_core.exceptions import Aborted

    from services.guardian.execution import (
        authorization_consumption_store as module,
    )

    monkeypatch.setattr(
        module.datastore,
        "Entity",
        FakeEntity,
    )

    class AlwaysAbortedClient(FakeDatastoreClient):
        def __init__(self):
            super().__init__()
            self.get_attempts = 0

        def get(self, key, transaction=None):
            self.get_attempts += 1
            raise Aborted(
                "simulated persistent contention"
            )

    client = AlwaysAbortedClient()

    store = module.DatastoreAuthorizationConsumptionStore(
        client=client
    )

    with pytest.raises(Aborted):
        store.try_consume(
            "persistent-contention-auth-001"
        )

    assert client.get_attempts > 1
    assert client.get_attempts <= 5
