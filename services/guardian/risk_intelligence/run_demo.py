from .detection.risk_detector import detect
from .scoring.risk_score import calculate
from .governance.governance_check import validate
from .mitigation.mitigation_planner import plan
from .memory.risk_memory import save
from services.guardian.risk_intelligence.detection.risk_detector import detect
from services.guardian.risk_intelligence.scoring.risk_score import calculate
from services.guardian.risk_intelligence.governance.governance_check import validate
from services.guardian.risk_intelligence.mitigation.mitigation_planner import plan
from services.guardian.risk_intelligence.memory.risk_memory import save


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
