from services.guardian.digital_twin_live.state import TwinState


def update_twin(data):

    return TwinState(
        warehouse=data["warehouse"],
        inventory=data["inventory"],
        demand=data["demand"],
        risk=data["risk"]
    )
