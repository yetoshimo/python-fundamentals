# 1. Valid Usernames
# usernames = input().split(", ")
# is_length = False
# is_symbol = False
#
# for i in usernames:
#
#     if 3 <= len(i) <= 16:
#         is_length = True
#
#     if is_length:
#         valid_username = i
#         for j in i:
#             if j.isdigit():
#                 i = i.replace(j, "")
#             if j.isalpha():
#                 i = i.replace(j, "")
#             if "-" in i:
#                 i = i.replace("-", "")
#             if "_" in i:
#                 i = i.replace("_", "")
#             if len(i) == 0:
#                 is_symbol = True
#
#     if is_length and is_symbol:
#         print(valid_username)
#         is_length = False
#         is_symbol = False

# 2. Character Multiplier
# two_strings = input().split(" ")
# counter = 0
# total_sum = 0
# first_word = list(two_strings[0])
# second_word = list(two_strings[1])
# if len(two_strings[0]) > len(two_strings[1]):  # first word is longer
#     counter = len(two_strings[1])
#     for i in range(counter):
#         total_sum += ord(first_word[i]) * ord(second_word[i])
#     for j in range(counter, len(first_word)):
#         total_sum += ord(first_word[j])
#
# else:  # second word is longer
#     counter = len(two_strings[0])
#     for i in range(counter):
#         total_sum += ord(first_word[i]) * ord(second_word[i])
#     for j in range(counter, len(second_word)):
#         total_sum += ord(second_word[j])
#
# print(total_sum)

# 3. Extract File
# path = input()
# extension = path[path.find(".") + 1:]
# filename = path[len(path) - path[::-1].find("\\"):path.find(".")]
# print(f"File name: {filename}")
# print(f"File extension: {extension}")

# 4. Caesar Cipher
# input_word = input()
# encrypted_word = ""
# for i in input_word:
#     encrypted_word += chr(ord(i) + 3)
# print(encrypted_word)

# 5. Emoticon Finder
# emoticon_string = input()
# emoticon_symbol = ""
# for i in range(len(emoticon_string)):
#     if emoticon_string[i] == ":":
#         emoticon_symbol += emoticon_string[i] + emoticon_string[i + 1]
#         print(emoticon_symbol)
#         emoticon_symbol = ""

# 6. Replace Repeating Chars
# repeated_string = input()
# refined_string = ""
# for i in range(len(repeated_string)):
#     if i == len(repeated_string) - 1:
#         refined_string += repeated_string[i]
#         break
#     elif repeated_string[i] != repeated_string[i + 1]:
#         refined_string += repeated_string[i]
# print(refined_string)

# 7. String Explosion
# input_string = list(input())
# refined_string = ""
# i = 0
# explosion = 0
#
# while i < len(input_string):
#
#     if input_string[i] != ">" and input_string[i] != "*":  # NOT explosion
#         refined_string += input_string[i]
#
#     elif input_string[i] != "*":  # > Explosion
#         refined_string += input_string[i]
#         explosion += int(input_string[i + 1])
#         boom_begin = i + 1
#         boom_end = i + explosion + 1
#         if boom_end >= len(input_string):
#             boom_end = len(input_string)
#         for j in range(boom_begin, boom_end):
#             if input_string[j] != ">":
#                 input_string[j] = "*"
#                 explosion -= 1
#             else:
#                 break
#
#     i += 1
#
# print(refined_string)

# 8. Letters Change Numbers
# UPPER_INDEX = 64
# LOWER_INDEX = 96
# input_string = input().strip()
# words_list = input_string.split()
# total_sum = 0
# for i in words_list:
#     end_index = len(i) - 1
#     number = int(i[1:end_index])
#
#     if i[0].isupper():  # FIRST LETTER UPPER CASE - DIVIDE
#         total_sum += number / (ord(i[0]) - UPPER_INDEX)
#     elif i[0].islower():  # FIRST LETTER lower case - MULTIPLY
#         total_sum += number * (ord(i[0]) - LOWER_INDEX)
#
#     if i[end_index].isupper():  # LAST LETTER UPPER CASE - SUBTRACT
#         total_sum -= ord(i[end_index]) - UPPER_INDEX
#     elif i[end_index].islower():  # LAST LETTER lower case - ADD
#         total_sum += ord(i[end_index]) - LOWER_INDEX
#
# print(f"{total_sum:.2f}")

# 9. Rage Quit
# input_string = input().upper()
# unique_list = set()
# rage_sub_word = ""
# rage_word = ""
# repeat = ""
#
# for i in range(len(input_string)):
#
#     if input_string[i].isdigit():
#         repeat += input_string[i]
#
#         if i + 1 < len(input_string):
#             if input_string[i + 1].isdigit():
#                 repeat += input_string[i + 1]
#                 i += 1
#         else:
#             pass
#
#         if int(repeat) > 0:
#             for j in rage_sub_word:
#                 unique_list.add(j)
#             rage_word += rage_sub_word * int(repeat)
#
#         repeat = ""
#         rage_sub_word = ""
#
#     else:
#         rage_sub_word += input_string[i]
#         i += 1
#
# print(f"Unique symbols used: {len(unique_list)}")
# print(rage_word)

# 10. Winning Ticket
def symbol_checker(ticket_half, symbol):
    if symbol not in ticket_half:
        return 0

    max_count = 0
    current_count = 0

    for k in range(len(ticket_half)):
        if ticket_half[k] == symbol:
            current_count += 1
        else:
            if max_count < current_count:
                max_count = current_count
            current_count = 0

    return max(max_count, current_count)


winner_symbol = "@#$^"
tickets = input().split(",")
for i in tickets:
    i = i.strip()
    if len(i) != 20:
        print(f"invalid ticket")
        continue

    jackpot = False
    symbol_match = False

    first_half = i[0:10]
    second_half = i[10:]

    for j in winner_symbol:

        if i.count(j) == 20:
            jackpot = True
            print(f'ticket "{i}" - {10}{j} Jackpot!')
            break

        first = symbol_checker(first_half, j)
        second = symbol_checker(second_half, j)

        if 6 <= first <= 10 and 6 <= second <= 10:
            symbol_match = True
            print(f'ticket "{i}" - {min(first, second)}{j}')
            break

    if not symbol_match and not jackpot:
        print(f'ticket "{i}" - no match')
