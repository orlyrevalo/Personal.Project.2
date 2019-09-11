'''Try it Yourself: Input 7.1 - 7.3'''
# 7-1 Rental Car
message = input("What kind of rental car would you like? ")
print("Let me see if I can find you a " + message.title() + ".")

# 7-2 Restaurant Seating
dinner_group = input("How many are you dining in? ")
dinner_group = int(dinner_group)
if dinner_group >= 8:
    print("You will have to wait for a table")
else:
    print("You're table is ready")

# 7-3 Multiples of Ten
number = int(input("Give me a number: "))
if number % 10 == 0:
    print("This number, " + str(number) + " is divisible by ten.")