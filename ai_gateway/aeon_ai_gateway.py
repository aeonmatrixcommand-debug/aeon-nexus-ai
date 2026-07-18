from ai_gateway.gemini_provider import GeminiProvider


class AEONAI:

    def __init__(self):
        self.provider = GeminiProvider()


    def analyze(self, event):

        prompt = f"""
You are AEON MATRIX Mother Brain AI.

System:
- Autonomous Logistics Operating System
- WMS Intelligence
- Digital Twin
- Command Center
- Predictive Operations
- AI Governance

Analyze operational event:

{event}

Return:
1. Situation
2. Risk
3. Prediction
4. Recommended Action
"""

        return self.provider.generate(prompt)
