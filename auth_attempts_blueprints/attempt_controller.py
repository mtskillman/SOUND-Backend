from flask import Blueprint, request
from otp_handling import verify, test_func
from response_handling import make_response
from database_integration import get_the_private_key
from database_connection import initialize
from os import getenv
from token_handling import encode_auth_token, test_token

db_connection = initialize(getenv('connection_url'))
attempt_blueprint = Blueprint('attempt_api', __name__)


@attempt_blueprint.route('/sender-attempt', methods=['POST'])
def sender_attempt():
    body = request.json
    code_to_eval = body.get('code')
    resource_id = body.get('resource-id')
    if not code_to_eval:
        return make_response(
            {
                'result': 'missing-code-param'
            }, 400
        )
    if not resource_id:
        return make_response(
            {
                'result': 'missing-resource-id-param'
            }, 400
        )

    secret_key = get_the_private_key(db_connection, resource_id)
    print(type(code_to_eval))
    print(code_to_eval)
    if not secret_key:
        return make_response({
            'result': "invalid-resource-id"
        }, 400)
    print(test_func(secret_key))
    print(type(test_func(secret_key)))

    if verify(secret_key, code_to_eval):
        token = encode_auth_token(resource_id)
        db_connection.store_token_in_db(resource_id, token)
        return make_response(
            {'access-token': token}, 200
        )
    else:
        return make_response(
            {'result': "failed-login",
             'resource-id': resource_id}, 400
        )


@attempt_blueprint.route('/receiver-attempt', methods=['POST'])
def receiver_attempt():
    body = request.json
    token = body.get('token')

    if not token:
        return make_response(
            {
                'result': 'missing-token-param'
            }, 400
        )
    if token not in db_connection.return_all_tokens():
        return make_response(
            {
                'result': 'token-not-issued-by-this-server'
            }, 400
        )
    if test_token(token) == 2:
        return make_response(
            {'result': 'valid-token'}, 200
        )
    elif test_token(token) == 0:
        return make_response(
            {'result': 'expired-token'}, 400
        )
    elif test_token(token) == 3:
        return make_response(
            {'result': 'token-not-valid-formatting'}, 400
        )
    else:
        return make_response(
            {'result': 'unknown-error'}, 400
        )

