class User:
    def __init__(self, first_name, last_name, relationship_status, location, age):
        self.first_name = first_name
        self.last_name = last_name
        self.relationship_status = relationship_status
        self.location = location
        self.age = age
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"User: {self.first_name.title()} {self.last_name.title()} is {self.age} years old. Lives in {self.location} and is currently {self.relationship_status}.")

    def greet_user(self):
        print(f"Hi, {self.first_name.title()} {self.last_name.title()}, how are you?!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, relationship_status, location, age):
        super().__init__(first_name, last_name, relationship_status, location, age)
        self.privileges = Privileges()

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def display_privileges(self):
        print(f"Here is a list of an admin's privileges: {self.privileges}")