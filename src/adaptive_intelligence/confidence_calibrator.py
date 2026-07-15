class ConfidenceCalibrator:


    def calibrate(self, decision, outcome):


        if outcome == "success":

            return {

                "previous_confidence":0.85,

                "new_confidence":0.92,

                "adjustment":"increase"

            }


        return {

            "previous_confidence":0.85,

            "new_confidence":0.60,

            "adjustment":"decrease"

        }
