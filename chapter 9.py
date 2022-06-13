class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"餐馆{self.restaurant_name}是一家{self.cuisine_type}餐厅")

    def open_restaurant(self):
        print(f"{self.cuisine_type}正在营业中")


restaurant = Restaurant('麦当劳', '快餐厅')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name}是一家{self.cuisine_type}餐厅")

    def open_restaurant(self):
        print(f"{self.cuisine_type}正在营业中")


restaurant = Restaurant('肯德基', '快餐')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('西贝', '西北')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant = Restaurant('沙县', '路边摊')
restaurant.describe_restaurant()
restaurant.open_restaurant()


# 9-3
class User:
    def __init__(self, firstname, lastname, sexual, motherland):
        self.firstname = firstname
        self.lastname = lastname
        self.sexual = sexual
        self.motherland = motherland

    def describe_user(self):
        print(f"{self.firstname}"
              f"{self.lastname}"
              f"{self.sexual}"
              f"{self.motherland} ")

    def greet_user(self):
        print(f"hello {self.firstname} {self.lastname}")


user1 = User('binbin', 'zheng', 'nan', 'zhongguo')
user1.describe_user()
user1.greet_user()


# 9-4
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name}是一家{self.cuisine_type}餐厅")

    def open_restaurant(self):
        print(f"{self.cuisine_type}正在营业中")

    def set_number_served(self):
        print(f"已用餐{self.served}人")

    def update_number_served(self, update_number):
        self.served = update_number

    def increment_number_served(self, increment_number):
        self.served += increment_number


# noinspection NonAsciiCharacters
肯德基 = Restaurant('肯德基', '快餐')
肯德基.describe_restaurant()
肯德基.open_restaurant()
肯德基.update_number_served(30)
肯德基.set_number_served()
肯德基.increment_number_served(50)
肯德基.set_number_served()

西贝 = Restaurant('西贝', '西北')
西贝.describe_restaurant()
西贝.open_restaurant()
西贝.update_number_served(60)
西贝.set_number_served()

沙县 = Restaurant('沙县', '路边摊')
沙县.describe_restaurant()
沙县.open_restaurant()
沙县.update_number_served(70)
沙县.set_number_served()


# 9-5
class User:
    def __init__(self, firstname, lastname, sexual, motherland):
        self.firstname = firstname
        self.lastname = lastname
        self.sexual = sexual
        self.motherland = motherland
        self.login_attempts = 1

    def describe_user(self):
        print(f"{self.firstname}"
              f"{self.lastname}"
              f"{self.sexual}"
              f"{self.motherland} ")

    def greet_user(self):
        print(f"hello {self.firstname} {self.lastname}")

    def increment_login_attempts(self, ila):
        self.login_attempts += ila

    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('binbin', 'zheng', 'nan', 'zhongguo')
for i in range(5):
    user1.increment_login_attempts(1)
    print(user1.login_attempts)
user1.reset_login_attempts()
print(f"{user1.login_attempts}")

# 9-6 冰激凌小站
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name}是一家{self.cuisine_type}餐厅")

    def open_restaurant(self):
        print(f"{self.cuisine_type}正在营业中")

    def set_number_served(self):
        print(f"已用餐{self.served}人")

    def update_number_served(self, update_number):
        self.served = update_number

    def increment_number_served(self, increment_number):
        self.served += increment_number

class IceCreamStand(Restaurant):
    """冰激凌站作为Restaurant的子类"""
    def __init__(self,restaurant_name, cuisine_type = '冰激凌小店'):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = []

    def describe_flavors(self):
        for self.flavor in self.flavors:
            print(f"{self.flavor}")

icecreamstand1 = IceCreamStand('icecreamstand1')
icecreamstand1.flavors = ['flavor1','flavor2','flavor3']
icecreamstand1.describe_flavors()

