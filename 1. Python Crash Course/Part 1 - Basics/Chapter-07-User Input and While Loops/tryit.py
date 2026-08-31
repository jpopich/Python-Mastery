#Notes: input() takes in input as a string, cast to int() for numerical comparison.


# 7.1 Rental Car:
# print("7.1 Rental Car:")
# car = input("What kind of rental car would you like? ")
# print(f"Let me see if I can find you a {car}.")
# print("\n\n\n")



# 7.2 Restaurant Seating:
# print("7.2 Restaurant Seating:")
# group_size = int(input("How many people are in your dinner group? "))
# if group_size > 8:
#     print("Your group will have to wait for a table.")
# else:
#     print("Your table is ready.")
# print("\n\n\n")



# 7.3 Multiples of Ten:
# print("7.3 Multiples of Ten:")
# num = int(input("Provide a number: "))
# if num % 10 == 0:
#     print(f"{num} is a multiple of ten.")
# else:
#     print(f"{num} is not a multiple of ten.")
# print("\n\n\n")



# 7.3 Multiples of Ten:
# print("7.3 Multiples of Ten:")
prompt = "\nTell me something and I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
    print(message)