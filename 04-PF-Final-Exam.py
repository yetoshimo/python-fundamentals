# 01. Password Reset
# input_string = input()
# execute_command = input()
# new_password = ""
# substring = ""
# take_odd_length = len(input_string)
# while execute_command != "Done":
#
#     command = execute_command.split(" ")[0]
#
#     if command == "TakeOdd":
#         new_password = input_string[1:take_odd_length:2]
#         # for i in range(take_odd_length):
#         #     if i % 2 != 0:
#         #         new_password += input_string[i]
#
#         if new_password != "":
#             input_string = new_password
#
#         print(input_string)
#
#     if command == "Cut":
#         index = int(execute_command.split(" ")[1])
#         length = int(execute_command.split(" ")[2])
#
#         substring = input_string[index:index + length]
#
#         input_string = input_string.replace(substring, "", 1)
#
#         print(input_string)
#
#     if command == "Substitute":
#         substring = execute_command.split(" ")[1]
#         substitute = execute_command.split(" ")[2]
#
#         if substring in input_string:
#             input_string = input_string.replace(substring, substitute)
#             print(input_string)
#         else:
#             print(f"Nothing to replace!")
#
#     execute_command = input()
#
# print(f"Your password is: {input_string}")

# 02. Fancy Barcodes
# from re import findall
# number_of_barcodes = int(input())
# for i in range(number_of_barcodes):
#     product_group = ""
#     input_barcode = input()
#
#     regex_barcode = r"(@[#]+)([A-Z][A-Za-z0-9]{4,}[A-Z])(@[#]+)"
#     matches = findall(regex_barcode, input_barcode)
#
#     if matches:
#         product = matches[0][1]
#
#         regex_group = r"([\d*])"
#         group_match = findall(regex_group, product)
#
#         if group_match:
#             for j in group_match:
#                 product_group += j
#         else:
#             product_group = "00"
#
#         print(f"Product group: {product_group}")
#
#     else:
#         print(f"Invalid barcode")

# 03. Heroes of Code and Logic VII
class Hero:
    def __init__(self, hero_name, health_point, mana_point):
        self.hero_name = hero_name
        self.health_point = health_point
        self.mana_point = mana_point


MAX_HEALTH = 100
MAX_MANA = 200

heroes_dictionary = {}
number_of_heroes = int(input())
for i in range(number_of_heroes):
    selected_hero = input().split(" ")
    hero_name = selected_hero[0]
    health = int(selected_hero[1])
    mana = int(selected_hero[2])

    heroes_dictionary[hero_name] = Hero(hero_name, health, mana)

input_command = input()
while input_command != "End":
    command = input_command.split(" - ")[0]

    if command == "CastSpell":
        hero_name = input_command.split(" - ")[1]
        mana_needed = int(input_command.split(" - ")[2])
        spell_name = input_command.split(" - ")[3]

        if heroes_dictionary[hero_name].mana_point >= mana_needed:
            heroes_dictionary[hero_name].mana_point -= mana_needed
            print(
                f"{hero_name} has successfully cast {spell_name} and now has {heroes_dictionary[hero_name].mana_point} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    if command == "TakeDamage":
        hero_name = input_command.split(" - ")[1]
        damage = int(input_command.split(" - ")[2])
        attacker = input_command.split(" - ")[3]

        heroes_dictionary[hero_name].health_point -= damage

        if heroes_dictionary[hero_name].health_point > 0:
            print(
                f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes_dictionary[hero_name].health_point} HP left!")
        else:
            heroes_dictionary.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")

    if command == "Recharge":
        hero_name = input_command.split(" - ")[1]
        mana_points = int(input_command.split(" - ")[2])

        if mana_points <= MAX_MANA - heroes_dictionary[hero_name].mana_point:
            heroes_dictionary[hero_name].mana_point += mana_points
            print(f"{hero_name} recharged for {mana_points} MP!")
        else:
            mana_points = MAX_MANA - heroes_dictionary[hero_name].mana_point
            heroes_dictionary[hero_name].mana_point = MAX_MANA
            print(f"{hero_name} recharged for {mana_points} MP!")

    if command == "Heal":
        hero_name = input_command.split(" - ")[1]
        health_points = int(input_command.split(" - ")[2])

        if health_points <= MAX_HEALTH - heroes_dictionary[hero_name].health_point:
            heroes_dictionary[hero_name].health_point += health_points
            print(f"{hero_name} healed for {health_points} HP!")
        else:
            health_points = MAX_HEALTH - heroes_dictionary[hero_name].health_point
            heroes_dictionary[hero_name].health_point = MAX_HEALTH
            print(f"{hero_name} healed for {health_points} HP!")

    input_command = input()

sorted_hero_dictionary = sorted(heroes_dictionary.values(), key=lambda kv: (-kv.health_point, kv.hero_name))

for i in sorted_hero_dictionary:
    print(i.hero_name)
    print(f"  HP: {i.health_point}")
    print(f"  MP: {i.mana_point}")
