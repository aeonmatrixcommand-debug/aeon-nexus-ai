
class AgentGovernanceEngine:

    def __init__(self):
        self.audit_log = []


    def check_permission(
        self,
        agent,
        capability
    ):

        return capability in agent.capabilities


    def calculate_risk(
        self,
        task
    ):

        if task.get("critical"):
            return 0.9

        return 0.2


    def authorize_execution(
        self,
        agent,
        task
    ):

        allowed = self.check_permission(
            agent,
            task["capability"]
        )

        risk = self.calculate_risk(
            task
        )

        if allowed and risk < 0.8:
            decision = "ALLOW"
        else:
            decision = "BLOCK"


        self.record_audit(
            agent.name,
            task,
            decision,
            risk
        )

        return decision


    def record_audit(
        self,
        agent_name,
        task,
        decision,
        risk
    ):

        self.audit_log.append(
            {
                "agent": agent_name,
                "task": task,
                "decision": decision,
                "risk": risk
            }
        )

