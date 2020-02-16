import datetime
import jwt
from os import getenv


def encode_auth_token(resource_id):
    """
    Generates the Auth Token
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
            'sub': resource_id
        }
        to_return = jwt.encode(
            payload,
            getenv('global_secret'),
            algorithm='HS256'
        )
        return to_return.decode('utf-8')
    except Exception as e:
        return e