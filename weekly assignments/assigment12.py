print("Brenda Kouam")

print("5-1")

print("test 1")

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print ("test 2")
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("test 3")
color = 'blue'
print("\nIs color == 'blue'? I predict True.")
print(color == 'blue')

print("test 4")
print("\nIs color != 'blue'? I predict False.")
print(color != 'blue')

print("test 5")
age = 20
print("\nIs age >= 18? I predict True.")
print(age >= 18)

print("test 6")
print("\nIs age < 18? I predict False.")
print(age < 18)

print("test 7")
fruit = 'apple'
print("\nIs fruit == 'apple'? I predict True.")
print(fruit == 'apple')

print("test 8")
print("\nIs fruit == 'banana'? I predict False.")
print(fruit == 'banana')

print("test 9")
temperature = 30
print("\nIs temperature > 25? I predict True.")
print(temperature > 25)

print("test 10")
print("\nIs temperature == 0? I predict False.")
print(temperature == 0)

print("5-2")

print("\nTests for equality and inequality with strings")
name = "Alice"
print("Is name == 'Alice'? I predict True.")
print(name == "Alice")

print("Is name != 'Alice'? I predict False.")
print(name != "Alice")


print("\nTests using the lower() method")
city = "NEW YORK"
print("Is city.lower() == 'new york'? I predict True.")
print(city.lower() == "new york")

print("Is city.lower() == 'los angeles'? I predict False.")
print(city.lower() == "los angeles")


print("\nNumerical tests")
age = 25
print("Is age == 25? I predict True.")
print(age == 25)

print("Is age != 25? I predict False.")
print(age != 25)

print("Is age > 20? I predict True.")
print(age > 20)

print("Is age < 20? I predict False.")
print(age < 20)

print("Is age >= 25? I predict True.")
print(age >= 25)

print("Is age <= 24? I predict False.")
print(age <= 24)


print("\nTests using 'and' and 'or'")
height = 170
weight = 65

print("Is height > 160 and weight < 70? I predict True.")
print(height > 160 and weight < 70)

print("Is height > 180 and weight < 70? I predict False.")
print(height > 180 and weight < 70)

print("Is height > 180 or weight < 70? I predict True.")
print(height > 180 or weight < 70)

print("Is height < 150 or weight > 100? I predict False.")
print(height < 150 or weight > 100)


print("\nTest whether an item is in a list")
fruits = ["apple", "banana", "orange"]
print("Is 'banana' in fruits? I predict True.")
print("banana" in fruits)

print("Is 'grape' in fruits? I predict False.")
print("grape" in fruits)


print("\nTest whether an item is not in a list")
print("Is 'grape' not in fruits? I predict True.")
print("grape" not in fruits)

print("Is 'apple' not in fruits? I predict False.")
print("apple" not in fruits)

print("5-3")

#pass
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")

#fail
alien_color = 'red'

if alien_color == 'green':
    print("You just earned 5 points!")


print("5-4")

#if block
alien_color = 'green'

if alien_color == 'green':
    print("You earned 5 points for shooting the alien!")
else:
    print("You earned 10 points!")

#eles
alien_color = 'yellow'

if alien_color == 'green':
    print("You earned 5 points for shooting the alien!")
else:
    print("You earned 10 points!")

print("5-5")

#green
alien_color = 'green'

if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")

#yellow
alien_color = 'yellow'

if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")

#red
alien_color = 'red'

if alien_color == 'green':
    print("You earned 5 points!")
elif alien_color == 'yellow':
    print("You earned 10 points!")
else:
    print("You earned 15 points!")