"""Classes Try it Yourself 9-4 - 9-5"""
# 9-4 Number Served
print("\n9-4 Number Served")


class Restaurant:
    """Make a Restaurant Profile"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initiate Restaurant Name and Cuisine Type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe and print the name of the Restaurant"""
        print("\nThe name of the restaurant is " + self.restaurant_name.title() + ".")
        print("This restaurant specializes in " + self.cuisine_type.title() + " cuisine.")

    def open_restaurant(self):
        """Tell user that the restaurant is open"""
        print(self.restaurant_name.title() + " is open.")

    def set_number_served(self, customers):
        """Set the number of customers that have been served."""
        self.number_served = customers

    def increment_number_served(self, customer_served_today):
        """Increments the number of customers who've been  served"""
        self.number_served += customer_served_today


restaurant = Restaurant("chilis", "american")
print(restaurant.restaurant_name.title() + " has served " + str(restaurant.number_served) + " customers.")
restaurant.number_served = 500
print(restaurant.restaurant_name.title() + " has served " + str(restaurant.number_served) + " customers.")
restaurant.set_number_served(300)
print(restaurant.restaurant_name.title() + " has served " + str(restaurant.number_served) + " customers.")
restaurant.increment_number_served(400)
print(restaurant.restaurant_name.title() + " has served " + str(restaurant.number_served) + " customers.")

# 9-5 Login Attempts
print("\n9-5 Login Attempts")


class User:
    """Make a User Profile"""

    def __init__(self, first_name, last_name, age, gender):
        """"Initiate User first name, last name, age and gender"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user profile"""
        print("\nProfile: " + self.first_name.title() + " " + self.last_name.title())
        print("Age: " + str(self.age))
        print("Gender: " + self.gender.title())

    def greet_user(self):
        """Print a personalized greeting to the user"""
        print("Hi " + self.first_name.title() + "! How are you today?")

    def increment_login_attempts(self):
        """Increments the number of login attempts by the user"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0"""
        self.login_attempts = 0


user_0 = User("orly", "revalo", 28, "male")
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
user_0.increment_login_attempts()
print("You have attempted to login " + str(user_0.login_attempts) + " times.")
user_0.reset_login_attempts()
print("You have attempted to login " + str(user_0.login_attempts) + " times.")
