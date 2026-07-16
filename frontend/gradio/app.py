import gradio as gr
import requests
import json
from datetime import datetime


API = "http://127.0.0.1:8000"


def api_get(path):
    try:
        r = requests.get(f"{API}{path}", timeout=5)
        return r.json()
    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }


def system_health():
    return json.dumps(
        api_get("/health"),
        indent=2,
        ensure_ascii=False
    )


def runtime_status():
    return json.dumps(
        api_get("/runtime"),
        indent=2,
        ensure_ascii=False
    )


def agents_status():
    return json.dumps(
        api_get("/agents"),
        indent=2,
        ensure_ascii=False
    )


def metrics_status():
    return json.dumps(
        api_get("/metrics"),
        indent=2,
        ensure_ascii=False
    )


with gr.Blocks(
    title="AEON MATRIX Enterprise AI Command Center"
) as app:

    gr.Markdown(
        """
# 🌍 AEON MATRIX
## Enterprise AI Command Center

Sense → Think → Decide → Act → Learn
"""
    )

    with gr.Tab("🧠 System Health"):
        health_btn = gr.Button("Refresh Health")
        health_out = gr.Code(language="json")
        health_btn.click(
            system_health,
            outputs=health_out
        )

    with gr.Tab("🚀 Runtime"):
        runtime_btn = gr.Button("Refresh Runtime")
        runtime_out = gr.Code(language="json")
        runtime_btn.click(
            runtime_status,
            outputs=runtime_out
        )

    with gr.Tab("🤖 Agents"):
        agents_btn = gr.Button("Refresh Agents")
        agents_out = gr.Code(language="json")
        agents_btn.click(
            agents_status,
            outputs=agents_out
        )

    with gr.Tab("📊 Metrics"):
        metrics_btn = gr.Button("Refresh Metrics")
        metrics_out = gr.Code(language="json")
        metrics_btn.click(
            metrics_status,
            outputs=metrics_out
        )

    gr.Markdown(
        f"""
---
AEON MATRIX Runtime Connected  
Last Build: {datetime.now()}
"""
    )


app.launch(
    server_name="0.0.0.0",
    server_port=7861
)
