from user import User

class Admin(User):
    def __init__(self, first_name, last_name, relationship_status, location, age):
        super().__init__(first_name, last_name, relationship_status, location, age)
        self.privileges = Privileges()

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def display_privileges(self):
        print(f"Here is a list of an admin's privileges: {self.privileges}")