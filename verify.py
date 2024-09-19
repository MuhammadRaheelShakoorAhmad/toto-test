import pyotp


def verify_secret(user_sec, totp_code):
    totp = pyotp.TOTP(user_sec)
    if totp.verify(totp_code):
        print("Validated!")
    else:
        print("Not Valid")


secret = input("Enter secret: ")
code = int(input("Enter code: "))
verify_secret(secret, code)
