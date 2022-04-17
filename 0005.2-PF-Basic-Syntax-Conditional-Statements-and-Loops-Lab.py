# 1. Biggest of Three Numbers
# first_num = int(input())
# second_num = int(input())
# third_num = int(input())
# print(f'{max(first_num , second_num , third_num)}')

# 2. Number Definer
# command_num = float(input())
# if command_num == 0:
#     print("zero")
# elif command_num > 0:
#     if command_num < 1:
#         print("small positive")
#     elif command_num > 1000000:
#         print("large positive")
#     else:
#         print("positive")
# elif command_num < 0:
#     if abs(command_num) < 1:
#         print("small negative")
#     elif abs(command_num) > 1000000:
#         print("large negative")
#     else:
#         print("negative")

# 3. Word Reverse
# command_word = input()
# reversed_word = ""
# for i in range(len(command_word) - 1, -1, -1):
#     reversed_word += command_word[i]
# print(reversed_word)

# 4. Number Between 1 and 100
# command_num = float(input())
# while command_num < 1 or command_num > 100:
#     command_num = float(input())
# print(f"The number {command_num} is between 1 and 100")

# 5. Patterns
command_num = int(input())
for i in range(1, command_num + 1, 1):
    print("*" * i)
for i in range(command_num - 1, 0, -1):
    print("*" * i)
