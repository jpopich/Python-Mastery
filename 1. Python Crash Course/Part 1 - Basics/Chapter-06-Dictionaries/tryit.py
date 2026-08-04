#Notes: Keywords - keys(), values(), sorted(), set(list as input) - unique values only
# create a set: set = {1, 2, 2} print 1, 2

# 6.1 Person:
print("6.1 Person:")
dict = {
"first_name": "John",
"last_name": "Doe",
"age": 30,
"city": "New Orleans"
}
print(dict["first_name"])
print(dict["last_name"])
print(dict["age"])
print(dict["city"])
print("\n\n\n")



# 6.2 Favorite Numbers:
print("6.2 Favorite Numbers:")
numDict = {
    "John": 7,
    "Jess": 27,
    "Mav": 21,
    "Mac": 11
}
for key, value in numDict.items():
    print(f"{key}'s favorite number is {value}")
print("\n\n\n")



# 6.3 Glossary:
print("6.3 Glossary:")
glossary = {
    "Dictionary" : "a data structure that can map keys to values.",
    "Boolean" : "a true or false, yes or no, 0 or 1 conditional.",
    "Tuple" : "a contiguous data structure where the contents can not be changed."
}
for k, v in glossary.items():
    print(f"{k} is {v}")
print("\n\n\n")



# 6.4 Glossary2:
print("6.4 Glossary2:")
glossary = {
    "Dictionary" : "a data structure that can map keys to values.",
    "Boolean" : "a true or false, yes or no, 0 or 1 conditional.",
    "Tuple" : "a contiguous data structure where the contents can not be changed.",
    "Set" : "a list that only have unique elements.",
    "Slicing" : "a feature used to extract a smaller part of a subset of a sequence."
}
for k, v in glossary.items():
    print(f"{k} is {v}")
print("\n\n\n")



# 6.5 Rivers:
print("6.5 Rivers:")
riverDict = {
    "mississippi" : "USA",
    "niles" : "egypt",
    "amazon" : "brazil"
}
for k, v in riverDict.items():
    print(f"{k.title()} runs through {v.title()}.")
for k in riverDict.keys():
    print(f"A river in the dictionary is {k.title()}.")
for v in riverDict.values():
    print(f"A country in the dictionary is {v.title()}.")
print("\n\n\n")



# 6.6 Polling:
print("6.6 Polling:")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'zig'
}
nameList = ["mav", "jen", "jess", "edward"]
for name in nameList:
    if name in favorite_languages.keys():
        print(f"Hi {name.title()}, I see your favorite language is {favorite_languages[name]}!")
    else:
        print(f"{name.title()}, you should take the poll!")
print("\n\n\n")



# 6.7 People:
print("6.7 People:")
p1Dict = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 30,
    "city": "New Orleans"
}
p2Dict = {
    "first_name": "Jane",
    "last_name": "Doe",
    "age": 41,
    "city": "Bay St. Louis"
}
p3Dict = {
    "first_name": "Carl",
    "last_name": "Mock",
    "age": 28,
    "city": "Lafayette"
}
people = [p1Dict, p2Dict, p3Dict]
for person in people:
    print(f"Hi, {person["first_name"]} {person["last_name"]}, you are {person["age"]} and from {person["city"]}.")
print("\n\n\n")



# 6.8 Pets:
print("6.8 Pets:")
pet1Dict = {
    "pet_type": "cat",
    "owner_name": "John Doe"
}
pet2Dict = {
    "pet_type": "dog",
    "owner_name": "Jane Doe"
}

pets = [pet1Dict, pet2Dict]
for pet in pets:
    print(f"Hi, {pet["owner_name"]}! I see you own a {pet["pet_type"]}.")
print("\n\n\n")




# 6.9 Favorite Places:
print("6.9 Favorite Places:")
favorite_places = {
    "John": ["French Quarter", "New Orleans", "Bay St. Louis"],
    "Jess": ["Home", "French Quarter"],
    "Mav": ["Mexico", "my house"]
}

for k, v in favorite_places.items():
    for i in range(len(v)):
        print(f"{k}'s favorite places are {v[i]}.")
print("\n\n\n")



# 6.10 Favorite Numbers:
print("6.10 Favorite Numbers:")
numDict = {
    "John": [7, 11, 13, 21],
    "Jess": [27, 18, 25, 8],
    "Mav": [21, 22, 23],
    "Mac": [11]
}
for k, v in numDict.items():
    print(f"{k}'s favorite numbers are {v}.")
print("\n\n\n")



# 6.11 Cities:
print("6.11 Cities:")
cities = {
    "venice": {"country": "USA", "population": 800, "fun_fact": "best fishing area of the world"},
    "belle chasse": {"country": "USA", "population": 2500, "fun_fact": "is my current place of living"},
    "buras": {"country": "USA", "population": 700, "fun_fact": "it is also known as DTR"}
}
for k, v in cities.items():
    print(f"Here is all the known information about {k} here: {v}.")
print("\n\n\n")
