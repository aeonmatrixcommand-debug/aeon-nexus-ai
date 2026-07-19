
from services.guardian.runtime.learning_bridge import (
    process_outcome
)


def test_learning():

    result=process_outcome(
        "trace1",
        "ALLOCATE",
        "SUCCESS"
    )


    assert result["learning"]["learning_status"]=="ADAPTIVE"
