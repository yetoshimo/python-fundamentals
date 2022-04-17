# # 1. Extract Person Information
# from re import search
#
# n_lines = int(input())
# for i in range(n_lines):
#     string_line = input()
#     name = search('@(.+?)\|', string_line).group(1)
#     age = search('#(.+?)\*', string_line).group(1)
#     print(f"{name} is {age} years old.")

# 2. Ascii Sumator
# first_character = ord(input())
# second_character = ord(input())
# random_string = input()
# total_sum = 0
# for i in random_string:
#     if first_character < ord(i) < second_character:
#         total_sum += ord(i)
# print(total_sum)

# 3. Treasure Finder
# from re import search
# number_sequence = input().split()
# number_sequence = [int(i) for i in number_sequence]
# command_input = input()
# key_round = len(command_input)
# modulo_number = len(number_sequence)
# secret_message = ""
# while command_input != "find":
#     key_round = len(command_input)
#     for i in range(key_round):
#         secret_message += chr(ord(command_input[i]) - number_sequence[i % modulo_number])
#     material = search('&(.+?)&', secret_message).group(1)
#     location = search('<(.+?)>', secret_message).group(1)
#     print(f"Found {material} at {location}")
#     secret_message = ""
#     command_input = input()

# 4. Morse Code Translator
# morse_alphabet = {
#     "A": ".-",
#     "B": "-...",
#     "C": "-.-.",
#     "D": "-..",
#     "E": ".",
#     "F": "..-.",
#     "G": "--.",
#     "H": "....",
#     "I": "..",
#     "J": ".---",
#     "K": "-.-",
#     "L": ".-..",
#     "M": "--",
#     "N": "-.",
#     "O": "---",
#     "P": ".--.",
#     "Q": "--.-",
#     "R": ".-.",
#     "S": "...",
#     "T": "-",
#     "U": "..-",
#     "V": "...-",
#     "W": ".--",
#     "X": "-..-",
#     "Y": "-.--",
#     "Z": "--..",
#     " ": "|"
# }
# inverse_morse_alphabet = dict((v, k) for (k, v) in morse_alphabet.items())
# input_code = filter(None, input().split(" "))
# message = ""
# for i in input_code:
#     message += inverse_morse_alphabet[i]
# print(message)

# 5. HTML
title_of_article = input()
content_of_article = input()
command_input = input()
comments_list = []
while command_input != "end of comments":
    comments_list.append(command_input)
    command_input = input()
print(f"<h1>\n\t{title_of_article}\n</h1>")
print(f"<article>\n\t{content_of_article}\n</article>")
for i in comments_list:
    print(f"<div>\n\t{i}\n</div>")
