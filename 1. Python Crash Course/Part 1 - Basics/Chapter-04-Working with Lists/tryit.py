# 4.1 Pizzas
print("4.1 Pizzas")
pizzas = ["meat lovers", "supreme", "deep dish"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("I really love pizza!")
print("\n\n\n")

# 4.2 Animals
print("4.2 Animals")
animals = ["lion", "dog", "raccoon"]
for animal in animals:
    print(f"A {animal} is a furry mammal.")
print("All of these animals have sharp teeth.")
print("\n\n\n")

# 4.3 Counting to Twenty
print("4.3 Counting to Twenty")
listOfTwenty = list(range(1, 21))
print(listOfTwenty)
print("\n\n\n")

# 4.4 One Million
print("4.4 One Million")
listOfOneMillion = list(range(1, 1000001))
# for value in listOfOneMillion:
#     print(value)
print("\n\n\n")

# 4.5 Summing a Million
print("4.5 Summing a Million")
print(f"Min = {min(listOfOneMillion)}")
print(f"Max = {max(listOfOneMillion)}")
print(f"Sum = {sum(listOfOneMillion)}")
print("\n\n\n")

# 4.6 Odd Numbers
print("4.6 Odd Numbers")
oddNums = list(range(1, 21, 2))
for value in oddNums:
    print(value)
print("\n\n\n")

# 4.7 Threes
print("4.7 Threes")
multiplesOfThree = list(range(3, 31, 3))
for value in multiplesOfThree:
    print(value)
print("\n\n\n")

# 4.8 Cubes
print("4.8 Cubes")
cubes = list(range(1, 11))
for value in cubes:
    value = value**3
    print(value)
print("\n\n\n")

# 4.9 List Comprehension
print("4.9 List Comprehension")
cubesLC = [value**3 for value in range(1, 11)]
for value in cubesLC:
    print(value)
print("\n\n\n")

# 4.10 Slices
print("4.10 Slices")
#Using the list from 4.3
print(f"First three items in the list: {listOfTwenty[:3]}")
print(f"Three items from the middle of the list are: {listOfTwenty[8:11]}")
print(f"The last three items in the list are: {listOfTwenty[-3:]}")
print("\n\n\n")


# 4.11 My Pizzas, Your Pizzas
print("4.11 My Pizzas, Your Pizzas")
#Using the list from 4.1 
friend_pizzas = pizzas[:] #Copy list
pizzas.append("pepperoni")
friend_pizzas.append("hawaiian")
print("My favorite pizza's are: ")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
print("\n\n\n")


# 4.12 More Loops
print("4.12 More Loops")
print("I guess I wasn't supposed to print using a for loop in prior sections, and I was meant to learn that in this exercise. I did it already.")
print("\n\n\n")


# 4.13 Buffet
print("4.13 Buffet")
fiveFoods = ('nachos', 'pickles', 'hamburgers', 'hotdogs', 'corndogs')
print(f"At the consession stand, your food options are:")
for food in fiveFoods:
    print(food)
#fiveFoods[1] = 'fries' # purposely cause error changing tuple

fiveFoods = ('nachos', 'fries', 'hamburgers', 'hotdogs', 'candies')
print("\nThe new items on our menu at consessions are: ")
for food in fiveFoods:
    print(food)
print("\n\n\n")


# 4.4  PEP 8
print("4.4  PEP 8")
print("Complete!")
print("\n\n\n")


# 4.15 Code Review
print("4.15 Code Review")
print("Complete!")

