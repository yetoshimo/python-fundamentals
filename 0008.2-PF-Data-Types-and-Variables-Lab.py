# 1. Concat Names
# command_first_name = input()
# command_last_name = input()
# command_delimiter = input()
# concat_name = command_first_name + command_delimiter + command_last_name
# print(concat_name)

# 2. Centuries to Minutes
# from math import floor
# command_century = int(input())
# years = command_century * 100
# days = floor(years * 365.2422)
# hours = days * 24
# minutes = hours * 60
# print(f"{command_century} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")

# 3. Special Numbers
# command_number = int(input())
# for i in range(1, command_number+1):
#     list_of_digits = [int(j) for j in str(i)]
#     if sum(list_of_digits) == 5 or sum(list_of_digits) == 7 or sum(list_of_digits) == 11:
#         print(f"{i} -> True")
#     else:
#         print(f"{i} -> False")

# 4. Convert Meters to Kilometers
# command_meters = int(input())
# kilometers = command_meters / 1000
# print(f"{kilometers:.2f}")

# 5. Pounds to Dollars
command_gbp = int(input())
conversion_rate = 1.31
usd_converted = command_gbp * conversion_rate
print(f"{usd_converted:.3f}")
