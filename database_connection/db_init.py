from .db_connection import Dummy


def initialize(upstream_url):  # returns db connection object
    return Dummy(upstream_url)