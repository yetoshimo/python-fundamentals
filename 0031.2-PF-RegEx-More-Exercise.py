# 1. Race
# from re import findall
# list_of_names = input().split(", ")
# character_set = input()
# matched_word = ""
# racer = ""
# distance = 0
# competition = {}
# while character_set != "end of race":
#     regex = r"(\w+)"
#     matches = findall(regex, character_set)
#     for i in matches:
#         matched_word += i
#     for j in matched_word:
#         if j.isalpha():
#             racer += j
#         else:
#             distance += int(j)
#     if racer in list_of_names:
#         if racer in competition:
#             competition[racer] += distance
#         else:
#             competition[racer] = distance
#     racer = ""
#     distance = 0
#     matched_word = ""
#     character_set = input()
# first_three = []
# for racer, distance in sorted(competition.items(), key=lambda kv: (-kv[1])):
#     first_three.append(racer)
# print(f"1st place: {first_three[0]}")
# print(f"2nd place: {first_three[1]}")
# print(f"3rd place: {first_three[2]}")

# 2. SoftUni Bar Income
# from re import findall
# customer_string = input()
# total_income = 0
# while customer_string != "end of shift":
#     regex = r"%(?P<name>[A-Z][a-z]+)%[^\|\$\%\.]*?<(?P<product>\w+)>[^\|\$\%\.]*?\|(?P<quantity>\d+)[^\|\$\%\.]*?\|[^\|\$\%\.]*?(?P<price>\d+\.?\d+)\$"
#     matches = findall(regex, customer_string)
#     if matches:
#         print(f"{matches[0][0]}: {matches[0][1]} - {int(matches[0][2]) * float(matches[0][3]):.2f}")
#         total_income += int(matches[0][2]) * float(matches[0][3])
#     customer_string = input()
# print(f"Total income: {total_income:.2f}")

# 3. Star Enigma
# from re import findall
# number_of_messages = int(input())
# real_message = ""
# attacked_planets = []
# destroyed_planets = []
# for i in range(number_of_messages):
#     encrypted_message = input()
#     star_encrypted = findall("([STARstar])", encrypted_message)
#     star_enigma = len(star_encrypted)
#     for j in encrypted_message:
#         real_message += chr(ord(j) - star_enigma)
#     regex = r"@(?P<planetname>[A-Za-z]+)[^\@\-\!\:\>]*?:(?P<population>\d+)[^\@\-\!\:\>]*?!(?P<attacktype>[AD])![^\@\-\!\:\>]*?->(?P<soldiercount>\d+)"
#     matches = findall(regex, real_message)
#     if matches:
#         if matches[0][2] == "A":
#             attacked_planets.append(matches[0][0])
#         if matches[0][2] == "D":
#             destroyed_planets.append(matches[0][0])
#     star_enigma = 0
#     real_message = ""
# print(f"Attacked planets: {len(attacked_planets)}")
# if len(attacked_planets) > 0:
#     for i in sorted(attacked_planets):
#         print(f"-> {i}")
# print(f"Destroyed planets: {len(destroyed_planets)}")
# if len(destroyed_planets) > 0:
#     for j in sorted(destroyed_planets):
#         print(f"-> {j}")

# 4. Nether Realms
# from re import findall
# from re import split
# demon_name = input()
# pattern = r"\s*,\s*|,\s*"
# demon_names = split(pattern, demon_name)
# total_health = 0
# raw_damage = 0
# demon_list = {}
# for name in demon_names:
#     demon_list[name] = []
#     health_matches = findall("([^0-9\+\-\*\/\.]+)", name)
#     health = "".join(health_matches)
#     for i in health:
#         total_health += ord(i)
#     demon_list[name].append(total_health)
#     total_health = 0
#     damage_matches = findall("(([+-]?)(\d+(\.\d+)?))", name)
#     for j in range(len(damage_matches)):
#         raw_damage += float(damage_matches[j][0])
#     damage_multiplier = findall("([\/\*])", name)
#     if damage_multiplier:
#         for k in damage_multiplier:
#             if k == "*":
#                 raw_damage = raw_damage * 2
#             elif k == "/":
#                 raw_damage = raw_damage / 2
#     demon_list[name].append(raw_damage)
#     raw_damage = 0
# for i in sorted(demon_list):
#     print(f"{i} - {demon_list[i][0]} health, {demon_list[i][1]:.2f} damage")

# 5. HTML Parser
from re import findall

title_regex = r'<title>([^<>]*)<\/title>'
info = input()
title = findall(title_regex, info)
title = ''.join(title)
print(f"Title: {title}")
body_regex = r'<body>.*<\/body>'
body = findall(body_regex, info)
body = ''.join(body)
content_regex = r">([^><]*)<"
content = findall(content_regex, body)
content = ''.join(content)
content = content.replace('\\n', '')
print(f'Content: {content}')
