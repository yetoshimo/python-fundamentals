# 01. Problem
# input_string = input()
#
# input_command = input()
#
# while input_command != "End":
#     command = input_command.split()[0]
#
#     if command == "Translate":
#         character = input_command.split()[1]
#         replacement = input_command.split()[2]
#
#         input_string = input_string.replace(character, replacement)
#
#         print(input_string)
#
#     if command == "Includes":
#         string = input_command.split()[1]
#
#         if string in input_string:
#             print(f"True")
#         else:
#             print(f"False")
#
#     if command == "Start":
#         string = input_command.split()[1]
#
#         if input_string.split()[0] == string:
#             print(f"True")
#         else:
#             print(f"False")
#
#     if command == "Lowercase":
#         input_string = input_string.lower()
#
#         print(input_string)
#
#     if command == "FindIndex":
#         character = input_command.split()[1]
#
#         for char in range(len(input_string)):
#             if input_string[char] == character:
#                 last_index = char
#
#         print(last_index)
#
#     if command == "Remove":
#         start_index = int(input_command.split()[1])
#         count = int(input_command.split()[2])
#
#         input_string = input_string[:start_index] + input_string[start_index + count:]
#
#         print(input_string)
#
#     input_command = input()

# 02. Problem
# from re import findall
#
# n_lines = int(input())
#
# regex = r"([\*|@])(?P<tag_name>[A-Z][a-z]{2,})\1[:][\s](\[(?P<message1>[A-Za-z]*)\])\|(\[(?P<message2>[A-Za-z]*)\])\|(\[(?P<message3>[A-Za-z]*)\])\|$"
#
# for _ in range(n_lines):
#     input_command = input()
#
#     matches = findall(regex, input_command)
#
#     if matches:
#         print(f"{matches[0][1]}: {ord(matches[0][3])} {ord(matches[0][5])} {ord(matches[0][7])}")
#     else:
#         print(f"Valid message not found!")

# from re import finditer
#
# n_lines = int(input())
#
# regex = r"([\*|@])(?P<tag_name>[A-Z][a-z]{2,})\1[:][\s](\[(?P<message1>[A-Za-z]*)\])\|(\[(?P<message2>[A-Za-z]*)\])\|(\[(?P<message3>[A-Za-z]*)\])\|$"
#
# for _ in range(n_lines):
#     input_command = input()
#
#     matches = finditer(regex, input_command)
#     found = False
#
#     for item in matches:
#         found = True
#         print(f"{item.group('tag_name')}: {ord(item.group('message1'))} {ord(item.group('message2'))} {ord(item.group('message3'))}")
#     if not found:
#         print(f"Valid message not found!")

# 03. Problem
class Users:
    def __init__(self, user_name, send_messages, received_messages):
        self.user_name = user_name
        self.send_messages = send_messages
        self.received_messages = received_messages


capacity = int(input())

input_command = input()

users_dictionary = {}

while input_command != "Statistics":
    command = input_command.split("=")[0]

    if command == "Add":
        username = input_command.split("=")[1]
        sent = int(input_command.split("=")[2])
        received = int(input_command.split("=")[3])

        if username not in users_dictionary:
            users_dictionary[username] = Users(username, sent, received)

    if command == "Message":
        sender = input_command.split("=")[1]
        receiver = input_command.split("=")[2]

        if sender in users_dictionary and receiver in users_dictionary:
            users_dictionary[sender].send_messages += 1
            users_dictionary[receiver].received_messages += 1

            if users_dictionary[sender].send_messages + users_dictionary[sender].received_messages >= capacity:
                print(f"{sender} reached the capacity!")
                users_dictionary.pop(sender)

            if users_dictionary[receiver].send_messages + users_dictionary[receiver].received_messages >= capacity:
                print(f"{receiver} reached the capacity!")
                users_dictionary.pop(receiver)

    if command == "Empty":
        username = input_command.split("=")[1]

        if username in users_dictionary:
            users_dictionary.pop(username)
        elif username == "All":
            users_dictionary.clear()

    input_command = input()

print(f"Users count: {len(users_dictionary)}")
for value in sorted(users_dictionary.values(), key=lambda kv: (-kv.received_messages, kv.user_name)):
    print(f"{value.user_name} - {value.send_messages + value.received_messages}")
