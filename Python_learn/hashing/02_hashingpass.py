# password hashing
def hash_password(password):
    hash_value = 0
    for char in password:
        hash_value += ord(char)
    return hash_value

# another advanced way
def hash_password_advanced(password):
    import hashlib
    return hashlib.sha256(password.encode()).hexdigest()
# above function uses SHA-256 hashing algorithm for better security