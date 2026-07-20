from .detection.risk_detector import detect
from .scoring.risk_score import calculate
from .governance.governance_check import validate
from .mitigation.mitigation_planner import plan
from .memory.risk_memory import save


risk = detect(
    "SUPPLY_CHAIN_DELAY"
)

score = calculate(
    risk
)

governance = validate(
    "AUTONOMOUS_RESPONSE"
)

mitigation = plan(
    score
)

print(risk)
print(score)
print(governance)
print(mitigation)
print(save(mitigation))
