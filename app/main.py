from fastapi import FastAPI

app = FastAPI()


@app.get("/health-status")
def read_health_status() -> dict:
    return {"status": "Service is up and running!"}


def start() -> None:
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
