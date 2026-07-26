from ai_gateway.federation.agent_message import AgentMessage


class AgentCollaboration:


    def __init__(self):

        self.messages = []



    def send(
        self,
        sender,
        receiver,
        payload
    ):

        message = AgentMessage(
            sender,
            receiver,
            "TASK_REQUEST",
            payload
        )


        self.messages.append(
            message.to_dict()
        )


        return message.to_dict()



    def history(self):

        return self.messages
