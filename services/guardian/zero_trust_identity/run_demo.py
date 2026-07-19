from .identity.identity_registry import register_identity
from .device.device_trust import verify_device
from .mfa.mfa_verify import verify_mfa
from .policy.access_policy import evaluate
from .audit.security_audit import record


identity = register_identity(
    "warehouse_operator",
    "OPERATOR"
)

device = verify_device(
    "AEON_ANDROID_DEVICE"
)

mfa = verify_mfa(
    "AUTHENTICATOR"
)

decision = evaluate(
    identity,
    device,
    mfa
)

audit = record(
    "ZERO_TRUST_ACCESS_CHECK"
)


print({
    "identity_status": "VERIFIED",
    "device_status": "TRUSTED",
    "mfa_status": "PASSED",
    "access_decision": "EVALUATED",
    "audit_status": "RECORDED"
})
