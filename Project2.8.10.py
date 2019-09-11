"""Functions Try it Yourself 8-12 - 8-14"""
# 8-12 Sandwiches
print("\n8-12 Sandwiches")


def sandwich_filling(*fillings):
    print("\nThis sandwich has the following filling/s: ")
    for filling in fillings:
        print("\t-" + filling)


sandwich_filling('cheese', 'lettuce', 'beef patty')
sandwich_filling('egg', 'mayo')
sandwich_filling('potato', 'ketchup', 'mayo', 'chicken')

# 8-13 User Profile
print("\nUser Profile")


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='pasig city', field='engineering',
                             horoscope='pisces')
print(user_profile)

# 8-13 Cars
print("\nCars")


def make_car(manufacturer, model_name, **car_info):
    car_profile = {}
    car_profile['manufacturer'] = manufacturer
    car_profile['model_name'] = model_name
    for key, value in car_info.items():
        car_profile[key] = value
    return car_profile


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
