# 1. Grades
# def grade_words(grade):
#     if 2 <= grade <= 2.99:
#         return "Fail"
#     elif 3 <= grade <= 3.99:
#         return "Poor"
#     elif 4 <= grade <= 4.49:
#         return "Good"
#     elif 4.5 <= grade <= 5.49:
#         return "Very Good"
#     elif 5.5 <= grade <= 6:
#         return "Excellent"
# print(grade_words(float(input())))

# 2. Calculations
# from math import floor
# math_operator = input()
# first_number = int(input())
# second_number = int(input())
# def math_operations(x, y, operator):
#     if operator == "multiply":
#         return x * y
#     elif operator == "divide":
#         return floor(x / y)
#     elif operator == "add":
#         return x + y
#     elif operator == "subtract":
#         return x - y
# print(math_operations(x = first_number, y = second_number, operator = math_operator))

# 3. Repeat String
# input_string = input()
# repeat_count = int(input())
# def repeat_the_string(a, b):
#     return input_string * repeat_count
# print(repeat_the_string(input_string, repeat_count))

# 4. Orders
# price_list = {"coffee": 1.5, "water": 1, "coke": 1.4, "snacks": 2}
# item_name = input()
# request_amount = int(input())
# def total_price (a, b):
#     return price_list[item_name] * request_amount
# print(f"{total_price(item_name, request_amount):.2f}")

# 5. Calculate Rectangle Area
first_side = int(input())
second_side = int(input())


def rectangle_area(a, b):
    return a * b


print(rectangle_area(first_side, second_side))
