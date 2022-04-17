# 1. Integer Operations
# from math import floor
# command_number_one = int(input())
# command_number_two = int(input())
# command_number_three = int(input())
# command_number_four = int(input())
# calculated_number = floor((command_number_one + command_number_two) / command_number_three) * command_number_four
# print(f"{calculated_number:.0f}")

# 2. Chars to String
# command_char_one = input()
# command_char_two = input()
# command_char_three = input()
# print(f"{command_char_one}{command_char_two}{command_char_three}")

# 3. Elevator
# from math import ceil
# command_people = int(input())
# command_capacity = int(input())
# rounds = ceil(command_people / command_capacity)
# print(rounds)

# 4. Sum of Chars
# command_interval = int(input())
# ascii_sum = 0
# for i in range(0, command_interval):
#     command_letter = input()
#     ascii_sum += ord(command_letter)
# print(f"The sum equals: {ascii_sum}")

# 5. Print Part of the ASCII Table
# command_first_index = int(input())
# command_second_index = int(input())
# for i in range(command_first_index, command_second_index+1):
#     print(f"{chr(i)} ", end="")

# 6. Triples of Latin Letters
# command_triplet_start = int(input())
# for i in range(0, command_triplet_start):
#     for j in range(0, command_triplet_start):
#         for k in range(0, command_triplet_start):
#             print(f"{chr(97 + i)}{chr(97 + j)}{chr(97 + k)}")

# 7. Water Overflow
# command_intervals = int(input())
# total_water_in_tank = 0
# for i in range(0, command_intervals):
#     command_bucket_capacity = int(input())
#     total_water_in_tank += command_bucket_capacity
#     if total_water_in_tank <= 255:
#         pass
#     elif total_water_in_tank > 255:
#         total_water_in_tank -= command_bucket_capacity
#         print(f"Insufficient capacity!")
# print(f"{total_water_in_tank}")

# 8. Party Profit
# from math import floor
# command_party_size = int(input())
# command_days = int(input())
# total_party_size = command_party_size
# total_coins = 0
# for i in range(1, command_days+1):
#     if i % 15 == 0:
#         total_party_size += 5
#     if i % 10 == 0:
#         total_party_size -= 2
#     total_coins += 50 - (2 * total_party_size)
#     if i % 15 == 0:
#         total_coins -= total_party_size * 2
#     if i % 5 == 0:
#         total_coins += total_party_size * 20
#     if i % 3 == 0:
#         total_coins -= total_party_size * 3
# print(f"{total_party_size} companions received {floor(total_coins/total_party_size)} coins each.")

# 9. Snowballs
# command_number_of_snowballs = int(input())
# snowball_value_list = []
# key_list = []
# snowball_dictionary = {}
# value_dictionary = {}
# highest_value = 0
# for i in range(1, command_number_of_snowballs+1):
#     snowball_snow = int(input())
#     snowball_time = int(input())
#     snowball_quality = int(input())
#     snowball_value = round((snowball_snow / snowball_time) ** snowball_quality)
#     snowball_value_list.append(snowball_value)
#     snowball_dictionary[i] = (snowball_snow, snowball_time, snowball_value, snowball_quality)
#     key_list.append(i)
#     value_dictionary[i] = (snowball_value)
#     value_list = list(value_dictionary.values())
# highest_value = max(value_list)
# highest_snow = list(snowball_dictionary[key_list[value_list.index(highest_value)]])[0]
# highest_time = list(snowball_dictionary[key_list[value_list.index(highest_value)]])[1]
# highest_quality = list(snowball_dictionary[key_list[value_list.index(highest_value)]])[3]
# print(f"{highest_snow} : {highest_time} = {highest_value} ({highest_quality})")

# 10. Gladiator Expenses
command_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
expenses = 0
shield_counter = 0
for i in range(1, command_lost_fights + 1):
    if i % 6 == 0:
        expenses += sword_price + helmet_price + shield_price
        shield_counter += 1
    if shield_counter == 2:
        expenses += armor_price
        shield_counter = 0
    if i % 3 == 0 and i % 6 != 0:
        expenses += sword_price
    if i % 2 == 0 and i % 6 != 0:
        expenses += helmet_price
print(f"Gladiator expenses: {expenses:.2f} aureus")
