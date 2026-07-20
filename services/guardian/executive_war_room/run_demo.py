from .situation.situation_engine import analyze
from .fusion.intelligence_fusion import fuse
from .decision.decision_brief import generate
from .command.command_board import display
from .memory.executive_memory import save


situation = analyze(
    "ENTERPRISE_OPERATION_STATUS"
)

fusion = fuse(
    [
        "WORLD_SIGNAL",
        "DIGITAL_TWIN",
        "ECONOMIC_INTELLIGENCE"
    ]
)

decision = generate(
    fusion
)

board = display(
    decision
)

print(situation)
print(fusion)
print(decision)
print(board)
print(save(board))
