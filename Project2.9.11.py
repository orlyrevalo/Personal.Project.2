"""Classes Try it Yourself 9-6 - 9-9"""

# 9-6 Ice Cream Stand
print("\nIce Cream Stand")


class Restaurant:
    """Make a Restaurant Profile"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initiate Restaurant Name and Cuisine Type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Describe and print the name of the Restaurant"""
        print("\nThe name of the restaurant is " + self.restaurant_name.title() + ".")
        print("This restaurant specializes in " + self.cuisine_type.title() + " cuisine.")

    def open_restaurant(self):
        """Tell user that the restaurant is open"""
        print(self.restaurant_name.title() + " is open.")


# restaurant = Restaurant("buffalo wings", "american & portuguese")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()


class IceCreamStand(Restaurant):  # Inherits the attributes from Parent Class "Restaurant"
    """Attempt to represent an Ice Cream Stand"""

    def __init__(self, restaurant_name, cuisine_name, flavors):
        """Initialize the attributes of an Ice Cream Stand"""
        super().__init__(restaurant_name, cuisine_name)
        self.flavors = flavors

    def display_flavors(self):
        """Print all the flavors the Ice Cream Stand offers"""
        print("These are flavors offered in this Ice Cream Stand:")
        for flavor in self.flavors:
            print(flavor.title())


list_of_flavors = ["chocolate", "strawberry", "banana"]
restaurant1 = IceCreamStand("Dairy King", "Dairy and Ice Cream", list_of_flavors)
restaurant1.display_flavors()

# 9-7 Admin
print("\n9.7 Admin")


class User:
    """Make a User Profile"""

    def __init__(self, first_name, last_name, age, gender):
        """"Initiate User first name, last name, age and gender"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        """Print a summary of the user profile"""
        print("\nProfile: " + self.first_name.title() + " " + self.last_name.title())
        print("Age: " + str(self.age))
        print("Gender: " + self.gender.title())

    def greet_user(self):
        """Print a personalized greeting to the user"""
        print("Hi " + self.first_name.title() + "! How are you today?")


class Admin(User):
    """Make a Admin User and Inherit attributes from class "User" """

    def __init__(self, first_name,  last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = ["can delete posts", "can ban user", "can add post"]

    def show_privileges(self):
        """Print all the privileges of the admin"""
        print("Since your an admin " + self.first_name.title() + ", You have the following privileges: ")
        for privilege in self.privileges:
            print("You " + privilege + ".")


user_0 = Admin("orly", "revalo", 28, "male")
user_0.show_privileges()

# 9-8 Privileges
print("\n9.8 Privileges")


class User:
    """Make a User Profile"""
    def __init__(self, first_name, last_name, age, gender):
        """"Initiate User first name, last name, age and gender"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def describe_user(self):
        """Print a summary of the user profile"""
        print("\nProfile: " + self.first_name.title() + " " + self.last_name.title())
        print("Age: " + str(self.age))
        print("Gender: " + self.gender.title())

    def greet_user(self):
        """Print a personalized greeting to the user"""
        print("Hi " + self.first_name.title() + "! How are you today?")


class Privileges:
    """Make a Privilege Class"""
    def __init__(self, first_name):
        """Initialize the privileges attributes"""
        self.privileges = ["can delete posts", "can ban user", "can add post"]
        self.first_name = first_name

    def show_privileges(self):
        """Print all the privileges of the admin"""
        print("Since your an admin, " + self.first_name + ", you have the following privileges: ")
        for privilege in self.privileges:
            print("You " + privilege + ".")


class Admin(User):
    """Make an Admin User and Inherit attributes from class "User" """
    def __init__(self, first_name,  last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = Privileges(self.first_name)


user_1 = Admin("Juan", "dela cruz", 33, "male")
user_1.privileges.show_privileges()

# 9-9 Battery Upgrade
print("\n9.9 Battery Upgrade")


class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # Initial value is set to 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print  a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """ Print a statment about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        """Upgrades the battery"""
        self.battery_size = 85


class ElectricCar(Car):
    """ Represent aspects of a car, specific to electric vehicles """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()  # Called a class for an attribute

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print("This car has a " + str(self.battery) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

