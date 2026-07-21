class TMSIntelligence:

    def analyze_route(self, route):
        distance = route.get("distance", 0)

        return {
            "route_status": "optimized" if distance > 0 else "unknown",
            "distance": distance
        }
