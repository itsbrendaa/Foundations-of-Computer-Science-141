print("hello world")

print("6-1")

person= {"first_name": "John",
         "last name": "Cena",
         "age":"47",
         "city":"West Newbury"}
print(person)

print("6-2")
favorite_numbers = {"Alice": "7", 
                    "Bob": "3", 
                    "Charlie": "42", 
                    "Diana": "8", 
                    "Eve": "13"}
for numbers in favorite_numbers:
    print(f"{numbers} favorite numbers is {favorite_numbers[numbers]}")

print("6-3")
glossary = { "Variable": "A named used to store data in the memory.",
    "Function": "A block of organized, reusable code that is used to perform a single action.",
    "Loop": "A sequence of instructions that is repeated until a condition is met.",
    "List": "A collection of items that are ordered and changeable.",
    "Dictionary": "A collection of pairs that are unordered and changeable",
    "Tuple": "A collection of items that are ordered and unchangeable.",
    "Set": "A collection of items that are unordered and unindexed.",
    "Class": "A blueprint for creating objects that encapsulates data and behavior.",
    "Object": "An instance of a class that contains data and behavior.",
    "Method": "A function that is defined within a class and operates on its instances."}
for words in glossary:
    print(f"{words}: {glossary[words]}")

print("6-4")
for words in glossary:
    print(f"{words}: {glossary[words]}")

print("6-5")
rivers = {"Nile": "Egypt",
          "Amazon": "Brazil",
          "Yangtze": "China"}
for river in rivers:
    print(f"The {river} runs through {rivers[river]}.")
for river in rivers:
    print(river)   
for country in rivers.values():
    print(country)

print("6-6")
favorite_languages = {'Jenn': 'python',
                    'Bob': 'c',
                    'Eve': 'ruby',
                    'Phil': 'python',}
people = ['Jenn', 'Bob', 'Eve', 'Phil', 'Sam', 'Alice']
for person in people:
    if person in favorite_languages:
        print(f"Thank you for taking the poll, {person}")
    else:
        print(f"{person}, please take our poll!")

print("6-7")
favorite_languages = {'Jenn': 'python',
                    'Bob': 'c',
                    'Eve': 'ruby',
                    'Phil': 'python',}
for language in set (favorite_languages.values()):
    print(language)
#remove set to see duplicate values

print("6-8")

pet1 = {"type": "dog",
        "owner": "Alice"}

pet2 = {"kind": "cat",
        "owner": "Bob"}

pet3 = {"kind": "parrot",
        "owner": "Charlie"}

pet4 = {"kind": "hamster",
        "owner": "Diana"}

pet5 = {"Kind": "rabbit",
    "owner": "Ethan"}

pets = [pet1, pet2, pet3, pet4, pet5]

for pet in pets:
    print("Pet Information:")
    for key, value in pet.items():
        print(f"  {key.title()}: {value}")

print("6-9")
favorite_places = { "Brenda": ["Douala", "Washington DC"],
                    "Alice": ["Paris", "New York"],
                    "Bob": ["Tokyo"],
                    "Charlie": ["London", "Berlin", "Rome"]}
for name, places in favorite_places.items():
    print(f"{name}'s favorite places are: {favorite_places[name]}")

print("6-10")
favorite_numbers = {"Brenda": [7, 8],
                    "Alice": [2, 4],
                    "Bob": [3],
                    "Charlie": [1, 6, 3]}
for numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are: {favorite_numbers[name]}")

print("6-11")

cities = {"New York City": {"country": "USA",
                             "population": "8.4 million",
                            "fact": "The Statue of Liberty is located here."},
          "Tokyo": {"country": "Japan",     
                    "population": "14 million",
                    "fact": "Tokyo is the largest metropolitan area in the world."},
          "Paris": {"country": "France",    
                    "population": "2.1 million",
                    "fact": "The Eiffel Tower is located here."}}
for city in cities:
    print(f"{city} is in {cities[city]['country']}, It has a population of {cities[city]['population']}. Fun fact: {cities[city]['fact']}")

print("6-12")

ppl= {"username": "efermo",
          "first name": "enrico",
          "last name": "fermi",}
for key, value in ppl.items():
    print(f"Key: {key}")
    print(f"Value: {value}")
