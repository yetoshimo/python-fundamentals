# 1. Count Chars in a String
# input_text = input().split(" ")
# letter_dictionary = {}
# for i in input_text:
#     letters = list(i)
#     for j in letters:
#         if j in letter_dictionary.keys():
#             letter_dictionary[j] += 1
#         else:
#             letter_dictionary[j] = 1
# for key, value in letter_dictionary.items():
#     print(f"{key} -> {value}")

# 2. A Miner Task
# input_resource = input()
# resource_list = []
# resource_dictionary = {}
# while input_resource != "stop":
#     resource_list.append(input_resource)
#     input_resource = input()
# for i in range(0, len(resource_list), 2):
#     if resource_list[i] not in resource_dictionary.keys():
#         resource_dictionary[resource_list[i]] = int(resource_list[i + 1])
#     else:
#         resource_dictionary[resource_list[i]] += int(resource_list[i + 1])
# for key, value in resource_dictionary.items():
#     print(f"{key} -> {value}")

# 3. Legendary Farming
# Shadowmourne – requires 250 Shards
# Valanyr – requires 250 Fragments
# Dragonwrath – requires 250 Motes
# key_materials = {"shards": 0, "fragments": 0, "motes": 0}
# junk_materials = {}
# LEGENDARY_LIMIT = 250
# legendary_found = False
# while True:
#     item_list = input().lower().split(" ")
#     length = len(item_list)
#
#     for i in range(0, length, 2):
#         material = item_list[i + 1]
#         quantity = int(item_list[i])
#
#         if material == "shards":
#             key_materials[material] += quantity
#
#             if key_materials[material] >= LEGENDARY_LIMIT:
#                 key_materials[material] -= LEGENDARY_LIMIT
#                 print(f"Shadowmourne obtained!")
#                 legendary_found = True
#                 break
#
#         elif material == "fragments":
#             key_materials[material] += quantity
#
#             if key_materials[material] >= LEGENDARY_LIMIT:
#                 key_materials[material] -= LEGENDARY_LIMIT
#                 print(f"Valanyr obtained!")
#                 legendary_found = True
#                 break
#
#         elif material == "motes":
#             key_materials[material] += quantity
#
#             if key_materials[material] >= LEGENDARY_LIMIT:
#                 key_materials[material] -= LEGENDARY_LIMIT
#                 print(f"Dragonwrath obtained!")
#                 legendary_found = True
#                 break
#
#         else:
#             if material not in junk_materials:
#                 junk_materials[material] = 0
#             junk_materials[material] += quantity
#
#     if legendary_found:
#         break
#
# for key, value in sorted(key_materials.items(), key=lambda kv: (-kv[1], kv[0])):
#     print(f"{key}: {value}")
#
# for key, value in sorted(junk_materials.items(), key=lambda kv: kv[0]):
#     print(f"{key}: {value}")

# 4. Orders
# product = input().split()
# product_name = product[0]
# product_price = float(product[1])
# product_quantity = float(product[2])
# price_dictionary = {}
# quantity_dictionary = {}
# while product_name != "buy":
#     product_price = float(product[1])
#     product_quantity = float(product[2])
#     if product_name not in price_dictionary:
#         price_dictionary[product_name] = 0
#     price_dictionary[product_name] = product_price
#     if product_name not in quantity_dictionary:
#         quantity_dictionary[product_name] = 0
#     quantity_dictionary[product_name] += product_quantity
#     product = input().split()
#     product_name = product[0]
# for key, value in price_dictionary.items():
#     print(f"{key} -> {value * quantity_dictionary[key]:.2f}")

# 5. SoftUni Parking
# number_of_commands = int(input())
# registered_cars = {}
# for i in range(number_of_commands):
#     input_command = input().split()
#     command = input_command[0]
#     name = input_command[1]
#     if command == "register":
#         registration_number = input_command[2]
#         if name not in registered_cars:
#             registered_cars[name] = ""
#             registered_cars[name] = registration_number
#             print(f"{name} registered {registration_number} successfully")
#         else:
#             print(f"ERROR: already registered with plate number {registered_cars[name]}")
#     if command == "unregister":
#         if name not in registered_cars:
#             print(f"ERROR: user {name} not found")
#         else:
#             print(f"{name} unregistered successfully")
#             registered_cars.pop(name)
# for key, value in registered_cars.items():
#     print(f"{key} => {value}")

# 6. Courses
# input_command = input()
# courses_dictionary = {}
# while input_command != "end":
#     course_name = input_command.split(" : ")[0]
#     student_name = input_command.split(" : ")[1]
#     if course_name not in courses_dictionary:
#         courses_dictionary[course_name] = []
#         courses_dictionary[course_name].append(student_name)
#     else:
#         courses_dictionary[course_name].append(student_name)
#     input_command = input()
#
# for key, value in sorted(courses_dictionary.items(), key=lambda kv: -len(kv[1])):
#     print(f"{key}: {len(value)}")
#     for i in sorted(value):
#         print(f"-- {i}")

# 7. Student Academy
# number_of_students = int(input())
# student_list = []
# students_dictionary = {}
#
# for i in range(number_of_students):
#     student_name = input()
#     if student_name not in students_dictionary:
#         students_dictionary[student_name] = []
#     grade = float(input())
#     students_dictionary[student_name].append(grade)
#
# for key, value in sorted(students_dictionary.items(), key=lambda kv: -(sum(kv[1])/len(kv[1]))):
#     if sum(value)/len(value) >= 4.5:
#         print(f"{key} -> {sum(value)/len(value):.2f}")

# 8. Company Users
# command_input = input()
# companies_dictionary = {}
#
# while command_input != "End":
#     company_name = command_input.split(" -> ")[0]
#     if company_name not in companies_dictionary:
#         companies_dictionary[company_name] = []
#     employee_id = command_input.split(" -> ")[1]
#     if employee_id not in companies_dictionary[company_name]:
#         companies_dictionary[company_name].append(employee_id)
#     command_input = input()
#
# for key, value in sorted(companies_dictionary.items(), key=lambda kv: kv[0]):
#     print(f"{key}")
#     for i in value:
#         print(f"-- {i}")

# 9. ForceBook
# command_input = input()
# force_users = {}
# while command_input != "Lumpawaroo":
#     if " | " in command_input:
#         force_side = command_input.split(" | ")[0]
#         if force_side not in force_users:
#             force_users[force_side] = []
#
#         force_user = command_input.split(" | ")[1]
#         for key, value in force_users.items():
#             if force_user in value:
#                 break
#             else:
#                 force_users[force_side].append(force_user)
#
#     else:
#         old_side = ""
#         force_user = command_input.split(" -> ")[0]
#         force_side = command_input.split(" -> ")[1]
#
#         for key, value in force_users.items():
#             if force_user in value:
#                 old_side = key
#                 break
#
#         if old_side != "":
#             force_users[old_side].remove(force_user)
#
#             if force_side not in force_users:
#                 force_users[force_side] = []
#             force_users[force_side].append(force_user)
#
#         else:
#             if force_side not in force_users:
#                 force_users[force_side] = []
#             force_users[force_side].append(force_user)
#
#         print(f"{force_user} joins the {force_side} side!")
#
#     command_input = input()
#
# for key, value in sorted(force_users.items(), key=lambda kv: (-len(kv[1]), kv[0])):
#     if len(value) > 0:
#         print(f"Side: {key}, Members: {len(value)}")
#         for i in sorted(value):
#             print(f"! {i}")


# line = input()
# sides = {}
#
# while line != "Lumpawaroo":
#     if " | " in line:
#         args = line.split(" | ")
#         side = args[0]
#         user = args[1]
#         # 2do If you receive forceSide | forceUser, you should check if such forceUser already exists, and if not, add him/her to the corresponding side
#         if side not in sides:
#             sides[side] = []
#
#         all_values = []
#
#         for current_list in sides.values():
#             all_values += current_list
#
#         if user not in all_values:
#             sides[side].append(user)
#
#     else:
#         args = line.split(" -> ")
#         user = args[0]
#         side = args[1]
#         old_side = ""
#
#         for key, value in sides.items():
#             if user in value:
#                 old_side = key
#                 break
#
#         if old_side != "":
#             sides[old_side].remove(user)
#
#             if side not in sides:
#                 sides[side] = []
#
#             sides[side].append(user)
#         else:
#             if side not in sides:
#                 sides[side] = []
#
#             sides[side].append(user)
#
#         print(f"{user} joins the {side} side!")
#
#     line = input()
#
# sides = dict(sorted(sides.items(), key=lambda x: (-len(x[1]), x[0])))
#
# for side, users in sides.items():
#     if len(users) == 0:
#         continue
#
#     print(f"Side: {side}, Members: {len(users)}")
#
#     for user in sorted(users):
#         print(f"! {user}")

# 10. SoftUni Exam Results
line_input = input()
scores_dictionary = {}
languages_dictionary = {}
while line_input != "exam finished":
    username = line_input.split("-")[0]
    language = line_input.split("-")[1]

    if language != "banned":
        points = int(line_input.split("-")[2])
        if username not in scores_dictionary:
            scores_dictionary[username] = points
        else:
            if scores_dictionary[username] > points:
                pass
            else:
                scores_dictionary[username] = points

        if language in languages_dictionary:
            languages_dictionary[language] += 1
        else:
            languages_dictionary[language] = 1

    else:
        scores_dictionary.pop(username)

    line_input = input()

print(f"Results:")
for username, score in sorted(scores_dictionary.items(), key=lambda kv: (-kv[1], kv[0])):
    print(f"{username} | {score}")
print(f"Submissions:")
for language, count in sorted(languages_dictionary.items(), key=lambda kv: (-kv[1], kv[0])):
    print(f"{language} - {count}")
