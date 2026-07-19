from .engine.decision_engine import create
from .scoring.confidence_score import calculate as confidence
from .risk.risk_score import calculate as risk
from .value.value_score import calculate as value
from .record.decision_record import create as record
from .memory.decision_memory import save


context = {
    "operation": "INVENTORY_OPTIMIZATION",
    "warehouse": "AEON_DC"
}


decision = create(
    context
)


confidence_result = confidence(
    decision
)


risk_result = risk(
    decision
)


value_result = value(
    decision
)


executive_record = record(
    {
        "decision": decision,
        "confidence": confidence_result,
        "risk": risk_result,
        "value": value_result
    }
)


memory = save(
    executive_record
)


print(decision)
print(confidence_result)
print(risk_result)
print(value_result)
print(executive_record)
print(memory)
