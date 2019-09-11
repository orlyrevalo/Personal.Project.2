'''Lists: Try it Yourself 3.4 - 3.7'''
# 3.4 Guest List
guest_list = ['Ash', 'Price', 'Jasmine', 'Rik']
for guest in guest_list:
    print("I would like you to go to dinner with me, " + guest)

# 3.5 Changing Guest
guest_list = ['Ash', 'Price', 'Jasmine', 'Rik']
print(guest_list[0] + " can't make it.")
guest_list.remove('Ash')
for guest in guest_list:
    print("I would like you to go to dinner with me, " + guest)

# 3.6 More Guests
guest_list = ['Price', 'Jasmine', 'Rik']
for guest in guest_list:
    print("I have found a larger table, " + guest)
guest_list.insert(0, "Aenne")
guest_list.insert(int(len(guest_list)/2), "Ash")
guest_list.append("Orly")
print(guest_list)
for guest in guest_list:
    print("You are invited to the new table, " + guest +"")
print('\n')

# 3.7 Shrinking Guest List
print("Sorry guys for the short notice, but the larger table won't arrive on time")
print("I can only have 2 people in.\n")

print(guest_list)
uninvited = guest_list.pop()
print("I am sorry you are uninvited to my party, " + uninvited)
uninvited = guest_list.pop()
print("I am sorry you are uninvited to my party, " + uninvited)
uninvited = guest_list.pop()
print("I am sorry you are uninvited to my party, " + uninvited)
uninvited = guest_list.pop()
print("I am sorry you are uninvited to my party, " + uninvited)
print("You are still invited to the party, " + guest_list[1])
print("You are still invited to the party, " + guest_list[0])
del guest_list
print(guest_list)

