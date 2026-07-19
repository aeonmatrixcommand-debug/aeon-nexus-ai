def predict(simulation):

    return {
        "prediction":
            simulation["recommendation"],
        "confidence":
            round(1 - simulation["risk"], 2)
    }
