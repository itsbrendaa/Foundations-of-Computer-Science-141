print("hello world")

print("4-1")
pizzas = ["meatball pizza", "cheese pizza", "pepperoni pizza"]

for pizza in pizzas:
    print(f"that {pizza.title()}, was a delicious!")
    print(f"I can't wait for the next slice of, {pizza.title()}.\n")
    print("that was a great meal! I really love pizza")
    
print ("4-2")
pets = ["dogs", "cats", "hampsters"]

for pet in pets:
    print(f"that {pet.title()}, is so cute!")
    print(f"i love, {pet.title()}.\n can be very playful at times")
    print(f"not all, {pet.title()}.\n are friendly")
    print("Any of these animals would make a great pet")

print ("4-3")
for number in range(1, 21):
    print(number)

print ("4-4")
#for number in range(1, 10**6):
#    print(number)

print("4-5")
print(min(range(1, 10**6+1)))
print(max(range(1, 10**6+1)))
print(sum(range(1, 10**6+1)))

print("4-6")
for odd_number in range(1, 21,2):
    print(odd_number)

print("4-7")
threes= list(range(0, 30, 3))

for three in threes:
    print(three)

print("4-8")
cubes= []

for i in range(1, 11):
    cubes.append(i**3)
    print(i**3)

print("4-9")
cube= [value**3 for value in range(1, 11)]
print(cube)

print("4-10")
