
RULES = [

"NO_SCAN_NO_MOVE",
"WEIGHT_VERIFICATION_REQUIRED",
"ROUTE_CHANGE_REQUIRES_APPROVAL",
"AI_ACTION_REQUIRES_CONFIDENCE"

]


def validate(confidence):

    if confidence < 0.8:

        return "BLOCKED"


    return "APPROVED"
