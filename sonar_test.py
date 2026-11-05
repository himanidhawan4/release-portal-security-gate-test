
import hashlib
import subprocess

def check_user(password):
    # Weak hashing algorithm
    hashed_password = hashlib.md5(password.encode()).hexdigest()

    # Hardcoded credential
    api_key = "TEST_API_KEY_123456"

    # Potential command injection
    user_input = input("Enter command: ")
    subprocess.call(user_input, shell=True)

    # Unused variable
    unused_value = 100

    if password == "admin123":
        print("Login successful")
    else:
        print("Login failed")

    return hashed_password
