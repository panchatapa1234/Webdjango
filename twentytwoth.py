class AuthenticationSystem:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            raise ValueError("Username already exists.")
        self.users[username] = password
        print(f"User '{username}' registered successfully.")

    def sign_in(self, username, password):
        if username not in self.users:
            raise ValueError("Username not found.")
        if self.users[username] != password:
            raise ValueError("Incorrect password.")
        print(f"User '{username}' signed in successfully.")
        return True

    def view_users(self):
        if not self.users:
            print("No users registered.")
        else:
            print("Registered users:")
            for username in self.users:
                print(username)

    def search_users(self):
        print("Enter a username to search :")
        if username1 in self.users:
            print("Se arch Successful")           

auth_system = AuthenticationSystem()
username1 = input("Enter username to register: ")
password1 = input("Enter password: ")
try:
    auth_system.register(username1, password1)
except ValueError as e:
    print(e)

username2 = input("Enter another username to register: ")
password2 = input("Enter password: ")
try:
    auth_system.register(username2, password2)
except ValueError as e:
    print(e)

signin_username1 = input("Enter username to sign in: ")
signin_password1 = input("Enter password: ")
try:
    auth_system.sign_in(signin_username1, signin_password1)
except ValueError as e:
    print(e)

signin_username2 = input("Enter another username to sign in: ")
signin_password2 = input("Enter password: ")
try:
    auth_system.sign_in(signin_username2, signin_password2)
except ValueError as e:
    print(e)

duplicate_username = input("Enter username to register again: ")
duplicate_password = input("Enter new password: ")
try:
    auth_system.register(duplicate_username, duplicate_password)
except ValueError as e:
    print(e)

nonexistent_username = input("Enter non-existent username to sign in: ")
nonexistent_password = input("Enter password: ")
try:
    auth_system.sign_in(nonexistent_username, nonexistent_password)
except ValueError as e:
    print(e)

# View registered users
auth_system.view_users()
auth_system.search_users()
