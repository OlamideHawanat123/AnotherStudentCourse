import os

class User:
    def __init__(self, name, email, password, role):
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def save_user(self):
        if self.email in User.map_email():
            print("Error: Email already exists.")
            return False

        with open("users.txt", "a") as file:
            file.write(f"{self.name},{self.email},{self.password},{self.role}\n")
        return True

    @staticmethod
    def map_email():
        users = {}
        if os.path.exists("users.txt"):
            with open("users.txt", "r") as file:
                for line in file:
                    name, email, password, role = line.strip().split(',')
                    users[email] = {"name": name, "password": password, "role": role}
        return users

    @staticmethod
    def login(email, password):
        users = User.map_email()
        return users.get(email, {}).get("password") == password
