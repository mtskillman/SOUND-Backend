import jwt
from os import getenv


def test_token(token):
    try:
        jwt.decode(token, getenv('global_secret'), algorithms=['HS256'])
        return 2
    except jwt.ExpiredSignatureError:
        return 0
    except jwt.exceptions.DecodeError:
        return 3
    else:
        return 4
