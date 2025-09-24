print("5-1")

car = 'tesla'
print("Is car == 'mercedez'? I predict True.")
print(car == 'mercedez')
print("\nIs car == 'chevrolet'? I predict False.")
print(car == 'chevrolet')
print("Is car == 'bmw'? I predict True.")
print(car == 'bmw')
print("\nIs car == 'ford'? I predict False.")
print(car == 'ford')
print("Is car == 'tesla'? I predict True.")
print(car == 'tesla')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("Is car == 'tesla'? I predict True.")
print(car == 'tesla')
print("\nIs car == 'tesla'? I predict False.")
print(car == 'tesla')
print("Is car == 'tesla'? I predict True.")
print(car == 'tesla')
print("\nIs car == 'tesla'? I predict False.")
print(car == 'tesla')

print("5-2")

#part 1
print("Tests for equality and inequality with strings:")
print("apple" == "apple") 
print("apple" != "banana")  
print("apple" == "banana") 
print("apple" != "apple")

#part 2
print("Tests using the lower() method:")
print("APPLE".lower() == "apple")  
print("Banana".lower() == "banana")  
print("Cherry".lower() == "cherry")  
print("Date".lower() == "passionfruit")  

#part 3
print("Numerical tests:")
num = 10
print(num == 10)  
print(num != 5)   
print(num > 5)    
print(num < 20)   
print(num >= 10)  
print(num <= 10)  

print(num == 5)   
print(num != 10)  
print(num > 20)   
print(num < 5)    
print(num >= 15)  
print(num <= 5)   

#part 4
print("Tests using and / or:")
a = 5
b = 10
print(a < 10 and b > 5)  
print(a == 5 or b == 5)  
print(a > 10 and b < 5)  
print(a == 0 or b == 0)  

#part 5
print("Test whether an item is in a list:")
fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)  
print('orange' in fruits)  

#part 6
print("Test whether an item is not in a list:")
print('grape' not in fruits)  
print('apple' not in fruits)

print("5-3")

alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points!")

print("5-4")
alien_color = 'green'

if alien_color == 'green':
    print("You just earned 5 points")
else:
    print("You just earned 10 points.")

print("5-5")

#part 1
alien_color = 'green'

if alien_color == 'green':
    print("Player earned 5 points.")
elif alien_color == 'yellow':
    print("Player earned 10 points.")
else:
    print("Player earned 15 points.")

#part 2
alien_color = 'yellow'

if alien_color == 'green':
    print("Player earned 5 points.")
elif alien_color == 'yellow':
    print("Player earned 10 points.")
else:
    print("Player earned 15 points.")

#part 3
alien_color = 'red'

if alien_color == 'green':
    print("Player earned 5 points.")
elif alien_color == 'yellow':
    print("Player earned 10 points.")
else:
    print("Player earned 15 points.")

print("5-6")
age = 25

if age < 2:
    print("The person is a baby.")
elif age < 4:
    print("The person is a toddler.")
elif age < 13:
    print("The person is a kid.")
elif age < 20:
    print("The person is a teenager.")
elif age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")

print("5-7")

favorite_fruits = ['mango', 'apple', 'banana']

if 'banana' in favorite_fruits:
    print("You really like bananas!")
if 'apple' in favorite_fruits:
    print("You really like apples!")
if 'orange' in favorite_fruits:
    print("You really like oranges!")
if 'mango' in favorite_fruits:
    print("You really like mangoes!")
if 'grape' in favorite_fruits:
    print("You really like grapes!")

print("5-8")

usernames = ['admin', 'Jaden', 'Maria', 'Alex', 'Liam']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")


print("5-9")

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username}, thank you for logging in again.")
else:
    print("We need to find some users!")

print("5-10")

#part 1
current_users = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']

#part 2
new_users = ['bob', 'Frank', 'alice', 'Grace', 'HEIDI']

#part 3
current_users_lower = [user.lower() for user in current_users]

#part 4
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry, the username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")

print("5-11")

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        suffix = 'st'
    elif number == 2:
        suffix = 'nd'
    elif number == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    print(f"{number}{suffix}")

print("5-12")
#i doubled checked my formating with the help of chat gpt.It was correct
#for the most part and i had minor mistakes like spacing beside commas

print ("5-13")
#i would still like to look into creting a social media app similar to instagram
#or tictok where you can share videos and interact with others.