import hashlib, binascii, os

# This function receives a password as a parameter
# its hashes and salts using sha512 encoding
def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

# below provide a plain password and see its hashed/salted output
hashedpassword = hash_password("modcom2020")
print(hashedpassword)
#
# we use sha512 algorithm
# this function checks if hashed password is the same as
# provided password
def verify_password(hashed_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = hashed_password[:64]
    hashed_password = hashed_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == hashed_password
# run it , provide the hashed and the real password
# SHOULD GIVE YOU TRUE/FALSE
# status = verify_password('102c0e772030d853168eef980facef5bc79b94e9680ed2a5e4c45d66dbb3b493953eeceb575f64d3ce49969cf5f0e3bdbd1274c566a6950c7c6ac44f5861ed5d111900c03023547e0699a0d023b85ca7c051e5b1cee97e79c37689b858b24200', "")
# print(status)