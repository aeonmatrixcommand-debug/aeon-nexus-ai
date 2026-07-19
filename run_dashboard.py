import uvicorn

uvicorn.run(
    "dashboard_api.app:app",
    host="0.0.0.0",
    port=8000
)
