# 1. Data Types
# def if_integer():
#     return int(input_string) * 2
#
#
# def if_real():
#     return float(input_string) * 1.5
#
#
# def if_string():
#     return "$"+input_string+"$"
#
#
# input_read = input()
# input_string = input()
# if input_read == "int":
#     print(if_integer())
# elif input_read == "real":
#     print("%.2f" % if_real())
# elif input_read == "string":
#     print(if_string())

# 2. Center Point
# from math import sqrt
#
#
# def calculate_diagonal_1():
#     return sqrt((coor_x1 ** 2) + (coor_y1 ** 2))
#
#
# def calculate_diagonal_2():
#     return sqrt((coor_x2 ** 2) + (coor_y2 ** 2))
#
#
# coor_x1 = float(input())
# coor_y1 = float(input())
# coor_x2 = float(input())
# coor_y2 = float(input())
# if calculate_diagonal_1() == calculate_diagonal_2() or calculate_diagonal_2() > calculate_diagonal_1():
#     print(f"({int(coor_x1)}, {int(coor_y1)})")
# else:
#     print(f"({int(coor_x2)}, {int(coor_y2)})")

# 3. Longer Line
# from math import sqrt
#
#
# def first_line_length():
#     return sqrt((abs(coor_x1 - coor_x2) ** 2) + abs(coor_y1 - coor_y2) ** 2)
#
#
# def second_line_length():
#     return sqrt((abs(coor_x3 - coor_x4) ** 2) + abs(coor_y3 - coor_y4) ** 2)
#
#
# def diagonal_length_1(x1, y1):
#     return sqrt((x1 ** 2) + (y1 ** 2))
#
#
# def diagonal_length_2(x2, y2):
#     return sqrt((x2 ** 2) + (y2 ** 2))
#
#
# # First Line Coordinates
# coor_x1 = float(input())
# coor_y1 = float(input())
# coor_x2 = float(input())
# coor_y2 = float(input())
# # Second Line Coordinates
# coor_x3 = float(input())
# coor_y3 = float(input())
# coor_x4 = float(input())
# coor_y4 = float(input())
# if first_line_length() == second_line_length() or first_line_length() > second_line_length():
#     if diagonal_length_1(coor_x1, coor_y1) == diagonal_length_2(coor_x2, coor_y2) \
#             or diagonal_length_2(coor_x2, coor_y2) > diagonal_length_1(coor_x1, coor_y1):
#         print(f"({int(coor_x1)}, {int(coor_y1)})({int(coor_x2)}, {int(coor_y2)})")
#     else:
#         print(f"({int()}, {int(coor_y2)})({int(coor_x1)}, {int(coor_y1)})")
# else:
#     if diagonal_length_1(coor_x3, coor_y3) == diagonal_length_2(coor_x4, coor_y4) \
#             or diagonal_length_2(coor_x4, coor_y4) > diagonal_length_1(coor_x3, coor_y3):
#         print(f"({int(coor_x3)}, {int(coor_y3)})({int(coor_x4)}, {int(coor_y4)})")
#     else:
#         print(f"({int(coor_x4)}, {int(coor_y4)})({int(coor_x3)}, {int(coor_y3)})")

# 4. Tribonacci Sequence
# def tribonacci_return(x):
#     if x <= 0:
#         return 0
#     elif x == 1 or x == 2:
#         return 1
#     elif x == 3:
#         return 2
#     elif x > 3:
#         return int(tribonacci_list[x - 2]) + int(tribonacci_list[x - 3]) + int(tribonacci_list[x - 4])
#
#
# def form_the_list(x):
#     for i in range(1, x+1):
#         tribonacci_list.append(str(tribonacci_return(i)))
#     return print(" ".join(tribonacci_list))
#
#
# requested_length = int(input())
# tribonacci_list =[]
# form_the_list(requested_length)

# 5. Multiplication Sign
def check_numbers(x, y, z):
    negative_count = 0
    if x == 0 or y == 0 or z == 0:
        return "zero"
    if x < 0:
        negative_count += 1
    if y < 0:
        negative_count += 1
    if z < 0:
        negative_count += 1
    if negative_count % 2 != 0:
        return "negative"
    else:
        return "positive"


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(check_numbers(first_number, second_number, third_number))
