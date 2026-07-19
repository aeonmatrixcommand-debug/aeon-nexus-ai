def calculate_score(confidence, success, risk):
    return round(
        (confidence * 0.5)
        + (success * 0.4)
        - (risk * 0.1),
        3
    )
