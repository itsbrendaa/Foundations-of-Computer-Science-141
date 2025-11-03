print("hey world its brenda")

print('9-1')

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

restaurant = Restaurant("AYCE Diner", "American")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

print("9-2")
restaurant1 = Restaurant("La Bella Vita", "Italian")
restaurant2 = Restaurant("Sakura Sushi", "Japanese")
restaurant3 = Restaurant("Spice House", "Indian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

print('9-3')
class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"User Profile:")
        print(f"  Name: {self.first_name} {self.last_name}")
        print(f"  Age: {self.age}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back!")

user1 = User("Alice", "kouam", 28, "alice.k@example.com", "New York")
user2 = User("Brian", "Smith", 34, "brian.smith@example.com", "Chicago")
user3 = User("Clara", "Lopez", 22, "clara.lopez@example.com", "Los Angeles")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

print('9-4')
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        """Set the number of customers served to a specific value."""
        if number >= 0:
            self.number_served = number
        else:
            print("Number served cannot be negative.")

    def increment_number_served(self, number):
        """Increment the number of customers served."""
        if number > 0:
            self.number_served += number
        else:
            print("Increment must be positive.")

restaurant = Restaurant("Sunset Diner", "American")

print(f"Customers served: {restaurant.number_served}")

restaurant.number_served = 25
print(f"Customers served (updated directly): {restaurant.number_served}")

restaurant.set_number_served(100)
print(f"Customers served (set method): {restaurant.number_served}")

restaurant.increment_number_served(30)
print(f"Customers served after increment: {restaurant.number_served}")

print("9-5")
class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
        self.login_attempts = 0 

    def describe_user(self):
        print(f"User Profile:")
        print(f"  Name: {self.first_name} {self.last_name}")
        print(f"  Age: {self.age}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back!")

    def increment_login_attempts(self):
        """Increase the number of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0


user1 = User("Alice", "Johnson", 28, "alice.j@example.com", "New York")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(f"Login attempts: {user1.login_attempts}")

user1.reset_login_attempts()
print(f"Login attempts after reset: {user1.login_attempts}")

print("9-6")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Chip"]

    def display_flavors(self):
        print(f"{self.restaurant_name} offers the following flavors:")
        for flavor in self.flavors:
            print(f" - {flavor}")

ice_cream_stand = IceCreamStand("Frosty Treats")
ice_cream_stand.display_flavors()

print("9-7")

class Admin(User):
    def __init__(self, first_name, last_name, age, email, location):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]

    def show_privileges(self):
        print(f"Admin privileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")

admin_user = Admin("Daniel", "Stone", 40, "daniel.admin@example.com", "Houston")
admin_user.describe_user()
admin_user.show_privileges()


print("Exercise 9-8")

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = ["can add post", "can delete post", "can ban user"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")

class AdminWithPrivileges(User):
    def __init__(self, first_name, last_name, age, email, location):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = Privileges()

admin2 = AdminWithPrivileges("Emma", "Green", 35, "emma.admin@example.com", "Boston")
admin2.privileges.show_privileges()

print("9-9")

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        return f"{self.year} {self.make} {self.model}".title()

class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("Battery is already at maximum capacity.")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('Tesla', 'Model 3', 2025)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

print("9-10")

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

        
print("9-11")

class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = ["can add post", "can delete post", "can ban user"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, email, location):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = Privileges()

print("9-12")

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = ["can add post", "can delete post", "can ban user"]
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("Privileges:")
        for privilege in self.privileges:
            print(f" - {privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age, email, location):
        super().__init__(first_name, last_name, age, email, location)
        self.privileges = Privileges()

print("9-13")
import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Return a random number between 1 and the number of sides."""
        return random.randint(1, self.sides)

die_6 = Die()
print("Rolling a 6-sided die 10 times:")
for i in range(10):
    print(die_6.roll_die(), end=" ")
print("\n")

die_10 = Die(10)
print("Rolling a 10-sided die 10 times:")
for i in range(10):
    print(die_10.roll_die(), end=" ")
print("\n")

die_20 = Die(20)
print("Rolling a 20-sided die 10 times:")
for i in range(10):
    print(die_20.roll_die(), end=" ")
print("\n")


print("9-14")

lottery_pool = [str(n) for n in range(10)] + ['A', 'B', 'C', 'D', 'E']

winning_ticket = random.sample(lottery_pool, 4)

print(f"Lottery Pool: {lottery_pool}")
print(f"Winning combination: {' '.join(winning_ticket)}")
print("Any ticket matching these 4 symbols wins a prize!")


print("9-15")

my_ticket = ['A', '3', '7', 'B']

tries = 0
while True:
    tries += 1
    draw = random.sample(lottery_pool, 4)
    if draw == my_ticket:
        break

print(f"Your ticket: {my_ticket}")
print(f"It took {tries} draws to win the lottery!")