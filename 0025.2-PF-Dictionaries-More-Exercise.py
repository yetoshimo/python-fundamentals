# 1. Ranking
# contest_input = input()
# contests_dictionary = {}
# while contest_input != "end of contests":
#     # contest_name = contest_input.split(":")[0]
#     # contest_password = contest_input.split(":")[1]
#     contest_name, contest_password = contest_input.split(":")
#     contests_dictionary[contest_name] = contest_password
#     contest_input = input()
#
# submissions_dictionary = {}
# submissions_input = input()
# while submissions_input != "end of submissions":
#     submission_contest = submissions_input.split("=>")[0]  # Contest Name
#     submission_password = submissions_input.split("=>")[1]  # Contest Password
#     submission_username = submissions_input.split("=>")[2]  # Submission Username
#     submission_point = int(submissions_input.split("=>")[3])  # Submission Points
#
#     if submission_contest in contests_dictionary and submission_password == contests_dictionary[submission_contest]:
#
#         if submission_username not in submissions_dictionary:
#             submissions_dictionary[submission_username] = {submission_contest: submission_point}
#
#         else:
#             if submission_contest in submissions_dictionary[submission_username]:
#                 if submissions_dictionary[submission_username][submission_contest] < submission_point:
#                     submissions_dictionary[submission_username][submission_contest] = submission_point
#
#             else:
#                 submissions_dictionary[submission_username][submission_contest] = submission_point
#
#     submissions_input = input()
#
# ## total_points = {}
# ##
# ## for username, contests in submissions_dictionary.items():
# ##     total_points[username] = 0
# ##     for contest_name, points in contests.items():
# ##         total_points[username] += points
#
# ordered_submissions = {n: v for n, v in (sorted(submissions_dictionary.items()))}
# for key, value in ordered_submissions.items():
#     v = {k: p for k, p in sorted(value.items(), key=lambda x: -x[1])}
#     ordered_submissions[key] = v
#
# max_points = 0
# best_candidate = ""
#
# for key, value in ordered_submissions.items():
#     current_points = 0
#     for sk, sv in value.items():
#         current_points += sv
#     if current_points > max_points:
#         max_points = current_points
#         best_candidate = key
#
# ## print(f"Best candidate is {max(total_points)} with total {total_points[max(total_points)]} points.")
#
# print(f"Best candidate is {best_candidate} with total {max_points} points.")
#
# print(f"Ranking:")
#
# for username, user_points in sorted(submissions_dictionary.items(), key=lambda kv: kv[0]):
#     print(f"{username}")
#     for contest, points in sorted(user_points.items(), key=lambda kv: -kv[1]):
#         print(f"#  {contest} -> {points}")

# 2. Judge
# command_input = input()
# contests_dict = {}
# while command_input != "no more time":
#     username = command_input.split(" -> ")[0]
#     contest = command_input.split(" -> ")[1]
#     points = int(command_input.split(" -> ")[2])
#
#     if contest in contests_dict:
#         if username in contests_dict[contest]:
#             if points > contests_dict[contest][username]:
#                 contests_dict[contest][username] = points
#         else:
#             contests_dict[contest][username] = points
#
#     else:
#         contests_dict[contest] = {username: points}
#
#     command_input = input()
#
# for key, value in contests_dict.items():
#     print(f"{key}: {len(value)} participants")
#     position = 1
#     for name, score in sorted(value.items(), key=lambda kv: (-kv[1],kv[0])):
#         print(f"{position}. {name} <::> {score}")
#         position += 1
#
# individual_dict = {}
#
# print(f"Individual standings:")
# for key, value in contests_dict.items():
#     for name, score in value.items():
#         if name in individual_dict:
#             individual_dict[name] += score
#         else:
#             individual_dict[name] = score
#
# individual_position = 1
# for name, score in sorted(individual_dict.items(), key=lambda kv: (-kv[1], kv[0])):
#     print(f"{individual_position}. {name} -> {score}")
#     individual_position += 1

# # 3. MOBA Challenger
# moba_dict = {}
# command_input = input()
# while command_input != "Season end":
#     if "->" in command_input:
#         player_name = command_input.split(" -> ")[0]
#         player_position = command_input.split(" -> ")[1]
#         player_skill = int(command_input.split(" -> ")[2])
#
#         if player_name not in moba_dict:
#             moba_dict[player_name] = {player_position: player_skill}
#
#         elif player_position not in moba_dict[player_name]:
#             moba_dict[player_name][player_position] = player_skill
#
#         elif moba_dict[player_name][player_position] < player_skill:
#             moba_dict[player_name][player_position] = player_skill
#
#     elif "vs" in command_input:
#         player_one = command_input.split(" vs ")[0]
#         player_two = command_input.split(" vs ")[1]
#         one_on_one_position = ""
#
#         if player_one in moba_dict and player_two in moba_dict:
#             for i in moba_dict[player_one]:
#                 for j in moba_dict[player_two]:
#                     if i == j:
#                         one_on_one_position = i
#
#         if one_on_one_position:
#             if moba_dict[player_one][one_on_one_position] > moba_dict[player_two][one_on_one_position]:
#                 moba_dict[player_two].pop(one_on_one_position)
#                 # del moba_dict[player_two][one_on_one_position]
#
#             elif moba_dict[player_one][one_on_one_position] == moba_dict[player_two][one_on_one_position]:
#                 pass
#
#             else:  # moba_dict[player_two][one_on_one_position] > moba_dict[player_one][one_on_one_position]:
#                 moba_dict[player_one].pop(one_on_one_position)
#                 # del moba_dict[player_one][one_on_one_position]
#
#     command_input = input()
#
# individual_standings = {}
#
# for player, skills in moba_dict.items():
#     individual_standings[player] = 0
#     for skill_name, skill_points in skills.items():
#         individual_standings[player] += skill_points
#
# for player, skills in sorted(individual_standings.items(), key=lambda kv: (-kv[1], kv[0])):
#     if skills > 0:
#         print(f"{player}: {skills} skill")
#
#         for skill_name, skill_points in sorted(moba_dict[player].items(), key=lambda kv: (-kv[1], kv[0])):
#             print(f"- {skill_name} <::> {skill_points}")

# 4. Snowwhite
# command_input = input()
# dwarves = {}
# colors = {}
# while command_input != "Once upon a time":
#     name = command_input.split(" <:> ")[0]
#     color = command_input.split(" <:> ")[1]
#     physics = int(command_input.split(" <:> ")[2])
#     id = name + ":" + color
#     if id not in dwarves:
#         if color not in colors:
#             colors[color] = 1
#         else:
#             colors[color] += 1
#         dwarves[id] = [0, color]
#     dwarves[id][0] = max([dwarves[id][0], physics])
#     command_input = input()
#
# sorted_dwarves = dict(sorted(dwarves.items(), key=lambda kv: (kv[1][0], colors[kv[1][1]]), reverse=True))
# for key, value in sorted_dwarves.items():
#     tokens = key.split(":")
#     print(f"({tokens[1]}) {tokens[0]} <-> {value[0]}")

# 5. Dragon Army
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="D:\\Downloads\\dragon_army.log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode="w")
logger = logging.getLogger()

dragon_book = {}
type_names = []
input_lines = int(input())
for i in range(input_lines):
    command_input = input()

    dragon_type = command_input.split(" ")[0]

    dragon_name = command_input.split(" ")[1]

    if dragon_type not in dragon_book:
        # logger.info(f"Type does not exist. {dragon_type} is added.")
        dragon_book[dragon_type] = []

        if command_input.split(" ")[2] == "null":
            dragon_damage = 45
        else:
            dragon_damage = int(command_input.split(" ")[2])

        if command_input.split(" ")[3] == "null":
            dragon_health = 250
        else:
            dragon_health = int(command_input.split(" ")[3])

        if command_input.split(" ")[4] == "null":
            dragon_armor = 10
        else:
            dragon_armor = int(command_input.split(" ")[4])

        stats_list = [dragon_name, dragon_damage, dragon_health, dragon_armor]

        dragon_book[dragon_type].append(stats_list)

    else:
        # logger.info(f"Type exists, Check if {dragon_name} exists in {dragon_type}.")
        for d_name in dragon_book[dragon_type]:
            type_names.append(d_name[0])
        if dragon_name not in type_names:
            # logger.info(f"{dragon_name} does not exist in type {dragon_type}.")
            if command_input.split(" ")[2] == "null":
                dragon_damage = 45
            else:
                dragon_damage = int(command_input.split(" ")[2])

            if command_input.split(" ")[3] == "null":
                dragon_health = 250
            else:
                dragon_health = int(command_input.split(" ")[3])

            if command_input.split(" ")[4] == "null":
                dragon_armor = 10
            else:
                dragon_armor = int(command_input.split(" ")[4])

            stats_list = [dragon_name, dragon_damage, dragon_health, dragon_armor]

            dragon_book[dragon_type].append(stats_list)

            type_names = []

        else:
            # logger.info(f"{dragon_name} does not exist in type {dragon_type}.")
            name_index = type_names.index(dragon_name)
            if command_input.split(" ")[2] == "null":
                dragon_damage = 45
            else:
                dragon_damage = int(command_input.split(" ")[2])
            dragon_book[dragon_type][name_index][1] = dragon_damage

            if command_input.split(" ")[3] == "null":
                dragon_health = 250
            else:
                dragon_health = int(command_input.split(" ")[3])
            dragon_book[dragon_type][name_index][2] = dragon_health

            if command_input.split(" ")[4] == "null":
                dragon_armor = 10
            else:
                dragon_armor = int(command_input.split(" ")[4])
            dragon_book[dragon_type][name_index][3] = dragon_armor

            type_names = []

for i in dragon_book.keys():
    average_type_damage = 0
    average_type_health = 0
    average_type_armor = 0
    t_damage = 0
    t_health = 0
    t_armor = 0
    counter = len(dragon_book[i])

    for j in range(counter):
        t_damage += dragon_book[i][j][1]
    average_type_damage = t_damage / len(dragon_book[i])

    for k in range(counter):
        t_health += dragon_book[i][k][2]
    average_type_health = t_health / len(dragon_book[i])

    for l in range(counter):
        t_armor += dragon_book[i][l][3]
    average_type_armor = t_armor / len(dragon_book[i])

    print(f"{i}::({average_type_damage:.2f}/{average_type_health:.2f}/{average_type_armor:.2f})")

    for m in sorted(dragon_book[i]):
        print(f"-{m[0]} -> damage: {m[1]}, health: {m[2]}, armor: {m[3]}")
