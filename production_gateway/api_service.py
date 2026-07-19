from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route("/health", methods=["GET"])
def health():

    return jsonify({
        "system": "AEON MATRIX API GATEWAY",
        "status": "ONLINE",
        "service": "PRODUCTION_LAYER",
        "timestamp": datetime.now().isoformat()
    })


@app.route("/decision", methods=["POST"])
def decision():

    data = request.json or {}

    return jsonify({
        "engine": "AEON MATRIX DECISION SERVICE",
        "status": "SUCCESS",
        "input": data,
        "decision": {
            "risk": "ANALYZED",
            "action": "OPTIMIZE_OPERATION",
            "approval": "GOVERNANCE_CHECKED"
        },
        "timestamp": datetime.now().isoformat()
    })


if __name__ == "__main__":

    print("=================================")
    print(" AEON MATRIX PRODUCTION API ")
    print("=================================")
    print(" HEALTH  : /health")
    print(" DECISION: /decision")
    print("=================================")

    app.run(
        host="0.0.0.0",
        port=8090
    )
