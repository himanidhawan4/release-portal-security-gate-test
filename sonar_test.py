
import hashlib

def insecure_password_hash(password):
    # Weak hashing algorithm: MD5
    return hashlib.md5(password.encode()).hexdigest()


def insecure_token_hash(token):
    # Weak hashing algorithm: SHA-1
    return hashlib.sha1(token.encode()).hexdigest()


def execute_user_input(user_input):
    # Unsafe use of eval()
    result = eval(user_input)
    return result


if __name__ == "__main__":
    password = "demo_password"
    token = "demo_token"

    print("MD5 Hash:", insecure_password_hash(password))
    print("SHA-1 Hash:", insecure_token_hash(token))
    print("Evaluation:", execute_user_input("2 + 3"))
