# 01. Activation Keys
# activation_key = input()
# operation_name = input()
# while operation_name != "Generate":
#     command = operation_name.split(">>>")[0]
#
#     if command == "Contains":
#         substring = operation_name.split(">>>")[1]
#
#         if substring in activation_key:
#             print(f"{activation_key} contains {substring}")
#         else:
#             print(f"Substring not found!")
#
#     if command == "Flip":
#         upper_lower = operation_name.split(">>>")[1]
#         start_index = int(operation_name.split(">>>")[2])
#         end_index = int(operation_name.split(">>>")[3])
#
#         to_flip = activation_key[start_index:end_index]
#
#         if upper_lower == "Upper":
#             to_upper_flip = to_flip.upper()
#             activation_key = activation_key.replace(to_flip, to_upper_flip)
#         else:
#             to_lower_flip = to_flip.lower()
#             activation_key = activation_key.replace(to_flip, to_lower_flip)
#
#         print(activation_key)
#
#     if command == "Slice":
#         start_index = int(operation_name.split(">>>")[1])
#         end_index = int(operation_name.split(">>>")[2])
#
#         to_slice = activation_key[start_index:end_index]
#
#         activation_key = activation_key.replace(to_slice, "", 1)
#
#         print(activation_key)
#
#     operation_name = input()
#
# print(f"Your activation key is: {activation_key}")

# 02. Emoji Detector
# from re import findall
# input_text = input()
# regex_cools = r"([:]{2}|[\*]{2})([A-Z][a-z]{2,})\1"
# matches_cools = findall(regex_cools, input_text)
# emoji_list = [i for i in matches_cools]
#
# regex_digits = r"([\d])"
# matches_digits = findall(regex_digits, input_text)
# cool_threshold_list = [int(i) for i in matches_digits]
# cool_threshold = cool_threshold_list[0]
# for i in range(1, len(cool_threshold_list)):
#     cool_threshold = cool_threshold * cool_threshold_list[i]
#
# print(f"Cool threshold: {cool_threshold}")
#
# print(f"{len(emoji_list)} emojis found in the text. The cool ones are:")
#
# for i in emoji_list:
#     emoji_coolness = 0
#     for j in i[1]:
#         emoji_coolness += ord(j)
#     if emoji_coolness > cool_threshold:
#         print(i[0] + i[1] + i[0])

# 03. P!rates
class City:
    def __init__(self, city_name, population, gold):
        self.city_name = city_name
        self.population = population
        self.gold = gold


city_dictionary = {}
target_cities = input()
while target_cities != "Sail":
    name = target_cities.split("||")[0]
    total_population = int(target_cities.split("||")[1])
    gold_amount = int(target_cities.split("||")[2])

    if name not in city_dictionary:
        city_dictionary[name] = City(name, total_population, gold_amount)
    else:
        city_dictionary[name].population += total_population
        city_dictionary[name].gold += gold_amount

    target_cities = input()

event_input = input()
while event_input != "End":
    command = event_input.split("=>")[0]

    if command == "Plunder":
        town = event_input.split("=>")[1]
        people = int(event_input.split("=>")[2])
        gold_quantity = int(event_input.split("=>")[3])

        print(f"{town} plundered! {gold_quantity} gold stolen, {people} citizens killed.")

        city_dictionary[town].population -= people

        if city_dictionary[town].population == 0:
            city_dictionary.pop(town)
            print(f"{town} has been wiped off the map!")

        if town in city_dictionary:
            city_dictionary[town].gold -= gold_quantity

            if city_dictionary[town].gold == 0:
                print(f"{town} has been wiped off the map!")
                city_dictionary.pop(town)

    if command == "Prosper":
        town = event_input.split("=>")[1]
        gold_quantity = int(event_input.split("=>")[2])

        if gold_quantity < 0:
            print(f"Gold added cannot be a negative number!")
        else:
            city_dictionary[town].gold += gold_quantity
            print(f"{gold_quantity} gold added to the city treasury. {town} now has {city_dictionary[town].gold} gold.")

    event_input = input()

sorted_city_dictionary = sorted(city_dictionary.values(), key=lambda kv: (-kv.gold, kv.city_name))

print(f"Ahoy, Captain! There are {len(sorted_city_dictionary)} wealthy settlements to go to:")
if len(sorted_city_dictionary) > 0:
    for i in sorted_city_dictionary:
        print(f"{i.city_name} -> Population: {i.population} citizens, Gold: {i.gold} kg")
else:
    print(f"Ahoy, Captain! All targets have been plundered and destroyed!")
