# 1. Which Are In?
# first_list = input().split(", ")
# second_list = input().split(", ")
# third_list = []
# for i in range(0, len(first_list)):
#     for j in range(0, len(second_list)):
#         if first_list[i] in second_list[j] and first_list[i] not in third_list:
#             third_list.append(first_list[i])
# print(third_list)
# first_list = input().split(", ")
# second_list = input().split(", ")
# third_list = [i for i in first_list for j in second_list if i in j]
# print(sorted(set(third_list), key=third_list.index))

# 2. Big Numbers Lover
# input_string = input().split(" ")
# input_string.sort(reverse=True)
# print("".join(input_string))

# 3. Next Version
# initial_version = input().split(".")
# next_version_number = int("".join(initial_version)) + 1
# next_version_string = [str(i) for i in str(next_version_number)]
# print(".".join(next_version_string))

# 4. Office Chairs
# number_of_rooms = int(input())
# seats_left = 0
# enough_seats = True
# for i in range(0, number_of_rooms):
#     room_setup = input().split(" ")
#     existing_chairs = [str(i) for i in room_setup[0]]
#     available_seats = int(len(existing_chairs))
#     # print(available_seats)
#     seats_to_be_taken = int(room_setup[1])
#     # print(seats_to_be_taken)
#     if seats_to_be_taken <= available_seats:
#         seats_left += (available_seats - seats_to_be_taken)
#     else:
#         print(f"{abs(available_seats - seats_to_be_taken)} more chairs needed in room {i + 1}")
#         enough_seats = False
# if enough_seats:
#     print(f"Game On, {seats_left} free chairs left")

# 5. Electron Distribution
# number_of_electrons = int(input())
# electron_distribution = []
# if 0 < number_of_electrons <= 2:
#     electron_distribution.append(number_of_electrons)
#     print(electron_distribution)
# else:
#     electron_distribution.append(2)
#     number_of_electrons -= 2
#     ring_level = 2
#     while number_of_electrons > 0:
#         if number_of_electrons >= 2 * (ring_level ** 2):
#             electron_distribution.append(2 * (ring_level ** 2))
#             number_of_electrons -= 2 * (ring_level ** 2)
#             ring_level += 1
#         else:
#             electron_distribution.append(number_of_electrons)
#             break
# print(electron_distribution)

# 6. Group of 10's
# from collections import defaultdict
# numbers_list = input().split(", ")
# numbers_list = [int(i) for i in numbers_list]
# numbers_dictionary = defaultdict(list)
# for i in numbers_list:
#     if i % 10 != 0:
#         numbers_dictionary[(i // 10) + 1].append(i)
#     elif i % 10 == 0:
#         numbers_dictionary[(i // 10)].append(i)
# for j in range(1, max(numbers_dictionary.keys()) + 1):
#     if j in numbers_dictionary.keys():
#         print(f"Group of {j * 10}'s: {numbers_dictionary[j]}")
#     else:
#         print(f"Group of {j * 10}'s: []")

# 7. Decipher This!
# encrypted_string = input().split(" ")
# for i in range(len(encrypted_string)):
#     item_elements = list(encrypted_string[i])
#     if item_elements[2].isdigit():
#         item_integer = item_elements[:3]
#         item_integer = "".join(item_integer)
#         item_integer = int(item_integer)
#         item_string = item_elements[3:]
#     else:
#         item_integer = item_elements[:2]
#         item_integer = "".join(item_integer)
#         item_integer = int(item_integer)
#         item_string = item_elements[2:]
#     switch_letter = item_string[len(item_string) - 1]
#     item_string[len(item_string) - 1] = item_string[0]
#     item_string[0] = switch_letter
#     encrypted_string[i] = chr(item_integer) + "".join(item_string)
# print(" ".join(encrypted_string))

# 8. Moving Target
# target_sequence = [int(i) for i in input().split(" ")]
# command_input = input().split(" ")
# while command_input[0] != "End":
#     command_type = command_input[0]
#     if command_type == "Shoot":  # index # power
#         target_index = int(command_input[1])
#         shot_power = int(command_input[2])
#         if 0 <= target_index < len(target_sequence):
#             target_sequence[target_index] -= shot_power
#             if target_sequence[target_index] <= 0:
#                 target_sequence.pop(target_index)
#         # print(target_sequence)  # CONTROL
#         command_input = input().split(" ")
#     if command_type == "Add":  # index # value
#         target_index = int(command_input[1])
#         target_value = int(command_input[2])
#         if 0 <= target_index < len(target_sequence):
#             target_sequence.insert(target_index, target_value)
#         else:
#             print(f"Invalid placement!")
#         # print(target_sequence)  # CONTROL
#         command_input = input().split(" ")
#     if command_type == "Strike":  # index # radius
#         target_index = int(command_input[1])
#         radius = int(command_input[2])
#         start_index = target_index - radius
#         end_index = target_index + radius
#         if 0 <= start_index and end_index < len(target_sequence):
#             del target_sequence[start_index:end_index + 1]
#         else:
#             print("Strike missed!")
#         # print(target_sequence)  # CONTROL
#         command_input = input().split(" ")
# target_sequence = [str(i) for i in target_sequence]
# print("|".join(target_sequence))

# 9. Heart Delivery
# neighborhood = [int(i) for i in input().split("@")]
# jump_command = input().split(" ")
# current_position = 0
# while jump_command[0] != "Love!":
#     jump_length = int(jump_command[1])
#     if 0 <= current_position <= len(neighborhood) - 1:
#         current_position += jump_length
#         if current_position > len(neighborhood) - 1:
#             current_position = 0
#         if neighborhood[current_position] == 0:
#             print(f"Place {current_position} already had Valentine's day.")
#         else:
#             neighborhood[current_position] -= 2
#             if neighborhood[current_position] == 0:
#                 print(f"Place {current_position} has Valentine's day.")
#         jump_command = input().split(" ")
# print(f"Cupid's last position was {current_position}.")
# if sum(neighborhood) == 0:
#     print(f"Mission was successful.")
# else:
#     print(f"Cupid has failed {len([i for i in neighborhood if i > 0])} places.")

# 10. Inventory
collecting_items = [i for i in input().split(", ")]
action_string = input().split(" - ")
while action_string[0] != "Craft!":
    action = action_string[0]
    if action == "Collect" and action_string[1] not in collecting_items:
        collecting_items.append(action_string[1])
        # print(f"Collect {collecting_items}")  # CONTROL
        action_string = input().split(" - ")
    elif action == "Drop" and action_string[1] in collecting_items:
        collecting_items.remove(action_string[1])
        # print(f"Drop {collecting_items}")  # CONTROL
        action_string = input().split(" - ")
    elif action == "Combine Items":
        items_to_combine = action_string[1].split(":")
        old_item = items_to_combine[0]
        new_item = items_to_combine[1]
        if old_item in collecting_items:
            collecting_items.insert(collecting_items.index(old_item) + 1, new_item)
            # print(f"Combine {collecting_items}")  # CONTROL
        action_string = input().split(" - ")
    elif action == "Renew" and action_string[1] in collecting_items:
        collecting_items.append(action_string[1])
        collecting_items.remove(action_string[1])
        # print(f"Renew {collecting_items}")  # CONTROL
        action_string = input().split(" - ")
    else:
        action_string = input().split(" - ")
print(", ".join(collecting_items))
