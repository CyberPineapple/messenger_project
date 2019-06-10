import binascii
import hashlib
import os


def hash_password(password, algorithm="sha512"):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode("ascii")
    pwdhash = hashlib.pbkdf2_hmac(algorithm, password.encode("utf-8"), salt,
                                  100000)
    pwdhash = binascii.hexlify(pwdhash)

    return (salt + pwdhash).decode("ascii")


def verify_password(stored_password, provided_password, algorithm="sha512"):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac(algorithm, provided_password.encode("utf-8"),
                                  salt.encode("ascii"), 100000)
    pwdhash = binascii.hexlify(pwdhash).decode("ascii")

    return pwdhash == stored_password
