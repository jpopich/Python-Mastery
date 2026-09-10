# Notes:
# positionals = function params in a specific order
# keyword args = args in a function call specified to a parameter
# default values = params at function definition given a value *used when a arg isnt provided*

# *args
# Arbitrary Arguments with * = takes any number of parameters in. Must be last in function definition. Creates a tuple.
        # Exmaple:
        # def make_sandwich(protein, *args):
            # ...
        # function call example: make_sandwich("bacon", "lettuce", "tomato", "mayo", "mustard")
        # protein = bacon, args = ("lettuce", "tomato", "mayo", "mustard")

# **kwargs
# Arbitrary Keyword Arguments with ** - Used to collect as many nonspecific keyword arguments. Creates a dict.
        # Exmaple:
        # def make_sandwich(protein, **kwargs):
            # ...
        # function call example: make_sandwich("bacon", veg1="lettuce", veg2="tomato", condiment1="mayo", condiment2="mustard")
        # protein = bacon, kwargs = {'veg1': 'lettuce', 'veg2': 'tomato', 'condiment1': 'mayo', 'condiment1': 'mustard'}

# import module
# import module as md
# from module import function
# from module import function as fn
# from module import *
# """ docstring example """

# 8-1: Message
print("8-1: Message")
def display_message():
    print("I'm learning about funtions in this chapter of the book.")
display_message()
print("\n\n\n")



# 8-2: Favorite Book
print("8-2: Favorite Book")
def favorite_book(title):
    print(f"One of my favorite books is {title}.")
favorite_book("Dune")
favorite_book("The Name of the Wind")
print("\n\n\n")



# 8-3: T-Shirt
print("8-3: T-Shirt")
def make_shirt(size, text):
    print(f"The shirt of size {size} will have the message '{text}' on it.")
make_shirt("XXL", "Mastermind working hea.")
make_shirt(size="XXL", text="Mastermind working hea.")
print("\n\n\n")



# 8-4: Large Shirts
print("8-4: Large Shirts")
def make_shirt(size="L", text="I love Python."):
    print(f"The shirt of size {size} will have the message '{text}' on it.")
make_shirt()
make_shirt(size="M")
print("\n\n\n")



# 8-5: Cities
print("8-5: Cities")
def describe_city(city, country="USA"):
    print(f"{city.title()} is in {country}.")
describe_city("Boston")
describe_city("New Orleans")
describe_city("Moscow")
print("\n\n\n")



# 8-6: City Names
print("8-6: City Names")
def city_country(city, country):
    return f"{city.title()}, {country.title()}"
print(f'"{city_country("paris", "france")}"')
print(f'"{city_country("london", "england")}"')
print(f'"{city_country("tokyo", "japan")}"')
print("\n\n\n")



# 8-7: Album
print("8-7: Album")
def make_album(artist_name, album_title, num_songs = None):
    album_dict = {}
    if num_songs:
        album_dict["Artist"] = artist_name.title()
        album_dict["Album Title"] = album_title.title()
        album_dict["Number of Songs"] = num_songs
    else:
        album_dict["Artist"] = artist_name
        album_dict["Album Title"] = album_title
    return album_dict

dict1 = make_album("Lil Wayne", "No Ceilings", 12)
dict2 = make_album("The Beatles", "Abbey Road",)
dict3 = make_album("Daft Punk", "Random Access Memories")
dict4 = make_album("PRESIDENT", "Blood of Your Empire", 10)
print(dict1)
print(dict2)
print(dict3)
print(dict4)
print("\n\n\n")


# 8-8: User Album
print("8-8: User Album")
while True:
    print("Type 'q' at any time to quit.")
    artist = input("Who's your favorite artists? ")
    if artist == "q":
        break
    title = input("What's your favorite album by that artist? ")
    if title == "q":
        break 
    user_dict = make_album(artist, title)
    print(user_dict)
print("\n\n\n")



# 8-9: Messages
print("8-9: Messages")
def show_messages(messages):
    for message in messages:
        print(f"Received message: {message}")
text_list = ["lol", "lmfao", "idk", "idc", "wyd", "wya"]
show_messages(text_list)
print("\n\n\n")



# 8-10: Sending Messages
print("8-10: Sending Messages")
def send_messages(messages):
    sending_messages = True
    while sending_messages:
        if messages:
            message = messages.pop()
            print(f"Sending message: {message}")
            sent_messages.append(message)
        else:   
            sending_messages = False
messages = ["lol", "lmfao", "idk", "idc", "wyd", "wya"]
sent_messages = []
print("--------------------BEFORE-------------------")
print(f"Messages to send: {messages}")
print(f"Messages sent: {sent_messages}")
print("---------------------------------------------")
send_messages(messages)
print("--------------------AFTER-------------------")
print(f"Messages to send: {messages}")
print(f"Messages sent: {sent_messages}")
print("---------------------------------------------")

print("\n\n\n")



# 8-11: Archived Messages
print("8-11: Archived Messages")

messages = ["lol", "lmfao", "idk", "idc", "wyd", "wya"]
sent_messages = []
print(f"Messages to send: {messages}")
print(f"Messages sent: {sent_messages}")
send_messages(messages[:])
print(f"Messages archived: {messages}")
print(f"Messages sent: {sent_messages}")
print("\n\n\n")



# 8-12: Sandwiches
print("8-12: Sandwiches")
def make_sandwich(*args):
    print(f"Sandwich ordered with the following add ons: {args}")
make_sandwich("bacon", "lettuce", "tomato")
make_sandwich("bacon", "mayo", "lettuce", "tomato")
make_sandwich("bacon", "mayo", "mustard", "lettuce", "tomato")
print("\n\n\n")



# 8-13: User Profiles
print("8-13: User Profiles")
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('john', 'popich', location='new orleans', field='computer science', age=33)
print(user_profile)
print("\n\n\n")



# 8-14: Cars
print("8-14: Cars")
def make_car(manufacturer, model_name, **kwargs):
    car_dict = kwargs
    car_dict['manufacturer'] = manufacturer
    car_dict['model_name'] = model_name
    return car_dict
my_old_truck = make_car("dodge", "ram", trim="sport", color='white', year=2010, engine="5.7L v8 hemi")
car = make_car('subaru', 'outback', color='blue', tow_package=True) 
print(my_old_truck)
print(car)
print("\n\n\n")



# 8-15: Printing Methods - Custom
print("8-15: Printing Methods")
import printing_functions
printing_functions.hello_world("USA")
print("\n\n\n")



# 8-16: Imports
print("8-16: Imports")
#from printing_functions import make_car
from printing_functions import make_car as mkcar
import printing_functions as pfuncs
#from printing_functions import *
#my_new_car = make_car("kia", "k5", trim="gt-line", color='white', awd_package=False)
my_new_car = mkcar("kia", "k5", trim="gt-line", color='white', awd_package=False)
my_new_car = pfuncs.make_car("kia", "k5", trim="gt-line", color='white', awd_package=False)
print(my_new_car)
print("\n\n\n")


# 8-16: Styling Functions
print("8-16: Styling Functions")
# A styling functions - choose three functions to style properly. Complete.
