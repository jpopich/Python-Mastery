#Notes: input() takes in input as a string, cast to int() for numerical comparison.


# 7.1 Rental Car:
print("7.1 Rental Car:")
car = input("What kind of rental car would you like? ")
print(f"Let me see if I can find you a {car}.")
print("\n\n\n")



# 7.2 Restaurant Seating:
print("7.2 Restaurant Seating:")
group_size = int(input("How many people are in your dinner group? "))
if group_size > 8:
    print("Your group will have to wait for a table.")
else:
    print("Your table is ready.")
print("\n\n\n")



# 7.3 Multiples of Ten:
print("7.3 Multiples of Ten:")
num = int(input("Provide a number: "))
if num % 10 == 0:
    print(f"{num} is a multiple of ten.")
else:
    print(f"{num} is not a multiple of ten.")
print("\n\n\n")




# 7-4: Pizza Toppings # print("7-4: Pizza Toppings") 
while True: 
    topping = input("Enter your desired pizza topping: ") 
    if topping.lower() == "quit": 
        break   
    print(f"{topping.title()} will be added to your pizza!") 
print("\n\n\n") 



# 7-5: Movie Tickets 
print("7-5: Movie Tickets") 
while True: 
    age = int(input("Enter your age: ")) 
    if age < 3: 
        print("Ticket is free.") 
    elif age >= 3 and age <= 12: 
        print("Ticket is $10.") 
    else: 
        print("Ticket is $15.") 
        break 
print("\n\n\n")



# 7-6: Three Exits 
print("7-6: Three Exits") 
print("Conditional Test") 
topping = "" 
while topping.lower() != "quit": 
    topping = input("Enter your desired pizza topping: ") 
    if topping.lower() != "quit": 
        print(f"{topping.title()} will be added to your pizza!") 

print("\nActive Variable (Flag)") 
flag = True 
while flag: 
    topping = input("Enter your desired pizza topping: ") 
    if topping.lower() != "quit": 
        print(f"{topping.title()} will be added to your pizza!") 
        continue 
    flag = False 

print("\nBreak Statment") 
while True: 
    topping = input("Enter your desired pizza topping: ") 
    if topping.lower() == "quit": 
        break 
    print(f"{topping.title()} will be added to your pizza!") 
print("\n\n\n") 



# 7-7: Infinity 
print("7-7: Infinity") 
print("This challenge runs an infinite loop. It is commented out so the later challenges may run.") 
i = 0 
while True: 
    print(i) 
    i += 1 
print("\n\n\n") 



# 7-8: Deli 
print("7-8: Deli") 
sandwich_orders = ["italian", "philly cheesesteak", "reuben", "roast beef", "ham", "turkey", "tuna", "pastrami"] 
finished_sandwiches = [] 
print(f"Sandwiches that are currently on order: {sandwich_orders}.") 
while sandwich_orders: 
    sandwich = sandwich_orders.pop() 
    print(f"I made your {sandwich}.") 
    finished_sandwiches.append(sandwich) 
    print(f"Finished sandwiches: {finished_sandwiches}.") 
print("\n\n\n") 
    
    
    
# 7-9: No Pastrami 
print("7-9: No Pastrami") 
sandwich_orders = ["italian", "pastrami", "philly cheesesteak", "pastrami", "reuben", "roast beef", "pastrami", "ham", "turkey", "tuna", "pastrami"] 
print(f"Our order queue: {sandwich_orders}") 
print("Unfortunately, we are all out of pastrami.") 
while "pastrami" in sandwich_orders: 
    sandwich_orders.remove("pastrami") 
    print(f"Our order queue after removal of pastrami: {sandwich_orders}") 
print("\n\n\n") 



# # 7-10: Dream Vacation 
print("7-10: Dream Vacation") 
polling_active = True 
poll_dict = {} 
while polling_active: 
    name = input("What is your name? ") 
    response = input("If you could visit one place in the world, where would you go? ") 
    continue_poll = input("Is anyone else going to poll after you? (yes/no): ") 
    poll_dict[name] = response 
    if continue_poll.lower() == "no": 
        polling_active = False 
        print(poll_dict) 
        
for k, v in poll_dict.items(): 
    print(f"{k.title()} would like to visit {v.title()}!")