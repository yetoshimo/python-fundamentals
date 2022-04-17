# 1. Trains
# def if_add(value, index):
#     train_list[index] = train_list[index] + value
#     return
#
#
# def if_insert(value, index):
#     train_list[index] = train_list[index] + value
#     return
#
#
# def if_leave(value, index):
#     train_list[index] = train_list[index] - value
#     return
#
#
# total_wagons = int(input())
# train_list = [0 for i in range(0, total_wagons)]
# command_line = input().split(" ")
# while command_line[0] != "End":
#     if command_line[0] == "add":
#         if_add(int(command_line[1]), total_wagons - 1)
#         command_line = input().split(" ")
#     elif command_line[0] == "insert":
#         if_insert(int(command_line[2]), int(command_line[1]))
#         command_line = input().split(" ")
#     elif command_line[0] == "leave":
#         if_leave(int(command_line[2]), int(command_line[1]))
#         command_line = input().split(" ")
# print(train_list)

# # 2. To-do List
# todo_list = []
# importance_dictionary = {}
# command_note = input()
# while command_note != "End":
#     token = command_note.split("-")
#     key = int(token[0])
#     value = token[1]
#     importance_dictionary[key] = value
#     command_note = input()
# for i in sorted(importance_dictionary.keys()):
#     todo_list.append(importance_dictionary[i])
# print(todo_list)

# 3. Palindrome Strings
# words = input()
# palindrome_string = input()
# check_list = words.split(" ")
# counter = 0
# palindromes_list = []
# for i in check_list:
#     if i == "".join(reversed(i)):
#         palindromes_list.append(i)
#     if i == palindrome_string:
#         counter += 1
# print(palindromes_list)
# print(f"Found palindrome {counter} times")

# 4. Even Numbers
# numbers = list(map(lambda x: int(x), input().split(", ")))
# even_indices = []
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         even_indices.append(i)
# print(even_indices)

# 5. The Office
employee_list = input().split(" ")
factor_number = int(input())
employee_happiness = list(map(lambda x: int(x) * factor_number, employee_list))
adjusted_happiness = [i for i in employee_happiness if i >= (sum(employee_happiness) / len(employee_happiness))]
if len(adjusted_happiness) >= len(employee_happiness) / 2:
    print(f"Score: {len(adjusted_happiness)}/{len(employee_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(adjusted_happiness)}/{len(employee_happiness)}. Employees are not happy!")
