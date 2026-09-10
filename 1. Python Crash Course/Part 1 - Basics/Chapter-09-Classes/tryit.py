# Setting default values for attributes.
    # 1 - In constructor parameters as var="value"
    # 2 - Removed from constructor and only in self clauses.
# Can update attributes directly or indirectly through a method.
# Inheritance: When declaring a class that inherits, the parent class is called inside the declaration. Ex: class ElectricCar(Car): - ElectricCar inherits from Car
    # Child class MUST be in same file and appear after the parent class.
    # Child class __init_() takes in self and same params as parent.
    # Child class super().__init__() allows child to access methods of the parent.
        # After super().__init__(), you can then start adding attributes and methods to differentiate the child from the parent.
    # Overriding parent methods - write a method in the child class with the same name as the parent method.
# Composition: when one object contains or uses another object rather than inheriting from it. Think the "has-a" relationship.
# Styling: 
    # Classes should be written using CamelCase
    # A docstring should follow every class definition.
    # When importing from Python standard library and your own custom modules. Import the standard modules first followed by a space then your custom modules.

# 9-1 Restaurant:
print("9-1 Restaurant:")
class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The name of this restaurant is {self.name} and it serves {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.name} is open for business!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

restaurant = Restaurant("Mae's", "southern comfort")
print(f"Name of restaurant: {restaurant.name}.")
print(f"Cuisine type: {restaurant.cuisine_type}.")
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("\n\n\n")



# 9-2 Three Restaurants:
print("9-2 Three Restaurants:")
r1 = Restaurant("Billy Wonka's Pizzaria", "pizza")
r1.describe_restaurant()
r2 = Restaurant("Popich's Cafe", "coffee")
r2.describe_restaurant()
r3 = Restaurant("Ben Hawaiian BBQ", "jerk chicken")
r3.describe_restaurant()



# 9-3 Users:
print("9-3 Users:")
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

user1 = User("jeff", "cong", "single", "new york", 37)
user2 = User("franklin", "rosa", "married", "frankfurt", 25)
user3 = User("vanessa", "aftin", "single", "new orleans", 29)

user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()
user3.describe_user()
user3.greet_user()
print("\n\n\n")



# 9-4 Numbers Served:
print("9-4 Numbers Served")
# Added a default attribute called number_served to class Restaurant from 9-1.
restaurant = Restaurant("Cafe Today", "coffee")
print(f"Number of customers served: {restaurant.number_served}.")
print("Just served 5 more cosutomers.")
restaurant.number_served += 5
print(f"Number of customers served: {restaurant.number_served}.")
# Added a method called set_number_served to class Restaurant from 9-1.
restaurant.set_number_served(4)
print(f"Number of customers served: {restaurant.number_served}.")
# Added a method called increment_number_served to class Restaurant from 9-1.
restaurant.set_number_served(0)
restaurant.increment_number_served(65)
print(f"Number of customers served in a single day of business: {restaurant.number_served}.")
print("\n\n\n")



# 9-5 Login Attempts:
print("9-5 Login Attempts")
# Added an attribute called login_attempts to User class from 9-3.
# Added an method called increment_login_attempts to User class from 9-3.
# Added an method called reset_login_attempts to User class from 9-3.
user_test = User("ezekiel", "corte", "single", "lancaster", 32)
for i in range(6):
    user_test.increment_login_attempts()
print(f"Login attempts: {user_test.login_attempts}.")
print("Called reset_login_attempts():")
user_test.reset_login_attempts()
print(f"Login attempts: {user_test.login_attempts}.")
print("\n\n\n")



# 9-6 Ice Cream Stand:
print("9-6 Ice Cream Stand")
class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ["vanilla", "chocolate", "strawberry", "banana", "rocky road"]

    def display_flavors(self):
        print(f"Here is a list of our ice cream flavors: {self.flavors}")

my_icecream_stand = IceCreamStand("shiny ice", "ice cream")
my_icecream_stand.display_flavors()
print("\n\n\n")



# 9-7 Admin:
print("9-7 Admin")
class Admin(User):
    def __init__(self, first_name, last_name, relationship_status, location, age):
        super().__init__(first_name, last_name, relationship_status, location, age)
        self.privileges = Privileges()

# admin1 = Admin("jon", "pop", "in a relationship", "new orleans", 23)
# admin1.display_privileges()
print("\n\n\n")



# 9-8 Privileges: # To test 9-8, move the class Admin from 9-7 below this Privileges class code.
print("9-8 Privileges")
class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def display_privileges(self):
        print(f"Here is a list of an admin's privileges: {self.privileges}")

# admin2 = Admin("bob", "saget", "married", "chicago", 54)
# admin2.privileges.display_privileges()
print("\n\n\n")



# 9-9 Battery Upgrade:
print("9-9 Battery Upgrade")

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size == 40:
            self.battery_size = 65

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_electric_car = ElectricCar("toyota", "prius", 2026)
my_electric_car.battery.get_range()
print("Upgrading car battery...")
my_electric_car.battery.upgrade_battery()
print("Upgrade complete.")
my_electric_car.battery.get_range()
print("\n\n\n")



# 9-10 Imported Restaurant:
print("9-10 Imported Restaurant")
from restaurant import Restaurant as rstrt # Used an alias like this because importing Restaurant from this class has many different Restaurant variables.
test_rest = rstrt("bud's pancakes", "pancakes")
test_rest.describe_restaurant()
print("\n\n\n")



# 9-11 Imported Admin:
print("9-11 Imported Admin")
import admin as admin_test
admin3 = admin_test.Admin("cole", "bitza", "complicated", "llano", 37)
print(f"{admin3.first_name.title()} {admin3.last_name.title()}: ")
admin3.privileges.display_privileges()
print("\n\n\n")



# 9-12 Multiple Modules:
print("9-12 Multiple Modules")
from admin2 import Admin as admin_test2
admin4 = admin_test2("brent", "damina", "single", "baton rouge", 21)
print(f"{admin4.first_name.title()} {admin4.last_name.title()}: ")
admin4.privileges.display_privileges()
print("\n\n\n")



# 9-13 Dice:
print("9-13 Dice")
from random import randint
class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        print(f"Dice rolled: {randint(1, self.sides)}")

die1 = Die(6)
for i in range(10):
    die1.roll_die()
print()
die2 = Die(10)
for i in range(10):
    die2.roll_die()
print()
die3 = Die(20)
for i in range(10):
    die3.roll_die()
print("\n\n\n")



# 9-14 Lottery:
print("9-14 Lottery")
from random import choice

lottery_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "a", "b", "c", "d", "e"]
lottery_string = ''
for i in range(4):
    lottery_string += choice(lottery_list)
print(f"Any ticket matching the following string wins! {lottery_string}")
print("\n\n\n")



# 9-15 Lottery Analysis:
print("9-15 Lottery Analysis")
my_ticket = "34ab"
still_gambling = True
counter = 0
while still_gambling:
    winning_ticket = ""
    for i in range(4):
        winning_ticket += choice(lottery_list)

    print(f"{my_ticket} ----- {winning_ticket}\n")

    if my_ticket == winning_ticket:
        print("Congratulaions, you WON!")
        print(f"It only took you {counter} tries!")
        still_gambling = False
    else:
        counter += 1
print("\n\n\n")



# 9-16 Python Module of the Week:
print("9-16 Python Module of the Week")
print("""Explored the Logging module: The logging module defines a standard API for reporting errors and 
status information from applications and libraries. The key benefit of having the logging API provided by a 
standard library module is that all Python modules can participate in logging, so an application’s log can include 
messages from third-party modules.""")