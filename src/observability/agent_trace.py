from datetime import datetime, timezone


class AgentTrace:

    """
    Track AI agent execution flow.
    """


    def __init__(self):

        self.traces = []


    def capture(self, agent, action):

        trace = {

            "agent": agent,

            "action": action,

            "timestamp":
            datetime.now(
                timezone.utc
            ).isoformat(),

            "status":"completed"

        }


        self.traces.append(trace)

        return trace



    def history(self):

        return self.traces
