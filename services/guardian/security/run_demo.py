from .identity.device_identity import verify_device
from .identity.user_identity import verify_user
from .authentication.token_service import create_token
from .authorization.rbac import check_permission
from .gateway.api_guard import protect
from .audit.security_logger import log
from .threat.anomaly_detector import detect
from services.guardian.security.identity.device_identity import verify_device
from services.guardian.security.identity.user_identity import verify_user
from services.guardian.security.authentication.token_service import create_token
from services.guardian.security.authorization.rbac import check_permission
from services.guardian.security.gateway.api_guard import protect
from services.guardian.security.audit.security_logger import log
from services.guardian.security.threat.anomaly_detector import detect


device = verify_device("WMS-TAB-001")

user = verify_user("operator-001")

token = create_token(user)

permission = check_permission(
    "warehouse_operator",
    "inventory_scan"
)

gateway = protect(
    "inventory_scan"
)

security = detect(
    gateway
)

print(device)
print(user)
print(token)
print(permission)
print(gateway)
print(security)
print(log("SECURITY_AUTH_FLOW"))
