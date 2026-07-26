from ai_gateway.lifecycle.agent import AutonomousAgent


class LifecycleManager:


    def __init__(self):

        self.agents = {}



    def create(self, agent_id):

        agent = AutonomousAgent(agent_id)

        self.agents[agent_id] = agent

        return agent



    def start(self, agent_id):

        agent = self.agents[agent_id]

        agent.transition("READY")

        return agent.info()



    def run(self, agent_id):

        agent = self.agents[agent_id]

        agent.transition("RUNNING")

        return agent.info()
