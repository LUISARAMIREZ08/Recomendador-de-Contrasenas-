# These lines of code are importing necessary modules and classes for creating a custom error handler
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi import Request, FastAPI, Response
from fastapi.responses import JSONResponse

# The `ErrorHandler` class is a middleware that catches exceptions and returns a JSON response with
# the error message and a status code of 500.
class ErrorHandler(BaseHTTPMiddleware):

    def __init__(self, app: FastAPI):
        super().__init__(app)
    
    async def dispatch(self, request: Request, call_next) -> Response | JSONResponse:
        try:
            return await call_next(request)
        except Exception as e:
            return JSONResponse(status_code=500,content ={'error': str(e)})