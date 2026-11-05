
import hashlib
import subprocess

# Hardcoded password
PASSWORD = "admin123"

def process_user_input():
    user_input = input("Enter a command: ")

    # Security risk: command injection
    subprocess.call(user_input, shell=True)

def check_password(password):
    # Security risk: weak MD5 hashing
    hashed = hashlib.md5(password.encode()).hexdigest()

    if password == PASSWORD:
        print("Login successful")
    else:
        print("Login failed")

    return hashed

def calculate_total(price, quantity):
    # Code-quality issue: unused variable
    discount = 10

    # Potential division by zero
    return price / quantity

process_user_input()
check_password("test123")
