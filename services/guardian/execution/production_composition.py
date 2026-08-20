"""Production composition for Guardian execution authority.

Production execution authority consumption must use persistent,
transactional storage. Failure to construct the Datastore client is
intentionally propagated: production must never silently fall back to
process-local in-memory consumption state.
"""

from google.cloud import datastore

from services.guardian.execution.authorization_consumption_store import (
    DatastoreAuthorizationConsumptionStore,
)
from services.guardian.execution.execution_layer import (
    AutonomousExecutionLayer,
)


def build_authorization_consumption_store():
    """Build the production authorization-consumption store."""

    client = datastore.Client()

    return DatastoreAuthorizationConsumptionStore(
        client=client,
    )


def build_execution_layer():
    """Build the production Guardian execution layer."""

    store = build_authorization_consumption_store()

    return AutonomousExecutionLayer(
        authorization_consumption=store,
    )
