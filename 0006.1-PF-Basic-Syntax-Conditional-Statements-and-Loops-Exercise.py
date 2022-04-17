# 1. Jenny's Secret Message
# command_name = input()
# if command_name != "Johnny":
#     print(f"Hello, {command_name}!")
# else:
#     print(f"Hello, my love!")

# 2. Drink Something
# command_age = int(input())
# if command_age <= 14:
#     print("drink toddy")
# elif 14 < command_age <= 18:
#     print("drink coke")
# elif 18 < command_age <= 21:
#     print("drink beer")
# elif 21 < command_age:
#     print("drink whisky")

# 3. Leonardo DiCaprio Oscars
# command_oscar = int(input())
# if command_oscar == 88:
#     print(f"Leo finally won the Oscar! Leo is happy")
# elif command_oscar == 86:
#     print(f"Not even for Wolf of Wall Street?!")
# elif command_oscar < 88:
#     print(f"When will you give Leo an Oscar?")
# elif command_oscar > 88:
#     print(f"Leo got one already!")

# 4. Double Char
# command_string = input()
# doubled_char = ""
# for i in range (0, len(command_string), 1):
#     doubled_char += command_string[i] * 2
# print(doubled_char)

# 5. Can't Sleep? Count Sheep
# command_num = int(input())
# for i in range(1, command_num+1):
#     print(str(i) + " sheep...", end="")

# 6. Next Happy Year
# command_year = int(input())+1
# while len(set(str(command_year))) != len(str(command_year)):
#     command_year += 1
# print(command_year)

# 7. Maximum Multiple
# command_divisor = int(input())
# command_bound = int(input())
# for i in range(1, command_bound+1, 1):
#     if i % command_divisor == 0:
#         list_numbers = [i]
# print(max(list_numbers))

# 8. Mutate Strings
# command_first_string = input()
# command_second_string = input()
# first_string_list = []
# second_string_list = []
# check_word = command_first_string
# for i in range(0, len(command_first_string)):
#     first_string_list += command_first_string[i]
# for j in range(0, len(command_second_string)):
#     second_string_list += command_second_string[j]
# for k in range(0, len(command_first_string)):
#     first_string_list[k] = second_string_list[k]
#     if "".join(first_string_list) != check_word:
#         print("".join(first_string_list))
#         check_word = "".join(first_string_list)

# 9. Easter Cozonacs
# command_budget = float(input())
# command_kg_flour_price = float(input())
# one_pack_egg_price = command_kg_flour_price * 0.75
# quarter_liter_milk_price = (command_kg_flour_price * 1.25) / 4
# total_price_one_cozonac = command_kg_flour_price + one_pack_egg_price + quarter_liter_milk_price
# left_budget = command_budget
# egg_count = 0
# turn_count = 0
# while total_price_one_cozonac < left_budget:
#     turn_count += 1
#     left_budget = command_budget - total_price_one_cozonac * turn_count
#     egg_count = egg_count + 3
#     if turn_count % 3 == 0:
#         egg_count = egg_count - (turn_count - 2)
# print(f"You made {turn_count} cozonacs! Now you have {egg_count} eggs and {left_budget:.2f}BGN left.")

# 10. Christmas Spirit
command_quantity = int(input())
command_days = int(input())
ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
total_cost = 0
total_spirit = 0
for days_passed in range(1, command_days + 1):
    if days_passed % 11 == 0:
        command_quantity += 2
    if days_passed % 15 == 0:
        total_spirit += 30
    if days_passed % 10 == 0:
        total_spirit -= 20
        total_cost += tree_skirt + tree_lights + tree_garlands
        if days_passed == command_days:
            total_spirit -= 30
    if days_passed % 5 == 0:
        total_spirit += 17
        total_cost += tree_lights * command_quantity
    if days_passed % 3 == 0:
        total_spirit += 13
        total_cost += (tree_skirt + tree_garlands) * command_quantity
    if days_passed % 2 == 0:
        total_spirit += 5
        total_cost += ornament_set * command_quantity
print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
