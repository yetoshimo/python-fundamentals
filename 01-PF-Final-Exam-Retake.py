# 01. The Imitation Game
# encrypted_message = list(input())
# instruction = input()
# while instruction != "Decode":
#     command = instruction.split("|")[0]
#
#     if command == "Move":
#         number_of_letters = int(instruction.split("|")[1])
#
#         to_append = "".join(encrypted_message)[0:number_of_letters]
#
#         left_letters = "".join(encrypted_message)[number_of_letters:]
#
#         encrypted_message = list(left_letters + to_append)
#
#     if command == "Insert":
#         index = int(instruction.split("|")[1])
#         value = instruction.split("|")[2]
#
#         encrypted_message.insert(index, value)
#
#     if command == "ChangeAll":
#         substring = instruction.split("|")[1]
#         replacement = instruction.split("|")[2]
#
#         encrypted_message = list("".join(encrypted_message).replace(substring, replacement))
#
#     instruction = input()
#
# print(f"The decrypted message is: {''.join(encrypted_message)}")

# 02. Ad Astra
# from re import findall
# input_string = input()
# total_calories = 0
# DAILY_CAL = 2000
# regex = r"(#|\|)([A-Za-z\s]+)\1([\d]{2}/[\d]{2}/[\d]{2})\1([\d]{1,5})\1"
# matches = findall(regex, input_string)
# for match in matches:
#     total_calories += int(match[3])
#
# print(f"You have food to last you for: {total_calories // DAILY_CAL} days!")
# for match in matches:
#     print(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")

# 03. The Pianist
my_list = {}
number_of_pieces = int(input())
for i in range(number_of_pieces):
    piece_info = input()
    my_list[piece_info.split("|")[0]] = [piece_info.split("|")[1], piece_info.split("|")[2]]
piece_info = input()
while piece_info != "Stop":
    command = piece_info.split("|")[0]

    if command == "Add":
        piece = piece_info.split("|")[1]
        composer = piece_info.split("|")[2]
        key = piece_info.split("|")[3]

        if piece in my_list:
            print(f"{piece} is already in the collection!")
        else:
            print(f"{piece} by {composer} in {key} added to the collection!")
            my_list[piece] = [composer, key]

    if command == "Remove":
        piece = piece_info.split("|")[1]

        if piece in my_list:
            print(f"Successfully removed {piece}!")
            my_list.pop(piece)
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    if command == "ChangeKey":
        piece = piece_info.split("|")[1]
        new_key = piece_info.split("|")[2]

        if piece in my_list:
            print(f"Changed the key of {piece} to {new_key}!")
            my_list[piece][1] = new_key
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    piece_info = input()

for piece, (composer, key) in sorted(my_list.items()):
    print(f"{piece} -> Composer: {composer}, Key: {key}")
