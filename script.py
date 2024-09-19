import pyotp
import qrcode


def generate_qr_code(totp_secret):
    totp = pyotp.TOTP(totp_secret)
    provisioning_uri = totp.provisioning_uri(name='Raheel', issuer_name='Microsoft Authenticator')
    qr = qrcode.make(provisioning_uri)
    qr.save("totp_qr.png")


# Generate random secret for user, base 32 secret.
totp_secret = pyotp.random_base32()
print("Your TOTP Secret (store it somewhere): ", totp_secret)
generate_qr_code(totp_secret)
