# middleware code

from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from app.limiter import FixedWindowRateLimiter
from fastapi.responses import JSONResponse

#independent per api key so independent counter storage

rate_limiter = FixedWindowRateLimiter(limit=5, window_size=60)  # example: 5 requests per 60 seconds
class RateLimitMiddleware(BaseHTTPMiddleware):
    # this middleware will be added to the FastAPI app to check rate limits before processing requests
    # dispatch is key method in starlette and fastapi
    async def dispatch(self, request: Request, call_next):
        # skip health
        if request.url.path.startswith(("/health", "/docs", "/openapi", "/redoc")):
            return await call_next(request)
        
        # extract api key from headers
        api_key = request.headers.get("X-API-Key")
        
        # used http exception previously but printed stack trace - converting to json
        if not api_key:
            return JSONResponse(status_code=401, content={"detail": "API key missing"})
        if not rate_limiter.is_allowed(api_key):
            return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})
        # call_next processes request and returns response object
        response = await call_next(request)
        return response

# sits between client and endpoint and intercepts requests before hitting the route itself