

def update_twin_learning(event):

    return {

        "twin_update":
            "APPLIED",

        "source":
            event["decision"]

    }
