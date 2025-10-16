print("7-1")

car = input("what type of car would you like")

print(f"i'll see if we have any {car.title()}s")

print("7-2")

group = int(input("How many people are in your dinner group? "))

if group > 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready.")

print("7-3")

number = input("what number do you want?")
number = int(number)

if number % 10 == 0:
    print ("this is a multiple of 10")
else:
    print("its not a multiple of 10")

print("7-4")

toppings = []

while True:
    topping = input('Enter a topping or type "im done" to finish: ')
    if topping.lower() == "im done":
        break
    toppings.append(topping)

print("7-5")

while True:
    age = input('Please enter your age or type "quit" to exit: ')
    if age.lower() == "quit":
        break
    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

print("7-6")

age = ''
while age != 'quit':
    age = input("Enter your age or 'quit' to stop: ")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Ticket is free.")
    elif 3 <= age <= 12:
        print("Ticket costs $10.")
    else:
        print("Ticket costs $15.")

print("7-7")

#while True:
    #print("This loop won't end")

print("7-8")

sandwich_orders = ['tuna', 'ham', 'turkey', 'chicken', 'veggie']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("7-9")

sandwich_orders = ['tuna', 'pastrami', 'ham', 'pastrami', 'turkey', 'pastrami', 'chicken']
finished_sandwiches = []

print("Sorry, the deli has run out of pastrami!\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

print("7-10")
responses = {}

polling_active = True

while polling_active:
    name = input("What's your name? ")
    vacation = input("If you could visit one place in the world, where would you go? ")

    responses[name] = vacation

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("Dream Vacation Poll Results")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")