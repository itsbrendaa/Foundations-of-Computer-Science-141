print("hello world")

print("3-1")
names = ["Moyin", "Angelic", "Francesca"]
print(names[0])
print(names[1])
print(names[2])

print("3-2")
print (f"Hey {names[0]}, i miss you so much")
print (f"Hey {names[1]}, i'll be back for christmas break so we can hang out then")
print (f"{names[-1]}, in the future i'll plan a trip to france so we can hang out togetehr for the summer")

print("3-3")
transportation = ["car", "bike", "metro/train", "bus"]
print (f"I would like to own a {transportation[0]} one day.")
print (f"I wouldn't want to ride a {transportation[1]} to work.")
print (f"I love taking the {transportation[2]} to school. It so covienient and fast.")

print("3-4")
dinner_guest_list = ["Moyin", "Angelic", "Francesca", "Mom", "Dad"]
print (f"{dinner_guest_list[0]}, would you like to come to dinner?")
print (f"{dinner_guest_list[1]}, would you like to come to dinner?")   
print (f"{dinner_guest_list[2]}, would you like to come to dinner?")
print (f"{dinner_guest_list[3]}, would you like to come to dinner?")
print (f"{dinner_guest_list[4]}, would you like to come to dinner?")

print("3-5")
print (f"Unfortunately, {dinner_guest_list[4]} can't make it to dinner.")
dinner_guest_list[4] = "uncle"
print (f"{dinner_guest_list[0]}, would you like to come to dinner?")
print (f"{dinner_guest_list[1]}, would you like to come to dinner?")
print (f"{dinner_guest_list[2]}, would you like to come to dinner?")
print (f"{dinner_guest_list[3]}, would you like to come to dinner?")
print (f"{dinner_guest_list[4]}, would you like to come to dinner?")

print("3-6")
print("I found a bigger dinner table")
dinner_guest_list.insert(0, "aunt")
dinner_guest_list.insert(2, "cousin")  
dinner_guest_list.append("grandma")
print (f"{dinner_guest_list[0]}, would you like to come to dinner?")
print (f"{dinner_guest_list[1]}, would you like to come to dinner?")
print (f"{dinner_guest_list[2]}, would you like to come to dinner?")
print (f"{dinner_guest_list[3]}, would you like to come to dinner?")
print (f"{dinner_guest_list[4]}, would you like to come to dinner?")
print (f"{dinner_guest_list[5]}, would you like to come to dinner?")
print (f"{dinner_guest_list[6]}, would you like to come to dinner?")
print (f"{dinner_guest_list[7]}, would you like to come to dinner?")

print("3-7")
print("the new dinner table won't arrive in time, so I can only invite 2 people for dinner. Sorry.")
print (f"Sorry {dinner_guest_list.pop()}, I can't invite you to dinner.")
print (f"Sorry {dinner_guest_list.pop()}, I can't invite you to dinner.")
print (f"Sorry {dinner_guest_list.pop()}, I can't invite you to dinner.")
print (f"Sorry {dinner_guest_list.pop()}, I can't invite you to dinner.")
print (f"{dinner_guest_list[0]}, you're still invited to dinner.")
print (f"{dinner_guest_list[1]}, you're still invited to dinner.")
del dinner_guest_list[0]
del dinner_guest_list[1]

print("3-8")
Europe_places = ["Italy", "France", "Spain", "Germany"]
print(Europe_places)
sorted_places = sorted(Europe_places)
print(sorted_places)
print(Europe_places)
Europe_places.reverse()
print(Europe_places)
Europe_places.reverse()
print(Europe_places)
Europe_places.sort()
print(Europe_places)
Europe_places.sort(reverse=True)
print(Europe_places)

print("3-10")
print(dinner_guest_list)
print (f"I'm inviting {len(dinner_guest_list)} for dinner because i won't have my big table in taime to host a bigger one")

print("3-11")
Balloon_colors=[]
print(Balloon_colors[-1])
