# # 1. Storage
# class Storage:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.storage = []
#
#     def add_product(self, product):
#         if len(self.storage) < self.capacity:
#             self.storage.append(product)
#
#     def get_products(self):
#         return self.storage
#
#
# storage = Storage(4)
# storage.add_product("apple")
# storage.add_product("banana")
# storage.add_product("potato")
# storage.add_product("tomato")
# storage.add_product("bread")
# print(storage.get_products())

# 2. Weapon
# class Weapon:
#     def __init__(self, bullets):
#         self.bullets = bullets
#
#     def shoot(self):
#         if self.bullets > 0:
#             self.bullets -= 1
#             return f"shooting..."
#         elif self.bullets <= 0:
#             return f"no bullets left"
#             return print(weapon)
#
#     def __repr__(self):
#         return f"Remaining bullets: {self.bullets}"
#
#
# weapon = Weapon(5)
# weapon.shoot()
# weapon.shoot()
# weapon.shoot()
# weapon.shoot()
# weapon.shoot()
# weapon.shoot()
# print(weapon)

# 3. Catalogue
# class Catalogue:
#     def __init__(self, name):
#         self.name = name
#         self.products = []
#
#     def add_product(self, product):
#         self.products.append(product)
#
#     def get_by_letter(self, first_letter):
#         return [i for i in self.products if i[0].lower() == first_letter.lower()]
#
#     def __repr__(self):
#         new_line = "\n"
#         return f"Items in the {self.name} catalogue:\n{f'{new_line}'.join(sorted(self.products, key=str.lower))}"
#
#
# catalogue = Catalogue("Furniture")
# catalogue.add_product("Sofa")
# catalogue.add_product("Mirror")
# catalogue.add_product("Desk")
# catalogue.add_product("Chair")
# catalogue.add_product("Carpet")
# print(catalogue.get_by_letter("c"))
# print(catalogue)

# 4. Town
# class Town:
#     def __init__(self, name):
#         self.name = name
#
#     def set_latitude(self, latitude):
#         self.latitude = latitude
#
#     def set_longitude(self, longitude):
#         self.longitude = longitude
#
#     def __repr__(self):
#         return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"
#
#
# town = Town("Sofia")
# town.set_latitude("42° 41\' 51.04\" N")
# town.set_longitude("23° 19\' 26.94\" E")
# print(town)

# 5. Class
# class Class:
#     __students_count = 22
#
#     def __init__(self, name):
#         self.name = name
#         self.students = []
#         self.grades = []
#
#     def add_student(self, name, grade):
#         if Class.__students_count > 0:
#             Class.__students_count -= 1
#             self.students.append(name)
#             self.grades.append(float(grade))
#
#     def get_average_grade(self):
#         if len(self.grades) == 0:
#             return 0
#         else:
#             return round(sum(self.grades)/len(self.grades), 2)
#
#     def __repr__(self):
#         return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"

#
# a_class = Class("11B")
# a_class.add_student("Peter", 4.8)
# a_class.add_student("George", 6.00)
# a_class.add_student("Amy", 3.50)
# print(a_class)


# 6. Inventory
# class Inventory:
#     def __init__(self, capacity):
#         self.__capacity = capacity
#         self.counter = self.__capacity
#         self.items = []
#
#     def add_item(self, item):
#         if self.counter > 0:
#             self.counter -= 1
#             self.items.append(item)
#         else:
#             return f"not enough room in the inventory"
#
#     def get_capacity(self):
#         return self.__capacity
#
#     def __repr__(self):
#         return f"Items: {', '.join(self.items)}.\nCapacity left: {self.counter}"
#
#
# inventory = Inventory(2)
# inventory.add_item("potion")
# inventory.add_item("sword")
# print(inventory.add_item("bottle"))
# print(inventory.get_capacity())
# print(inventory)

# 7. Articles
# class Article:
#     def __init__(self, title, content, author):
#         self.title = title
#         self.content = content
#         self.author = author
#
#     def edit(self, new_content):
#         self.content = new_content
#
#     def change_author(self, new_author):
#         self.author = new_author
#
#     def rename(self, new_title):
#         self.title = new_title
#
#     def __repr__(self):
#         return f"{self.title} - {self.content}: {self.author}"
#
#
# article = Article("some title", "some content", "some author")
# article.edit("new content")
# article.rename("new title")
# article.change_author("new author")
# print(article)

# 8. Vehicle
# class Vehicle:
#     def __init__(self, type, model, price, owner=None):
#         self.type = type
#         self.model = model
#         self.price = price
#         self.owner = owner
#
#     def buy(self, money, potential_owner):
#         if money >= self.price and self.owner is None:
#             self.owner = potential_owner
#             return f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"
#         elif money < self.price:  # and self.owner is None:
#             return f"Sorry, not enough money"
#         elif money >= self.price and self.owner is not None:
#             return f"Car already sold"
#
#     def sell(self):
#         if self.owner is not None:
#             self.owner = None
#         else:
#             return "Vehicle has no owner"
#
#     def __repr__(self):
#         if self.owner is not None:
#             return f"{self.model} {self.type} is owned by: {self.owner}"
#         else:
#             return f"{self.model} {self.type} is on sale: {self.price}"


# vehicle_type = "car"
# model = "BMW"
# price = 30000
# vehicle = Vehicle(vehicle_type, model, price)
# vehicle.buy(-15000, "Peter")
# vehicle.buy(35000, "George")
# print(vehicle)
# vehicle.sell()
# print(vehicle)


# # 9. Movie
class Movie:
    __watched_movies = 0

    def __init__(self, name, director, watched=False):
        self.name = name
        self.director = director
        self.watched = watched

    def change_name(self, new_name):
        self.name = new_name

    def change_director(self, new_director):
        self.director = new_director

    def watch(self):
        if not self.watched:
            self.watched = True
            Movie.__watched_movies += 1
        else:
            pass

    def __repr__(self):
        return f"Movie name: {self.name}; Movie director: {self.director}. Total watched movies: {Movie.__watched_movies}"


first_movie = Movie("Inception", "Christopher Nolan")
second_movie = Movie("The Matrix", "The Wachowskis")
third_movie = Movie("The Predator", "Shane Black")
first_movie.change_director("Me")
third_movie.change_name("My Movie")
first_movie.watch()
third_movie.watch()
first_movie.watch()
print(first_movie)
print(second_movie)
print(third_movie)
