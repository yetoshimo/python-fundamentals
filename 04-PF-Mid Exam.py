# 01. National Court
# employee_one = int(input())
# employee_two = int(input())
# employee_three = int(input())
# per_hour_answered = employee_one + employee_two + employee_three
# time_passed = 0
# total_people = int(input())
# while total_people > 0:
#     time_passed += 1
#     if time_passed % 4 == 0:
#         continue
#     else:
#         total_people -= per_hour_answered
# print(f"Time needed: {time_passed}h.")

# 02. Shopping List
# groceries_list = input().split("!")
# command_string = input()
# while command_string != "Go Shopping!":
#     command_string.split(" ")
#     to_do_command = command_string.split(" ")[0]
#     if to_do_command == "Urgent":
#         to_do_item = command_string.split(" ")[1]
#         if to_do_item not in groceries_list:
#             groceries_list.insert(0, to_do_item)
#     elif to_do_command == "Unnecessary":
#         to_do_item = command_string.split(" ")[1]
#         if to_do_item in groceries_list:
#             groceries_list.remove(to_do_item)
#     elif to_do_command == "Correct":
#         old_item = command_string.split(" ")[1]
#         new_item = command_string.split(" ")[2]
#         if old_item in groceries_list:
#             groceries_list[groceries_list.index(old_item)] = new_item
#     elif to_do_command == "Rearrange":
#         to_do_item = command_string.split(" ")[1]
#         if to_do_item in groceries_list:
#             groceries_list.remove(to_do_item)
#             groceries_list.append(to_do_item)
#     command_string = input()
# print(", ".join(groceries_list))

# 03. Heart Delivery
neighborhood = input().split("@")
house_index = 0
for i in range(len(neighborhood)):
    neighborhood[i] = int(neighborhood[i])
commands = input()
while commands != "Love!":
    length_to_jump = int(commands.split(" ")[1])
    house_index += length_to_jump
    # house_index = house_index % len(neighborhood)
    if house_index > len(neighborhood) - 1:
        house_index = 0
    if neighborhood[house_index] >= 2:
        neighborhood[house_index] -= 2
        if neighborhood[house_index] <= 0:
            print(f"Place {house_index} has Valentine's day.")
    elif neighborhood[house_index] == 0:
        print(f"Place {house_index} already had Valentine's day.")
    commands = input()
print(f"Cupid's last position was {house_index}.")
if sum(neighborhood) == 0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {sum(map(lambda x: x > 0, neighborhood))} places.")
