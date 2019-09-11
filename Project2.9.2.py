"""Classes: Try it Yourself 9-1 - 9-3"""
# 9.1 Restaurant
print("\n9.1 Restaurant")


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


restaurant = Restaurant("buffalo wings", "american & portuguese")
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9.2 Three Restaurants
print("\n9.2 Three Restaurants")

restaurant_A = Restaurant("chilis", "american")
restaurant_B = Restaurant("mang juan", "filipino")
restaurant_C = Restaurant("old spaghetti house", "italian")

restaurant_A.describe_restaurant()
restaurant_B.describe_restaurant()
restaurant_C.describe_restaurant()

# 9.3 Users
print("\n9.3 Users")


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


user_0 = User("orly", "revalo", 28, "male")
user_1 = User("Juan", "dela cruz", 33, "male")
user_2 = User("alodia", "gosiegnfiao", 30, "female")

user_0.describe_user()
user_0.greet_user()
user_1.describe_user()
user_1.greet_user()
user_2.describe_user()
user_2.greet_user()


