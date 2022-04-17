# 01. Problem
# needed_experience = float(input())
# count_of_battles = int(input())
# gathered_experience = 0
# is_gained = False
# for i in range(1, count_of_battles + 1):
#     experience_gained = float(input())
#
#     if i % 3 == 0 and i % 5 != 0:
#         gathered_experience += experience_gained * 1.15
#
#     elif i % 5 == 0 and i % 3 != 0:
#         gathered_experience += experience_gained * 0.9
#
#     elif i % 15 == 0:
#         gathered_experience += experience_gained * 1.05
#
#     else:
#         gathered_experience += experience_gained
#
#     if gathered_experience >= needed_experience:
#         print(f"Player successfully collected his needed experience for {i} battles.")
#         is_gained = True
#         break
#
# if not is_gained:
#     print(f"Player was not able to collect the needed experience, {needed_experience - gathered_experience:.2f} more needed.")

# 02. Problem
# series_of_strings = [i for i in input().split()]
# command_input = input()
# while command_input != "end":
#     command = command_input.split()[0]
#
#     if command == "reverse":
#         start_index = int(command_input.split()[2])
#         count = int(command_input.split()[4])
#
#         reversed_list = series_of_strings[start_index:(start_index + count)]
#
#         for i in range(count):
#             series_of_strings.pop(start_index)
#
#         for j in reversed_list:
#             series_of_strings.insert(start_index, j)
#
#     if command == "sort":
#         start_index = int(command_input.split()[2])
#         count = int(command_input.split()[4])
#
#         reversed_list = sorted(series_of_strings[start_index:(start_index + count)], reverse=True)
#
#         for i in range(count):
#             series_of_strings.pop(start_index)
#
#         for j in reversed_list:
#             series_of_strings.insert(start_index, j)
#
#     if command == "remove":
#         count = int(command_input.split()[1])
#
#         del series_of_strings[0:count]
#
#     command_input = input()
#
# print(", ".join(series_of_strings))

# 03. Problem
command_input = input()
chat_list = []

while command_input != "end":
    command = command_input.split()[0]

    if command == "Chat":
        chat_list.append(command_input.split()[1])

    if command == "Delete":
        message_to_delete = command_input.split()[1]

        if message_to_delete in chat_list:
            chat_list.remove(message_to_delete)

    if command == "Edit":
        old_message = command_input.split()[1]
        new_message = command_input.split()[2]

        chat_list[chat_list.index(old_message)] = new_message

    if command == "Pin":
        chat_list.remove(command_input.split()[1])
        chat_list.append(command_input.split()[1])

    if command == "Spam":
        spam_message = command_input.split()
        spam_message.remove(command)

        for i in spam_message:
            chat_list.append(i)

    command_input = input()

print("\n".join(chat_list))
