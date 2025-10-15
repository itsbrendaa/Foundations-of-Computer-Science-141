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
topping = ""

while topping != "im done":
    topping = input('Enter a topping or type "im done" to finish:')
    toppings.append(topping)

print(f"your pizza toppings are: {toppings}")

("7-5")
while True:
    age = input('Please enter your age or type "quit" to exit:')

    age = int(age)
    if age < 3:
        print("Your ticket is free!")
    elif 3 <= age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
    if age() == 'quit':
        break