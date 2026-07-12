from services.guardian.ai_gateway.runtime import AIGateway

def test_gateway():
    assert AIGateway().process({"task":"forecast"})["status"] == "accepted"
