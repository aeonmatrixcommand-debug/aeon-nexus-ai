class WhatIfEngine:
    """
    Compare possible futures.
    """

    def compare(self, results):

        best = None
        score = -999


        for result in results:

            current = (
                result["risk_change"] * -1
                -
                result["cost"] / 100000
            )


            if current > score:

                score = current
                best = result


        return {
            "recommended_future": best,
            "confidence": 0.95
        }
