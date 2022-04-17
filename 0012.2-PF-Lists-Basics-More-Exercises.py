# 1. Zeros to Back
# input_string = input().split(", ")
# zero_counter = 0
# while "0" in input_string:
#     input_string.remove("0")
#     zero_counter += 1
# for i in range(0, zero_counter):
#      input_string.append("0")
# for i in range(0, len(input_string)):
#     input_string[i] = int(input_string[i])
# print(input_string)

# 2. Tic-Tac-Toe
# first_line = input().split(" ")
# second_line = input().split(" ")
# third_line = input().split(" ")
# player_one = False
# player_two = False
# # All possible winning combinations
# # winning_position = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
# # horizontal check
# if first_line.count("1") == 3 or second_line.count("1") == 3 or third_line.count("1") == 3:
#     player_one = True
# if first_line.count("2") == 3 or second_line.count("2") == 3 or third_line.count("2") == 3:
#     player_two = True
# # vertical check
# for i in range(0, 3):
#     if first_line[i] == second_line[i] == third_line[i] and first_line[i] != "0":
#         if first_line[i] == "1":
#             player_one = True
#         if first_line[i] == "2":
#             player_two = True
# # diagonal check
# if (first_line[0] == second_line[1] == third_line[2] and first_line[0] != "0") \
#         or (first_line[2] == second_line[1] == third_line[0] and first_line[2] != "0"):
#     if first_line[0] == "1" or first_line[2] == "1":
#         player_one = True
#     if first_line[0] == "2" or first_line[2] == "2":
#         player_two = True
# if player_one:
#     print("First player won")
# elif player_two:
#     print("Second player won")
# else:
#     print("Draw!")

# 3. Josephus Permutation
# number_string = input().split(" ")
# josephus_offset = int(input())
# counted_out = []
# counter = 0
# index = 0
# while len(number_string) > 0:
#     counter += 1
#     if counter % josephus_offset == 0:
#         counted_out.append(number_string.pop(index))
#     else:
#         index += 1
#     if index >= len(number_string):
#         index = 0
# print('[{0}]'.format(','.join(map(str, counted_out))))

# 4. Battle Ships
# field_rows = int(input())
# counter = 0
# line_input = []
# attacks = []
# attack_columns = []
# coordinates = ""
# row_after_attack = ""
# sunk_ship = 0
# while counter < field_rows:
#     line_input.append(input())
#     counter += 1
# attacks = input().split(" ")
# for i in range(0, len(attacks)):
#     coordinates = attacks[i].split("-")
#     row = int(coordinates[0])
#     column = int(coordinates[1])
#     attack_row = line_input[row]
#     attack_columns = attack_row.split(" ") # this is a list
#     if int(attack_columns[column]) > 0:
#         attack_columns[column] = int(attack_columns[column]) - 1
#         if attack_columns[column] == 0:
#             sunk_ship += 1
#         row_after_attack = " ".join([str(elem) for elem in attack_columns])
#         line_input[row] = row_after_attack
#     else:
#         pass
# print(sunk_ship)

# 5. Hungry Hippos
field_rows = int(input())
counter = 0
line_input = []
block_count = 0
while counter < field_rows:
    row_item = input()
    line_input.append(row_item.split(" "))
    counter += 1
column_number = len(line_input[0])
for i in range(0, field_rows):
    row_elements = line_input[i]
    for j in range(0, column_number):
        if int(row_elements[j]) > 0:
            block_count += 1
            if j + 1 < column_number and int(row_elements[j + 1]) > 0:
                block_count -= 1
            if i > 0:
                temp_element = line_input[i - 1]
                if int(temp_element[j]) > 0:
                    block_count -= 1
print(block_count)
