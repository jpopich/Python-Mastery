# 5.1 Conditional Tests
print("5.1 Conditional Tests")
car = 'toyota'
print("Is car == toyota, I predict True.")
print(car == 'toyota')
print("Is car == audi, I predict False.")
print(car == 'audi')
print("Is car == Toyota, I predict False.")
print(car == 'Toyota')
titleCase = 'Toyota'
print("Is car == Toyota.lower(), I predict True.")
print(car == titleCase.lower())
print("\n\n\n")


# 5.2 More Conditional Tests
print("5.2 More Conditional Tests")
print("Testing equality in string:")
truck = "Ford"
print(f"I predict True: {truck == "Ford"}")

print("Testing inquality in string:")
print(f"I predict False: {truck != "Ford"}")

print("Testing using lower():")
print(f"I predict True: {truck.lower() != "FORD"}")

print("Testing numerical inequality:")
print(f"I predict True: {8 == 8}")

print("Testing numerical equality:")
print(f"I predict False: {8 != 8}")

print("Testing numerical GT:")
print(f"I predict False: {8 > 8}")

print("Testing numerical LT:")
print(f"I predict True: {8 < 9}")

print("Testing numerical GTE:")
print(f"I predict False: {8 >= 9}")

print("Testing numerical LTE:")
print(f"I predict True: {8 <= 9}")

print("Testing using and:")
print(f"I predict True: {16 < 17 and truck == "Ford"}")

print("Testing numerical or:")
print(f"I predict False: {8 > 9 or 9 < 8}")

listTest = ["FORD", "toyota", "Toyota"]
print(f"I predict False: {truck in listTest}")
print(f"I predict True: {truck not in listTest}")
print("\n\n\n")


# 5.3 Alien Colors #1
print("5.3 Alien Colors #1")
alien_color = 'green'
if alien_color == 'green':
    print("Player gains 5 points!")
if alien_color == 'red':
    print("Player gains 5 points!")
if alien_color == 'green':
    print("Player gains 10 points!")
print("\n\n\n")


# 5.4 Alien Colors #2
print("5.4 Alien Colors #2")
alien_color = 'red'
if alien_color == 'green':
    print("Player gains 5 points for shooting down the green alien.")
else:
    print("Player gains 10 points!")
if alien_color != 'green':
    print("Player gains 5 points for shooting down the green alien.")
else:
    print("Player gains 10 points!")
print("\n\n\n")


# 5.5 Alien Colors #3
print("5.5 Alien Colors #3")
alien_color = 'green'
if alien_color == 'green':
    print("Player gains 5 points for shooting down the green alien.")
elif alien_color == 'yellow':
    print("Player gains 10 points for shooting down the yellow alien.")
else:
    print("Player gains 15 points for shooting down the red alien.")
alien_color = 'yellow'
if alien_color == 'green':
    print("Player gains 5 points for shooting down the green alien.")
elif alien_color == 'yellow':
    print("Player gains 10 points for shooting down the yellow alien.")
else:
    print("Player gains 15 points for shooting down the red alien.")
alien_color = 'red'
if alien_color == 'green':
    print("Player gains 5 points for shooting down the green alien.")
elif alien_color == 'yellow':
    print("Player gains 10 points for shooting down the yellow alien.")
else:
    print("Player gains 15 points for shooting down the red alien.")
print("\n\n\n")


# 5.6 Stages of Life
print("5.6 Stages of Life")
age = 27
if age < 2:
    print("You are a baby.")
elif age >= 2 and age < 4:
    print("You are a toddler.")
elif age >= 4 and age < 13:
    print("You are a kid.")
elif age >= 13 and age < 20:
    print("You are a teenager.")
elif age >= 20 and age < 65:
    print("You are a adult.")
else:
    print("You are a elder.")
print("\n\n\n")


# 5.7 Favorite Fruit
print("5.7 Favorite Fruit")
fav_fruits = ['watermelon', 'strawberry', 'kiwi']
if 'banana' in fav_fruits:
    print(f"You really like bananas.")
if 'kiwi' in fav_fruits:
    print(f"You really like kiwi.")
if 'watermelon' in fav_fruits:
    print(f"You really like watermelon.")
if 'pineapple' in fav_fruits:
    print(f"You really like pineapple.")
if 'strawberry' in fav_fruits:
    print(f"You really like strawberry.")
print("\n\n\n")


# 5.8 Hello Admin
print("5.8 Hello Admin")
usernames = ['BIGmac', 'mavTopG', 'jessXO', 'johnGG', 'admin']
for username in usernames:
    if username == 'admin':
        print(f'Hello {username}, would you like to see a status report?')
    else:
        print(f'Hello {username}, thank you for logging in again.')
print("\n\n\n")


# 5.9 No Users
print("5.9 No Users")
usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f'Hello {username}, would you like to see a status report?')
        else:
            print(f'Hello {username}, thank you for logging in again.')
else:
    print("We need to find some users!")
print("\n\n\n")


# 5.10 Checking Usernames
print("5.10 Checking Usernames")
current_users = ['BIGmac', 'mavTopG', 'jessXO', 'johnGG', 'admin']
new_users = ['BIGmac', 'mavTopG', 'jessXOXO', 'johnGx3', 'teflonHammer']
copy_current_users = []
for user in current_users:
    copy_current_users.append(user.lower())

for user in new_users:
    if user.lower() in copy_current_users:
        print(f'You will need to choose another username, {user} is already in use!')
    else:
        print(f'That username is available!')
print("\n\n\n")


# 5.11 Ordinal Numbers
print("5.11 Ordinal Numbers")
numArr = list(range(1, 10))
for num in numArr:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(f'{num}th')
print("\n\n\n")


# 5.12 Styling if Statments
print("5.12 Styling if Statments")
print("Complete!")
print("\n\n\n")


# 5.13 Your Ideas
print("5.13 Your Ideas")
print("I have some great video game ideas I want to create. I also want to create a website for my brother, but before that I want to update my portfolio. " \
"As far as datasets, I do not know of any out there that I am interested in right now.")
print("\n\n\n")