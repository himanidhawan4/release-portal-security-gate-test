import subprocess
import pickle
import hashlib


def run_command(user_input):
    # Intentionally insecure: passing untrusted input to a shell
    subprocess.call(user_input, shell=True)


def load_untrusted_data(data):
    # Intentionally insecure: deserializing untrusted data
    return pickle.loads(data)


def weak_hash(password):
    # Intentionally insecure: MD5 is unsuitable for password storage
    return hashlib.md5(password.encode()).hexdigest()
