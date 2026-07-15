class CommunicationProtocol:
    """
    Standard communication between AI agents.
    """

    def send(self, sender, receiver, message):

        return {
            "from": sender,
            "to": receiver,
            "message": message,
            "status": "delivered"
        }
