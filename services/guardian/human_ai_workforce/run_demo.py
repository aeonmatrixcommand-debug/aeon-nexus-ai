from .signal.workforce_signal import analyze
from .skill.skill_engine import evaluate
from .agent.ai_collaboration import collaborate
from .optimization.workforce_optimizer import optimize
from .memory.workforce_memory import save


workforce = analyze(
    "ENTERPRISE_TEAM_SIGNAL"
)

skill = evaluate(
    "DIGITAL_OPERATION_SKILL"
)

agent = collaborate(
    "GUARDIAN_AI_AGENT"
)

optimization = optimize(
    [
        workforce,
        skill,
        agent
    ]
)

print(workforce)
print(skill)
print(agent)
print(optimization)
print(save(optimization))
