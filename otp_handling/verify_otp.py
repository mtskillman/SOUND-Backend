import pyotp


def verify(secret_key, otp_to_eval):
    if otp_to_eval == pyotp.TOTP(secret_key).now():
        return True
    else:
        return False
