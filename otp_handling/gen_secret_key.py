from pyotp import random_base32


def gen_new_secret_key():
    return random_base32()  # NOTE use this to make new secret key
