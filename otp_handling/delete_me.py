import pyotp

def test_func(secret_key):
    return pyotp.TOTP(secret_key).now()