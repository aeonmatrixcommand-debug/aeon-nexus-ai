from flask import Flask, jsonify
from datetime import datetime
import random

app = Flask(__name__)


@app.route("/dashboard", methods=["GET"])
def dashboard():

    return jsonify({
        "system": "AEON MATRIX REAL-TIME COMMAND CENTER",
        "status": "ONLINE",

        "telemetry": {
            "warehouse": "ACTIVE",
            "fleet": "ACTIVE",
            "orders": "MONITORING",
            "data_quality": "HIGH"
        },

        "kpi": {
            "OTIF": "96.8%",
            "SLA": "98.1%",
            "Inventory_Accuracy": "99.2%",
            "Productivity": "94.5%",
            "Risk_Score": "LOW",
            "Logistics_Flow_Index": round(random.uniform(90,93),1)
        },

        "ai": {
            "mother_brain": "ONLINE",
            "copilot": "ONLINE",
            "decision_engine": "READY"
        },

        "timestamp": datetime.now().isoformat()
    })


if __name__ == "__main__":

    print("=================================")
    print(" AEON MATRIX COMMAND DASHBOARD ")
    print("=================================")
    print(" Dashboard : http://127.0.0.1:8100/dashboard")
    print("=================================")

    app.run(
        host="0.0.0.0",
        port=8100
    )
