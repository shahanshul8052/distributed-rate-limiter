from fastapi import FastAPI, Header
from app.middleware import RateLimitMiddleware

app = FastAPI(title="ShieldAPI")

# add the rate limit middleware to the app
app.add_middleware(RateLimitMiddleware)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/request")
# x_api_key is required header for this endpoint - tells fastapi that endpoint requires header so ... means it's required
async def protected_request(x_api_key: str = Header(...)):
    return {"message": "Request successful"}