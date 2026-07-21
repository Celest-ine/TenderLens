from fastapi import FastAPI

app = FastAPI(
    title="TenderLens API",
    description="AI-powered Tender document analysis API",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to TenderLens API"
        }

@app.post("/greet")
def greet_user(name: str):
    return {
        "message": f"Hello, {name}"
    }