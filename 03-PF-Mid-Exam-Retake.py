# 01. Counter Strike
# initial_energy = int(input())
# distance = input()
# battle_won = 0
# is_live = True
# while distance != "End of battle":
#     if initial_energy - int(distance) >= 0:
#         initial_energy -= int(distance)
#         battle_won += 1
#         if battle_won % 3 == 0:
#             initial_energy += battle_won
#     else:
#         print(f"Not enough energy! Game ends with {battle_won} won battles and {initial_energy} energy")
#         is_live = False
#         break
#     distance = input()
# if is_live:
#     print(f"Won battles: {battle_won}. Energy left: {initial_energy}")

# 02. Shoot for the Win
# targets_list = input().split(" ")
# for i in range(len(targets_list)):
#     targets_list[i] = int(targets_list[i])
# command_entry = input()
# while command_entry != "End":
#     index_number = int(command_entry)
#     if index_number <= len(targets_list) - 1:
#         if targets_list[index_number] != -1:
#             check_number = targets_list[index_number]
#             targets_list[index_number] = -1
#             for j in range(len(targets_list)):
#                 if targets_list[j] != -1:
#                     if targets_list[j] <= check_number:
#                         targets_list[j] = targets_list[j] + check_number
#                     else:
#                         targets_list[j] = targets_list[j] - check_number
#     command_entry = input()
# print(f"Shot targets: {len([i for i in targets_list if i == -1])} -> ", end="")
# print(*targets_list, sep=" ")

# 03. Moving Target
targets_list = [int(i) for i in input().split(" ")]
command_input = input()
while command_input != "End":
    command = command_input.split(" ")[0]

    if command == "Shoot":
        index = int(command_input.split(" ")[1])
        power = int(command_input.split(" ")[2])

        if 0 <= index <= len(targets_list) - 1:
            targets_list[index] -= power

            if targets_list[index] <= 0:
                targets_list.remove(targets_list[index])

    if command == "Add":
        index = int(command_input.split(" ")[1])
        value = int(command_input.split(" ")[2])

        if 0 <= index <= len(targets_list) - 1:
            targets_list.insert(index, value)
        else:
            print(f"Invalid placement!")

    if command == "Strike":
        index = int(command_input.split(" ")[1])
        radius = int(command_input.split(" ")[2])

        if index + radius < len(targets_list) and index - radius >= 0:
            del targets_list[index - radius:index + radius + 1]
        else:
            print(f"Strike missed!")

    command_input = input()

print(*targets_list, sep="|")
