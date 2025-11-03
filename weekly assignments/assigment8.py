print("hey brenda's world")

print("8-1")
def display_message():
    print("In this chapter, I'm learning about functions in Python.")
display_message()

print("8-2")
def favorite_book(title):
    print(f"One of my favorite books is {title}.")
favorite_book("Alice in Wonderland")

print("8-3")
def make_shirt(size, message):
    print(f"A {size} shirt will be made with the message: '{message}'.")
make_shirt("Large", "Python is awesome!")
make_shirt(size="Medium", message="Keep calm and code on.")

print("8-4")
def make_shirt(size='Large', message='I love Python'):
    print(f"A {size} shirt will be made with the message: '{message}'.")
make_shirt()
make_shirt(size='Medium')
make_shirt(size='Small', message='Code is life!')

print("8-5")
def describe_city(city, country='Iceland'):
    print(f"{city} is in {country}.")
describe_city('Reykjavik')
describe_city('Akureyri')
describe_city('Paris', 'France')

print("8-6")
def city_country(city, country):
    return f"{city}, {country}"
print(city_country("Santiago", "Chile"))
print(city_country("Paris", "France"))
print(city_country("Tokyo", "Japan"))

print("8-7")
def make_album(artist, title, num_songs=None):
    album = {'artist': artist,
            'title': title}
    if num_songs is not None:
        album['songs'] = num_songs
    return album
album1 = make_album("Taylor Swift", "1989")
album2 = make_album("The Beatles", "Abbey Road")
album3 = make_album("Kendrick Lamar", "DAMN.", num_songs=14)
print(album1)
print(album2)
print(album3)

print("8-8")
def make_album(artist, title, num_songs=None):
    album = {'artist': artist,
            'title': title}
    if num_songs:
        album['songs'] = num_songs
    return album
while True:
    print("\nEnter album details (or type 'q' to quit):")
    artist = input("Artist name: ")
    if artist.lower() == 'q':
        break
    title = input("Album title: ")
    if title.lower() == 'q':
        break
    songs_input = input("Number of songs (optional, press Enter to skip): ")
    if songs_input.lower() == 'q':
        break
    if songs_input.strip() == "":
        album = make_album(artist, title)
    else:
        album = make_album(artist, title, int(songs_input))
    print("\nAlbum created:")
    print(album)

print("8-9")
def show_messages(messages):
    for message in messages:
        print(message)
messages = ["Hello!", "How are you?", "See you later!", "Good luck!"]

print("8-10") 
def show_messages(messages):
    for message in messages:
        print(message)

def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

messages = ["Hello!", "How are you?", "See you soon!", "Don't forget to smile :)"]
sent_messages = []

send_messages(messages, sent_messages)

print("\nOriginal messages list (now empty):")
print(messages)

print("\nSent messages list:")
print(sent_messages)

print("8-11")
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

original_messages = ["Hello!", "How are you?", "See you soon!", "Don't forget to smile :)"]
sent_messages = []

send_messages(original_messages[:], sent_messages)

print("\nOriginal messages list (unchanged):")
print(original_messages)

print("\nSent messages list:")
print(sent_messages)

print("8-12")
def make_sandwich(*items):
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich("turkey", "lettuce", "tomato")
make_sandwich("ham", "cheddar cheese")
make_sandwich("peanut butter", "jelly", "banana", "honey")

print("8-13")
def build_profile(first, last, **user_info):
    profile = {'first_name': first,
                'last_name': last}
    profile.update(user_info)
    return profile
my_profile = build_profile('John',
                            'Doe',
                            age=25,
                            location='New York',
                            hobby='photography')
print(my_profile)