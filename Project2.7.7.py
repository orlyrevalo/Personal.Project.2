''''While Loops: Try it Yourself 7-8 - 7-10'''
# 7-8 Deli
print("\nDeli")
sandwich_orders = ['tuna', 'chicken', 'pork', 'veggie', 'beef']
finished_sandwiches = []
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print("I made you a " + finished_sandwich)
    finished_sandwiches.append(finished_sandwich)
print("The following sandwiches were made: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

# 7-9 No Pastrami
print("\nNo Pastrami")
sandwich_orders = ['tuna', 'pastrami', 'chicken', 'pork', 'pastrami', 'veggie', 'beef', 'pastrami']
finished_sandwiches = []
print("The deli has run out of pastrami.")
while 'pastrami'in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print("I made you a " + finished_sandwich)
    finished_sandwiches.append(finished_sandwich)
print("The following sandwiches were made: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())

# 7-10 Dream Vacation
print("\nDream Vacation")
dream_vacation = {}
poll_active = True
while poll_active:
    name = input("What is your name? ")
    dream_vacation[name] = input("If you could visit one place in the world, where would you go?: ")
    response = input("Is there anyone else who want to take this survey (yes/no): ")
    if response == 'no':
        poll_active = False

for name, place in dream_vacation.items():
    print(name.title() + "'s dream vacation is in" + place.title())