import cx_Oracle
from os import environ


class Dummy:  # this object manages db connection
    def __init__(self, link_url):
        self.upstream_url = link_url
        '''
        name = environ['DB_NAME']
        user = environ['USERNAME']
        password = environ['PASSWORD']
        host = environ['HOSTNAME']
        port = environ['PORT']
        connection = cx_Oracle.connect(user, password, host)
        self.cursor = connection.cursor()
        '''
        self.private_keys = {2: "OKP352FJMFDFBDG2"}
        self.tokens = {}

    def store_token_in_db(self, id_value, token_to_store):
        self.tokens[id_value] = token_to_store
        return True

    def return_private_key(self, id_value):
        return self.private_keys.get(id_value)

    def return_token_in_db(self, id_value):
        return self.tokens.get[id_value]

    def return_all_tokens(self):
        return self.tokens.values()

