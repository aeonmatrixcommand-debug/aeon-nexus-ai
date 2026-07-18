from security_control.zero_trust import ZeroTrustEngine
from governance_plane.control import GovernanceControl


security = ZeroTrustEngine()
governance = GovernanceControl()


print("=== AEON MATRIX SECURITY CONTROL PLANE ===")

print("\nZERO TRUST VERIFY")
print(
    security.verify(
        "AI_AGENT",
        "EXECUTE_INVENTORY_RECOVERY"
    )
)

print("\nAI GOVERNANCE")
print(
    governance.evaluate()
)
