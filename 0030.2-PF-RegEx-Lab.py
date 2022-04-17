# 1. Match Full Name
# from re import findall
# names = input()
# regex = r'\b[A-Z][a-z]+\s+[A-Z][a-z]+\b'
# matches = findall(regex, names)
# print(" ".join(matches))

# 2. Match Phone Number
# from re import findall
# phone_numbers = input()
# regex = "(\\+359-2-[0-9]{3}-[0-9]{4}|\\+359 2 [0-9]{3} [0-9]{4})\\b"
# matches = findall(regex, phone_numbers)
# print(", ".join(matches))

# 3. Match Dates
# from re import findall
# year_string = input()
# regex = "\\b(?P<day>\\d{2})([-.\\/])(?P<month>[A-Z][a-z]{2})\\2(?P<year>\\d{4})\\b"
# matches = findall(regex, year_string)
# for match in matches:
#     print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")

# 4. Match Numbers
from re import finditer

number_string = input()
regex = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
matches = finditer(regex, number_string)
for match in matches:
    print(match.group(0), end=" ")
