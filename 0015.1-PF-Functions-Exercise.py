# 1. Smallest of Three Numbers
# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
# def smallest_of_three(a, b, c):
#     return min(a, b, c)
# print(smallest_of_three(first_number, second_number, third_number))

# 2. Add and Subtract
# def add_and_subtract():
#     first_number = int(input())
#     second_number = int(input())
#     third_number = int(input())
#
#     def sum_numbers():
#         return first_number + second_number
#     sum_numbers()
#
#     def subtract():
#         return sum_numbers() - third_number
#     subtract()
#     return print(subtract())
#
#
# add_and_subtract()

# 3. Characters in Range
# first_character_value = ord(input())
# second_character_value = ord(input())
#
#
# def characters_in_range(a, b):
#     for i in range(a+1, b):
#         print(chr(i), end=" ")
#     return
#
#
# characters_in_range(first_character_value, second_character_value)

# 4. Odd and Even Sum
# def odd_and_even_sum():
#     odd_sum = 0
#     even_sum = 0
#     input_string = list(input())
#     for i in range(0, len(input_string)):
#         if int(input_string[i]) % 2 == 0 or int(input_string[i]) == 0:
#             even_sum += int(input_string[i])
#         else:
#             odd_sum += int(input_string[i])
#     return print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
#
#
# odd_and_even_sum()

# 5. Palindrome Integers
# def palindrome_integers():
#     list_of_integers = input().split(", ")
#     for i in range(0, len(list_of_integers)):
#         if list_of_integers[i] == list_of_integers[i][::-1]:
#             print("True")
#         else:
#             print("False")
#     return
#
#
# palindrome_integers()

# 6. Password Validator
# def password_validator():
#     length = False
#     letters_digits = False
#     two_digits_min = False
#     digit_count = 0
#     string_password = input()
#     if 6 <= len(string_password) <= 10:
#         pass
#     else:
#         length = True
#     if length:
#         print("Password must be between 6 and 10 characters")
#     if string_password.isalnum():
#         pass
#     else:
#         letters_digits = True
#     if letters_digits:
#         print("Password must consist only of letters and digits")
#     for i in string_password:
#         if i.isdigit():
#             digit_count += 1
#         else:
#             pass
#     if digit_count < 2:
#         two_digits_min = True
#     if two_digits_min:
#         print("Password must have at least 2 digits")
#     if not length and not letters_digits and not two_digits_min:
#         print("Password is valid")
#     return
#
#
# password_validator()


# 7. Perfetct Number
# def perfect_number():
#     target_number = int(input())
#     denominator_total = 0
#     for i in range(1, target_number):
#         if target_number % i == 0:
#             denominator_total += i
#     if target_number == denominator_total:
#         print("We have a perfect number!")
#     else:
#         print("It's not so perfect.")
#     return
#
#
# perfect_number()

# 8. Loading Bar
# def loading_bar():
#     loaded_value = int(input())
#     if loaded_value == 100:
#         print(f"{loaded_value}% Complete!\n[{'%' * int(loaded_value / 10)}]")
#     else:
#         print(f"{loaded_value}% [{'%' * int(loaded_value / 10)} \
#         {'.' * (10 - int(loaded_value / 10))}]\nStill loading...")
#     return
#
#
# loading_bar()

# 9. Factorial Division
# from math import factorial
#
#
# def factorial_division():
#     first_number = int(input())
#     second_number = int(input())
#     first_factor = factorial(first_number)
#     second_factor = factorial(second_number)
#     print(f"{(first_factor / second_factor):.2f}")
#     return
#
#
# factorial_division()

# 10. Array Manipulator
def exchange_index(index_number):
    return shifted_list[index_number + 1:] + shifted_list[:index_number + 1]


def max_odd():
    max_odd_list = [i for i in shifted_list if i % 2 != 0]
    if not max_odd_list:
        return "No matches"
    else:
        for i in range(total_length - 1, -1, -1):
            if shifted_list[i] == max(max_odd_list):
                return i


def max_even():
    max_even_list = [i for i in shifted_list if i % 2 == 0]
    if not max_even_list:
        return "No matches"
    else:
        for i in range(total_length - 1, -1, -1):
            if shifted_list[i] == max(max_even_list):
                return i


def min_odd():
    min_odd_list = [i for i in shifted_list if i % 2 != 0]
    if not min_odd_list:
        return "No matches"
    else:
        for i in range(total_length - 1, -1, -1):
            if shifted_list[i] == min(min_odd_list):
                return i


def min_even():
    min_even_list = [i for i in shifted_list if i % 2 == 0]
    if not min_even_list:
        return "No matches"
    else:
        for i in range(total_length - 1, -1, -1):
            if shifted_list[i] == min(min_even_list):
                return i


def first_odd(requested_length):
    first_odd_list = [i for i in shifted_list if i % 2 != 0]
    return first_odd_list[:requested_length]


def first_even(requested_length):
    first_even_list = [i for i in shifted_list if i % 2 == 0]
    return first_even_list[:requested_length]


def last_odd(requested_length):
    last_odd_list = [i for i in shifted_list if i % 2 != 0]
    return last_odd_list[-requested_length:]


def last_even(requested_length):
    last_even_list = [i for i in shifted_list if i % 2 == 0]
    return last_even_list[-requested_length:]


input_array = [int(i) for i in input().split(" ")]
call_function = input().split(" ")
total_length = len(input_array)
shifted_list = input_array
while call_function[0] != "end":
    if call_function[0] == "exchange":
        if 0 > int(call_function[1]) or int(call_function[1]) >= total_length:
            print("Invalid index")
        else:
            shifted_list = exchange_index(int(call_function[1]))
        call_function = input().split(" ")
    elif call_function[0] == "max":
        if call_function[1] == "odd":
            print(max_odd())
        else:
            print(max_even())
        call_function = input().split(" ")
    elif call_function[0] == "min":
        if call_function[1] == "odd":
            print(min_odd())
        else:
            print(min_even())
        call_function = input().split(" ")
    elif call_function[0] == "first":
        if int(call_function[1]) > total_length:
            print("Invalid count")
        elif call_function[2] == "odd":
            print(first_odd(int(call_function[1])))
        else:
            print(first_even(int(call_function[1])))
        call_function = input().split(" ")
    elif call_function[0] == "last":
        if int(call_function[1]) > total_length:
            print("Invalid count")
        elif call_function[2] == "odd":
            print(last_odd(int(call_function[1])))
        else:
            print(last_even(int(call_function[1])))
        call_function = input().split(" ")
print(shifted_list)
