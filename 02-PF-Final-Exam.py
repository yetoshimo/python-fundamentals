# 01. World Tour
# given_string = input()
# command_manipulate = input()
# while command_manipulate != "Travel":
#     command = command_manipulate.split(":")[0]
#
#     if command == "Add Stop":
#         index = int(command_manipulate.split(":")[1])
#         string = command_manipulate.split(":")[2]
#
#         if 0 <= index < len(given_string):
#             given_string = given_string[:index] + string + given_string[index:]
#
#         print(given_string)
#
#     elif command == "Remove Stop":
#         start_index = int(command_manipulate.split(":")[1])
#         end_index = int(command_manipulate.split(":")[2])
#
#         if 0 <= start_index < len(given_string) and 0 <= end_index < len(given_string):
#             given_string = given_string[:start_index] + given_string[end_index+1:]
#
#         print(given_string)
#
#     elif command == "Switch":
#         old_string = command_manipulate.split(":")[1]
#         new_string = command_manipulate.split(":")[2]
#
#         if old_string in given_string:
#             given_string = given_string.replace(old_string, new_string)
#
#         print(given_string)
#
#     else:
#         print(given_string)
#
#     command_manipulate = input()
#
# print(f"Ready for world tour! Planned stops: {given_string}")

# 02. Destination Mapper
# from re import findall
#
# regex = r"([=|/])([A-Z][A-Za-z]{2,})\1"
# matches = findall(regex, input())
# places = []
# total_points = 0
#
# for (identifier, match) in matches:
#     places.append(match)
#     total_points += len(match)
#
# print(f"Destinations: {', '.join(places)}")
# print(f"Travel Points: {total_points}")

# 03. Plant Discovery
class Plant:
    def __init__(self, plant_name, rarity):
        self.plant_name = plant_name
        self.rarity = rarity
        self.ratings = []

    def rating_avg(self):
        if self.ratings:
            return sum(self.ratings) / len(self.ratings)
        return 0


plants = {}

number = int(input())
for i in range(number):
    token = input().split("<->")
    plant_name = token[0]
    plant_rarity = int(token[1])

    plants[plant_name] = Plant(plant_name, plant_rarity)

input_command = input()

while input_command != "Exhibition":
    token_2 = input_command.split(": ")
    token_3 = token_2[1].split(" - ")

    plant_name = token_3[0]
    command_type = token_2[0]

    if plant_name not in plants:
        print("error")

    elif command_type == "Rate":
        rating = int(token_3[1])

        plants[plant_name].ratings.append(rating)

    elif command_type == "Update":
        new_rarity = int(token_3[1])

        plants[plant_name].rarity = new_rarity

    elif command_type == "Reset":
        plants[plant_name].ratings.clear()

    else:
        print("error")

    input_command = input()

sorted_plants = sorted(plants.values(), key=lambda p: (p.rarity, p.rating_avg()), reverse=True)

print(f"Plants for the exhibition:")
for plant in sorted_plants:
    print(f"- {plant.plant_name}; Rarity: {plant.rarity}; Rating: {plant.rating_avg():.2f}")
