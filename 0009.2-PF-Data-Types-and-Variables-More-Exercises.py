# 1. Biggest of 3 Numbers
# command_first_number = int(input())
# command_second_number = int(input())
# command_third_number = int(input())
# list_of_numbers = [command_first_number, command_second_number, command_third_number]
# print(max(list_of_numbers))

# 2. Exchange Integers
# command_first_number = int(input())
# command_second_number = int(input())
# print(f"Before:\na = {command_first_number}\nb = {command_second_number}\nAfter:\na = {command_second_number}\nb = {command_first_number}")

# 3. Prime Number Checker
# command_input_number = int(input())
# if command_input_number > 1:
#     for i in range(2, command_input_number//2):
#         if (command_input_number % i) == 0:
#             print("False")
#             break
#     else:
#         print("True")
# else:
#     print("False")

# 4. Decrypting Messages
# command_key = int(input())
# command_lines = int(input())
# secret_word = ""
# for i in range(0, command_lines):
#     command_character_input = input()
#     secret_word += chr(ord(command_character_input) + command_key)
# print(secret_word)

# 5. Balanced Brackets
command_number_of_lines = int(input())
open_counter = 0
close_counter = 0
isBalanced = True
for i in range(0, command_number_of_lines):
    command_string = input()
    if command_string == "(":
        open_counter += 1
        if open_counter - close_counter >= 2:
            isBalanced = False
    if command_string == ")":
        close_counter += 1
        if close_counter > open_counter:
            isBalanced = False
if open_counter != close_counter:
    isBalanced = False
if isBalanced:
    print("BALANCED")
else:
    print("UNBALANCED")
