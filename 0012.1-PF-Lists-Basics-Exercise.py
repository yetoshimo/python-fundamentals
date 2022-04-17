# 1. Invert Values
# command_string_input = input()
# list_of_string = command_string_input.split(" ")
# for i in range(0, len(list_of_string)):
#     list_of_string[i] = -1 * int(list_of_string[i])
# print(list_of_string)

# 2. Multiples List
# command_factor = int(input())
# command_count = int(input())
# list_of_multiples = []
# for i in range(1, command_count+1):
#     list_of_multiples.append(i * command_factor)
# print(list_of_multiples)

# 3. Football Cards
# command_card_order = input()
# list_of_players = command_card_order.split(" ")
# clear_list = list(dict.fromkeys(list_of_players))
# a_team_players = 11
# b_team_players = 11
# for i in range(0, len(clear_list)):
#     player = clear_list[i]
#     if "A" in player:
#         a_team_players -= 1
#     if "B" in player:
#         b_team_players -= 1
#     if a_team_players < 7 or b_team_players < 7:
#         print(f"Team A - {a_team_players}; Team B - {b_team_players}")
#         print("Game was terminated")
#         break
# if a_team_players >= 7 and b_team_players >= 7:
#     print(f"Team A - {a_team_players}; Team B - {b_team_players}")

# 4. Number Beggars
# command_number_string = input()
# string_of_numbers = command_number_string.split(", ")
# list_of_numbers = []
# list_of_earnings = []
# for i in range(0, len(string_of_numbers)):
#     list_of_numbers.append(int(string_of_numbers[i]))
# command_number_of_beggars = int(input())
# for j in range(0, command_number_of_beggars):
#     list_of_earnings.append(sum(list_of_numbers[j:len(list_of_numbers):command_number_of_beggars]))
# print(list_of_earnings)

# 5. Faro Shuffle
# command_input_string = input()
# list_of_strings = command_input_string.split(" ")
# first_half = []
# second_half = []
# shuffled_list = list_of_strings
# command_number_of_shuffles = int(input())
# for i in range(0, command_number_of_shuffles):
#     first_half = shuffled_list[:len(shuffled_list)//2]
#     second_half = shuffled_list[len(shuffled_list)//2:]
#     shuffled_list = [c for pair in zip(first_half, second_half) for c in pair]
# print(shuffled_list)

# 6. Survival of the Biggest
# command_input_string = input()
# string_of_numbers = command_input_string.split(" ")
# list_of_numbers = []
# for i in range(0, len(string_of_numbers)):
#     list_of_numbers.append(int(string_of_numbers[i]))
# command_input_remove = int(input())
# for j in range(0, command_input_remove):
#     smallest_number = min(list_of_numbers)
#     list_of_numbers.remove(smallest_number)
# print(list_of_numbers)

# 7. Easter Gifts
# names_of_gifts = input()
# list_of_gifts = names_of_gifts.split(" ")
# command_input = input()
# while command_input != "No Money":
#     list_of_command = command_input.split(" ")
#     if "OutOfStock" in list_of_command:
#         gift_name = list_of_command[1]
#         while gift_name in list_of_gifts:
#             index_number = list_of_gifts.index(gift_name)
#             list_of_gifts[index_number] = "None"
#     if "Required" in list_of_command and 0 <= int(list_of_command[2]) <= len(list_of_gifts)-1:
#         gift_name = list_of_command[1]
#         gift_index = int(list_of_command[2])
#         list_of_gifts[gift_index] = gift_name
#     if "JustInCase" in list_of_command:
#         gift_name = list_of_command[1]
#         list_of_gifts[len(list_of_gifts)-1] = gift_name
#     command_input = input()
# while "None" in list_of_gifts:
#     list_of_gifts.remove("None")
# print(*list_of_gifts, sep=" ")

# 8. Seize the Fire
# fire_with_their_cells = input()
# separated_cells = fire_with_their_cells.split("#")
# water_amount = int(input())
# put_out_cells = []
# effort = 0
# total_fire = 0
# for i in range(0, len(separated_cells)):
#     element = separated_cells[i]
#     if "High" in element:
#         fire_value = element.split("High = ")
#         fire_range = int(fire_value[1])
#         if 81 <= fire_range <= 125 and 0 <= fire_range <= water_amount:
#             put_out_cells.append(fire_range)
#             effort += fire_range * 0.25
#             total_fire += fire_range
#             water_amount -= fire_range
#     if "Medium" in element:
#         fire_value = element.split("Medium = ")
#         fire_range = int(fire_value[1])
#         if 51 <= fire_range <= 80 and 0 <= fire_range <= water_amount:
#             put_out_cells.append(fire_range)
#             effort += fire_range * 0.25
#             total_fire += fire_range
#             water_amount -= fire_range
#     if "Low" in element:
#         fire_value = element.split("Low = ")
#         fire_range = int(fire_value[1])
#         if 1 <= fire_range <= 50 and 0 <= fire_range <= water_amount:
#             put_out_cells.append(fire_range)
#             effort += fire_range * 0.25
#             total_fire += fire_range
#             water_amount -= fire_range
# print(f"Cells:")
# for i in range(0, len(put_out_cells)):
#     print(f" - {put_out_cells[i]}")
# print(f"Effort: {effort:.2f}")
# print(f"Total Fire: {total_fire}")

# 9. Hello, France
# items_with_their_prices = input()
# separated_items = items_with_their_prices.split("|")
# budget = float(input())
# individual_price = 0
# profit_total = 0
# increased_prices = []
# for i in range(0, len(separated_items)):
#     element = separated_items[i]
#     individual_item = element.split("->")
#     individual_item_name = individual_item[0]
#     individual_price = float(individual_item[1])
#     if budget - individual_price >= 0:
#         if (individual_item_name == "Clothes" and individual_price <= 50) \
#                 or (individual_item_name == "Shoes" and individual_price <= 35) \
#                 or (individual_item_name == "Accessories" and individual_price <= 20.50):
#             budget -= individual_price
#             increased_prices.append(individual_price * 1.4)
#             profit_total += individual_price * 0.4
# for j in range(0, len(increased_prices)):
#     print(f"{(increased_prices[j]):.2f}", end=" ")
# print()
# print(f"Profit: {profit_total:.2f}")
# if budget + sum(increased_prices) >= 150:
#     print("Hello, France!")
# else:
#     print("Time to go.")

# 10. Bread Factory
events = input().split("|")
energy_level = 100
max_energy = 100
gained_energy = 0
total_coins = 100
element = ""
bankrupt = False
for item in events:
    element = item.split("-")
    action = element[0]
    magnitude = int(element[1])
    if action == "rest":
        if energy_level == 100:
            print(f"You gained 0 energy.")
        elif energy_level < 100:
            energy_level += magnitude
            if energy_level > 100:
                gained_energy = energy_level - max_energy
                energy_level = 100
                print(f"You gained {magnitude - gained_energy} energy.")
            else:
                print(f"You gained {magnitude} energy.")
        print(f"Current energy: {energy_level}.")
    elif action == "order":
        if (energy_level - 30) >= 0:
            print(f"You earned {magnitude} coins.")
            total_coins += magnitude
            energy_level -= 30
        else:
            print(f"You had to rest!")
            energy_level += 50
    else:
        if (total_coins - magnitude) > 0:
            print(f"You bought {action}.")
            total_coins -= magnitude
        else:
            print(f"Closed! Cannot afford {action}.")
            bankrupt = True
            break
if not bankrupt:
    print(f"Day completed!\nCoins: {total_coins}\nEnergy: {energy_level}")
