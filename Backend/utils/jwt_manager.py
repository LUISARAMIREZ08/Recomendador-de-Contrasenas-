#The code defines functions to create and validate JWT tokens using a secret key.
from jwt import decode, encode
pwd = '1234567890'

def create_token(data, secret=pwd): #data is the payload to be encoded
    return encode(payload=data, key=secret, algorithm='HS256') #HS256 is the algorithm used to encode the token

def validate_token(token): #token is the payload to be decoded
    return decode(token, pwd, algorithms=['HS256']) #HS256 is the algorithm used to decode the token