from .partner.partner_engine import analyze
from .signal.external_signal import detect
from .relationship.ecosystem_graph import connect
from .insight.ecosystem_insight import generate
from .memory.ecosystem_memory import save


partner = analyze(
    "LOGISTICS_PARTNER"
)

signal = detect(
    "MARKET_TECHNOLOGY_CHANGE"
)

relation = connect(
    "AEON_MATRIX",
    "PARTNER_NETWORK"
)

insight = generate(
    [
        partner,
        signal,
        relation
    ]
)

print(partner)
print(signal)
print(relation)
print(insight)
print(save(insight))
