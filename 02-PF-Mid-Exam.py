# 01. SoftUni Reception
# first_employee = int(input())
# second_employee = int(input())
# third_employee = int(input())
# per_hour = first_employee + second_employee + third_employee
# total_students = int(input())
# time_passed = 0
# while total_students > 0:
#     time_passed += 1
#     total_students -= per_hour
#     if time_passed % 4 == 0:
#         time_passed += 1
# print(f"Time needed: {time_passed}h.")

# 02. Array Modifier
# number_list = [int(i) for i in input().split(" ")]
# command_input = input()
# while command_input != "end":
#     command = command_input.split(" ")[0]
#
#     if command == "swap":
#         index_one = int(command_input.split(" ")[1])
#         number_one = number_list[index_one]
#         index_two = int(command_input.split(" ")[2])
#         number_two = number_list[index_two]
#
#         number_list[index_one] = number_two
#         number_list[index_two] = number_one
#
#     elif command == "multiply":
#         index_one = int(command_input.split(" ")[1])
#         number_one = number_list[index_one]
#         index_two = int(command_input.split(" ")[2])
#         number_two = number_list[index_two]
#
#         number_list[index_one] = number_one * number_two
#
#     elif command == "decrease":
#         for i in range(len(number_list)):
#             number_list[i] -= 1
#
#     command_input = input()
# print(*number_list, sep=", ")

# 03. Numbers
number_list = [int(i) for i in input().split(" ")]
average = sum(number_list) / len(number_list)
above_average = sorted([i for i in number_list if i > average], reverse=True)
if above_average:
    if len(above_average) < 5:
        print(*above_average, sep=" ")
    else:
        for i in range(5):
            print(above_average[i], end=" ")
else:
    print("No")
