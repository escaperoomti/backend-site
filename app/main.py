from fastapi import FastAPI

app = FastAPI()


@app.get("/health-status")
def read_health_status() -> dict:
    return {"status": "Service is up and running!"}
