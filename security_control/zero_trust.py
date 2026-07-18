from datetime import datetime


class ZeroTrustEngine:

    def verify(self, identity, action):

        allowed = [
            "AI_AGENT",
            "HUMAN_OPERATOR",
            "SYSTEM_SERVICE"
        ]

        return {
            "identity": identity,
            "action": action,
            "verified": identity in allowed,
            "timestamp": datetime.utcnow().isoformat()
        }
