from fastapi import FastAPI

app = FastAPI(title="ShieldAPI")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/request")
async def protected_request():
    return {"message": "Request successful"}