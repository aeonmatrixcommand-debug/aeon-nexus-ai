from customer_gateway.tenant_context import TenantContext


class CustomerAIGateway:

    def __init__(self):

        self.context = TenantContext()


    def request(self, customer_id, query):

        tenant = self.context.load(customer_id)

        return {
            "tenant": tenant,

            "request": {
                "query": query,
                "mode": "enterprise_ai"
            },

            "intelligence": {
                "status": "ready",
                "engine": "AEON_MATRIX_MOTHER_BRAIN"
            }
        }
