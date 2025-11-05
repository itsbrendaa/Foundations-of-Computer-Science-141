print("hey world")

print("10-1")

file = 'learning_python.txt'
with open(file) as file_object:
    contents = file_object.read()
print("Reading entire file:\n")
print(contents)

print("\nReading line by line:\n")
with open(file) as file_object:
    for line in file_object:
        print(line.rstrip())
    
print("10-2")

filename = 'learning_python.txt'
with open(filename) as file_object:
    for line in file_object:
        modified_line = line.replace('Python', 'C')
        print(modified_line.rstrip())

print("10-3")

filename = 'learning_python.txt'
with open(filename) as file_object:
    for line in file_object.read().splitlines():
        print(line)

print("10-4")

filename = 'guest.txt'
name = input("Please enter your name: ")
with open(filename, 'w') as file_object:
    file_object.write(name)
print(f"Hello, {name}! Your name has been written to {filename}.")

print("10-5")

filename = 'guest_book.txt'
print("Enter 'quit' when you are finished.\n")
while True:
    name = input("Please enter your name: ")
    if name.lower() == 'quit':
        break
    print(f"Welcome, {name}!")
    with open(filename, 'a') as file_object:
        file_object.write(name + "\n")

    import json

print("10-6")

print("Enter two numbers and I’ll add them together.\n")

try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    result = int(num1) + int(num2)
except ValueError:
    print("Oops! That’s not a valid number. Please enter numbers only.")
else:
    print(f"The sum of {num1} and {num2} is {result}.")

print("10-7")

print("Enter two numbers to add. Type 'quit' to exit.\n")

while True:
    num1 = input("Enter the first number (or 'quit' to stop): ")
    if num1.lower() == 'quit':
        break
    num2 = input("Enter the second number (or 'quit' to stop): ")
    if num2.lower() == 'quit':
        break
    try:
        result = int(num1) + int(num2)
    except ValueError:
        print("Sorry, you must enter numbers only!\n")
    else:
        print(f"The sum of {num1} and {num2} is {result}.\n")

print("10-8")

filenames = ['cats.txt', 'dogs.txt']
for file in filenames:
    try:
        with open(file) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {file} was not found.")
    else:
        print(f"\nContents of {file}:\n{contents}")

print("10-9")

for file in filenames:
    try:
        with open(file) as f:
            contents = f.read()
    except FileNotFoundError:
        pass  # Fail silently
    else:
        print(f"\nContents of {file}:\n{contents}")

print("10-10")

text_files = ['little_women.txt', 'alice_in_wonderland.txt', 'moby_dick.txt']
for text in text_files:
    try:
        with open(text, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"File {text} not found.")
    else:
        word_count = contents.lower().count('the ')
        print(f"The word 'the' appears about {word_count} times in {text}.")

print("10-11")

fav_number_file = 'favorite_number.json'
fav_number = input("What is your favorite number? ")
with open(fav_number_file, 'w') as f:
    json.dump(fav_number, f)
print(f"Your favorite number ({fav_number}) has been saved!")

with open(fav_number_file) as f:
    number = json.load(f)
print(f"I know your favorite number! It’s {number}.")

print("10-12")

try:
    with open(fav_number_file) as f:
        number = json.load(f)
except FileNotFoundError:
    fav_number = input("What is your favorite number? ")
    with open(fav_number_file, 'w') as f:
        json.dump(fav_number, f)
    print("Got it! I'll remember that number next time.")
else:
    print(f"I know your favorite number! It’s {number}.")

print("10-13")

user_info_file = 'user_info.json'
user_info = {
    'name': input("What is your name? "),
    'age': input("What is your age? "),
    'favorite_color': input("What is your favorite color? ")}

with open(user_info_file, 'w') as f:
    json.dump(user_info, f)

with open(user_info_file) as f:
    loaded_info = json.load(f)

print("\nHere’s what I remember about you:")
for key, value in loaded_info.items():
    print(f"{key.title()}: {value}")

print("10-14")

username_file = 'username.json'
def get_new_username():
    username = input("What is your name? ")
    with open(username_file, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    try:
        with open(username_file) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = get_new_username()
        print(f"We’ll remember you when you come back, {username}!")
    else:
        correct = input(f"Are you {username}? (y/n): ")
        if correct.lower() == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We’ll remember you when you come back, {username}!")