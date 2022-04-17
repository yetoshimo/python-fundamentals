# 01. Bonus Scoring System
# count_of_students = int(input())
# count_of_lectures = int(input())
# initial_bonus = int(input())
# attendance_list = []
# bonus_list = []
# for i in range(count_of_students):
#     attendance_list.append(int(input()))
# # {total bonus} = {student attendances} / {course lectures} * (5 + {additional bonus})
# for j in attendance_list:
#     total_bonus = j / count_of_lectures * (5 + initial_bonus)
#     bonus_list.append(total_bonus)
# if bonus_list:
#     print(f"Max Bonus: {max(bonus_list):.0f}.")
#     print(f"The student has attended {attendance_list[bonus_list.index(max(bonus_list))]} lectures.")
# else:
#     print(f"Max Bonus: {0}.")
#     print(f"The student has attended {0} lectures.")

# 02. MuOnline
# dungeon_rooms = input().split("|")
# MAX_HEALTH = 100
# health = MAX_HEALTH
# bitcoins = 0
# best_room = 0
# for i in dungeon_rooms:
#     best_room += 1
#     command = i.split(" ")[0]
#     number = int(i.split(" ")[1])
#
#     if command == "potion":
#         if health + number > MAX_HEALTH:
#             number = MAX_HEALTH - health
#             health = MAX_HEALTH
#
#         else:
#             health += number
#         print(f"You healed for {number} hp.")
#         print(f"Current health: {health} hp.")
#
#     elif command == "chest":
#         print(f"You found {number} bitcoins.")
#         bitcoins += number
#
#     else:
#         health -= number
#         if health > 0:
#             print(f"You slayed {command}.")
#
#         else:
#             print(f"You died! Killed by {command}.")
#             print(f"Best room: {best_room}")
#             break
#
# if health > 0:
#     print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")

# 03. Inventory
collecting_items = input().split(", ")
different_commands = input()
while different_commands != "Craft!":
    command = different_commands.split(" - ")[0]
    if command == "Collect":
        item = different_commands.split(" - ")[1]
        if item not in collecting_items:
            collecting_items.append(item)
    elif command == "Drop":
        item = different_commands.split(" - ")[1]
        if item in collecting_items:
            collecting_items.remove(item)
    elif command == "Combine Items":
        old_item = different_commands.split(" - ")[1].split(":")[0]
        if old_item in collecting_items:
            new_item = different_commands.split(" - ")[1].split(":")[1]
            collecting_items.insert(collecting_items.index(old_item) + 1, new_item)
    elif command == "Renew":
        item = different_commands.split(" - ")[1]
        if item in collecting_items:
            collecting_items.remove(item)
            collecting_items.append(item)
    different_commands = input()
print(", ".join(collecting_items))
