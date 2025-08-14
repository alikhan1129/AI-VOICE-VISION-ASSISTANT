import getpass

SECURE_COMMANDS = ["open", "delete", "shut down"]  # Add keywords to secure

# You can later store this encrypted or in an env variable
PASSWORD = "1234"

def is_secure_command(text):
    return any(cmd in text for cmd in SECURE_COMMANDS)

def verify_password():
    print("Password required for this command.")
    pwd = getpass.getpass("Enter password: ")
    return pwd == PASSWORD
