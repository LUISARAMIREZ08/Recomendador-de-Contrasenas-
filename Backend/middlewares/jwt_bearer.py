# The code is importing necessary modules and functions for implementing JWT (JSON Web Token)
# authentication in a FastAPI application.
from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException
from utils.jwt_manager import validate_token

# The JWTBearer class extends the HTTPBearer class and validates the token credentials, 
#raising an exception if the user is not the admin.
class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@mail.com":
            raise HTTPException(status_code=401, detail="Invalid User")
            