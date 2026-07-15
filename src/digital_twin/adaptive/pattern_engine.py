class PatternEngine:
    """
    Detect recurring patterns from digital twin history.
    """

    def detect(self, events):

        patterns = []

        if "cold_chain_breach" in events:
            patterns.append({
                "pattern": "cold_chain_risk",
                "confidence": 0.82
            })

        if "capacity_shortage" in events:
            patterns.append({
                "pattern": "capacity_pressure",
                "confidence": 0.76
            })

        return {
            "patterns": patterns,
            "pattern_count": len(patterns)
        }
