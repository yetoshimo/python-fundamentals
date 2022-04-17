# 1. Comment
# class Comment:
#     def __init__(self, username, content, likes = 0):
#         self.username = username
#         self.content = content
#         self.likes = likes

# comment = Comment("user1", "I like this book")
# print(comment.username)
# print(comment.content)
# print(comment.likes)


# 2. Party
# class Party:
#     def __init__(self):
#         self.people = []
#
#
# party = Party()
# line = input()
# while line != "End":
#     party.people.append(line)
#     line = input()
# print(f"Going: {', '.join(party.people)}")
# print(f"Total: {len(party.people)}")

# 3. Email
# class Email:
#     def __init__(self, sender, receiver, content, is_sent = False):
#         self.sender = sender
#         self.receiver = receiver
#         self.content = content
#         self.is_sent = False
#
#     def send(self):
#         self.is_sent = True
#
#     def get_info(self):
#         return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
#
#
# emails = []
# line = input().split(" ")
# while line[0] != "Stop":
#     sender = line[0]
#     receiver = line[1]
#     content = line[2]
#     email = Email(sender, receiver, content)
#     emails.append(email)
#     line = input().split(" ")
#
# sent_emails = (int(i) for i in input().split(", "))
#
# for x in sent_emails:
#     emails[x].send()
#
# for email in emails:
#     print(email.get_info())

# # 4. Zoo
# class Zoo:
#     __animals = 0
#
#     def __init__(self, name):
#         self.name = name
#         self.mammals = []
#         self.fishes = []
#         self.birds = []
#
#     def add_animal(self, species, name):
#         if species == "mammal":
#             self.mammals.append(name)
#         if species == "fish":
#             self.fishes.append(name)
#         if species == "bird":
#             self.birds.append(name)
#
#         Zoo.__animals += 1
#
#     def get_info(self, species):
#         result = ""
#         if species == "mammal":
#             result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
#         elif species == "fish":
#             result += f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
#         elif species == "bird":
#             result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
#
#         result += f"Total animals: {Zoo.__animals}"
#         return result
#
#
# zoo_name = input()
# zoo = Zoo(zoo_name)
# count = int(input())
# for i in range(count):
#     animal = input().split(" ")
#     species = animal[0]
#     name = animal[1]
#     zoo.add_animal(species, name)
#
# info = input()
# print(zoo.get_info(info))

# 5. Circle
class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        return 2 * Circle.__pi * self.diameter / 2

    def calculate_area(self):
        return Circle.__pi * (self.diameter / 2) ** 2

    def calculate_area_of_sector(self, angle):
        return Circle.calculate_area(self) * (angle / 360)


circle = Circle(10)
angle = 5
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
