# 1. Reverse Strings
# command_input = input()
# while command_input != "end":
#     print(f"{command_input} = {command_input[::-1]}")
#     command_input = input()

# 2. Repeat Strings
# command_input = input().split(" ")
# concatenated_string = ""
# for i in command_input:
#     concatenated_string += i * len(i)
# print(concatenated_string)

# 3. Substring
# remove_string = input()
# main_string = input()
# while remove_string in main_string:
#     main_string = main_string.replace(remove_string, "")
# print(main_string)

# 4. Text Filter
# ban_list = input().split(", ")
# sample_text = input()
# for i in ban_list:
#     while i in sample_text:
#         sample_text = sample_text.replace(i, "*" * len(i))
# print(sample_text)

# 5. Digits, Letters and Other
command_input = input()
digits = ""
characters = ""
for i in command_input:
    if i.isdigit():
        digits += i
        command_input = command_input.replace(i, "")
print(digits)
for j in command_input:
    if j.isalpha():
        characters += j
        command_input = command_input.replace(j, "")
print(characters)
print(command_input)
