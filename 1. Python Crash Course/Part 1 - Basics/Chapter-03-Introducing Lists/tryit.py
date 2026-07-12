# 3.1 Names:
print('----TRY IT YOURSELF----')
print('\n3.1 Names:')
names = ['John', 'Jess', 'Mac', 'Div', 'Mav']

for name in names:
    print(name)

# 3.2 Greetings
print('\n\n\n3.2 Greetings:')
for name in names:
    print(f'Hey {name}!, how are you doing bud?')


# 3.3 Your Own List:
print('\n\n\n3.3 Your Own List:')
transportation = ['Toyota Tundra', 'Honda Accord Sport', 'Toyota Rav 4', '1969 Ford Mustang']
for vehicle in transportation:
    print(f"I would like to own a {vehicle} one day.")

#I dont believe I was meant to use loops... lol oh well.

# 3.4 Guest List:
print('\n\n\n3.4 Guest List:')
invitations = ['Bas Rutten', 'Woody Harrelson', 'Theo Von']
for person in invitations:
    print(f'Hey {person}, you are invited to my event!')


# 3.5 Changing Guest List:
print('\n\n\n3.5 Changing Guest List:')
unavailable_guest = invitations[2]
print(f'{unavailable_guest.title()} is unavailable to make the event!')
invitations[2] = 'Bob Ross'
for person in invitations:
    print(f'Hey {person}, you are invited to my event!')

# 3.6 More Guest:
print('\n\n\n3.6 More Guest:')
print("We found a bigger dinner table so we are inviting more guests!")
invitations.insert(0, 'Brian Cox')
invitations.insert(2, 'Isaac Newton')
invitations.append('Alexander the Great')
for person in invitations:
    print(f'Hey {person}, this is your invitation to my event, hope you can make it!')

# 3.7 Shrinking Guest List:
print('\n\n\n3.7 Shrinking Guest List:')
print('Unfortunately mistakes were made, and I will only be able to invite two guests in total.')
uninvited_guest = invitations.pop(-1)
print(f"Sorry {uninvited_guest}, but I had to uninvite you.")
uninvited_guest = invitations.pop(-2)
print(f"Sorry {uninvited_guest}, but I had to uninvite you.")
uninvited_guest = invitations.pop(-3)
print(f"Sorry {uninvited_guest}, but I had to uninvite you.")
uninvited_guest = invitations.pop(2)
print(f"Sorry {uninvited_guest}, but I had to uninvite you.")
for person in invitations:
    print(f'Hey {person}, you are still invited to my event!')
print(invitations)
for i in range(2):
    del invitations[0]
    print(invitations)



# 3.8 Seeing the World:
print('\n\n\n3.8 Seeing the World:')
bucket_list = ['Japan', 'Belarus', 'Germany', 'France', 'Portugal']
print(bucket_list)
print(sorted(bucket_list))
print(f'List not affected: {bucket_list}')
print(sorted(bucket_list, reverse=True))
print(f'List not affected: {bucket_list}')
bucket_list.reverse()
print(f'Reversed: {bucket_list}')
bucket_list.reverse()
print(f'Reversed again to original ordering: {bucket_list}')
bucket_list.sort()
print(f'sort(): {bucket_list}')
bucket_list.sort(reverse=True)
print(f'sort(reverse=True): {bucket_list}')


# 3.9 Dinner Guests:
print('\n\n\n3.9 Dinner Guests:')
new_guest_list = ['Bas Rutten', 'Woody Harrelson', 'Theo Von', 'Bob Ross', 'Isaac Newton', 'Brian Cox', 'Alexander the Great']
print(f'The number of guests I invited to dinner is {len(new_guest_list)}')



# 3.10 Every Function:
print('\n\n\n3.10 Every Function:')







