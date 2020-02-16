from flask import Response
from json import dumps

def make_response(content, status):
    '''
    :param content: should be a dictionary
    :param status: integer value
    :return: Resonse object
    '''
    ret = dumps(content)
    resp = Response(response=ret, status=status, mimetype="application/json")
    return resp
