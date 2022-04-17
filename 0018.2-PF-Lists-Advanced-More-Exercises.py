# 1. Messaging
# list_of_numbers = [i for i in input().split(" ")]
# string_input = [i for i in input()]
# message = []
# for i in list_of_numbers:
#     char_index = sum([int(j) for j in i])
#     if 0 <= char_index < len(string_input) - 1:
#         message.append(string_input[char_index])
#         string_input.pop(char_index)
#     else:
#         char_index = char_index - len(string_input)
#         message.append(string_input[char_index])
#         string_input.pop(char_index)
# print("".join(message))

# 2. Car Race
# left_racer_path = [int(i) for i in input().split(" ")]
# left_racer_time = 0
# length_of_race = len(left_racer_path)
# right_racer_path = list(reversed(left_racer_path))
# right_racer_time = 0
# for i in left_racer_path[:(length_of_race // 2)]:
#     if i == 0:
#         left_racer_time = left_racer_time * 0.8
#     else:
#         left_racer_time += i
# for j in right_racer_path[:(length_of_race // 2)]:
#     if j == 0:
#         right_racer_time = right_racer_time * 0.8
#     else:
#         right_racer_time += j
# if right_racer_time > left_racer_time:
#     print(f"The winner is left with total time: {left_racer_time:.1f}")
# else:
#     print(f"The winner is right with total time: {right_racer_time:.1f}")

# 3. Take/Skip Rope
# input_string = list(input())
# numbers_list = []
# take_list = []
# skip_list = []
# characters_list = []
# result_string = []
# position = 0
# index = 0
# for i in input_string:
#     if i.isdigit():
#         numbers_list.append(int(i))
#     else:
#         characters_list.append(i)
# for i in range(0, len(numbers_list)):
#     if i == 0:
#         take_list.append(numbers_list[i])
#     elif i % 2 == 0:
#         take_list.append(numbers_list[i])
#     else:
#         skip_list.append(numbers_list[i])
# while index < len(take_list):
#     if take_list[index] > 0:
#         result_string += characters_list[position:position + take_list[index]]
#         position += take_list[index] + skip_list[index]
#     else:
#         position += skip_list[index]
#     index += 1
# print("".join(result_string))

# 4. Social Distribution
# population_numbers = [int(i) for i in input().split(", ")]
# minimum_wealth = int(input())
# if sum(population_numbers) / len(population_numbers) >= minimum_wealth:
#     for i in range(0, len(population_numbers)):
#         max_wealth = max(population_numbers)
#         max_wealth_index = population_numbers.index(max_wealth)
#         if population_numbers[i] < minimum_wealth:
#             population_numbers[max_wealth_index] = max_wealth - (minimum_wealth - population_numbers[i])
#             population_numbers[i] = minimum_wealth
#     print(population_numbers)
# else:
#     print("No equal distribution possible")

# 5. Kate's Way Out
rows = int(input())
maze = [list(input()) for i in range(rows)]
rows = 4
maze = ["######",
        "##  k#",
        "## ###",
        "## ###"]
start_pos = [(row, col) for row in range(rows) for col in range(len(maze[row])) if maze[row][col] == "k"][0]

try:
    exitPoint = [(row, col) for row in range(rows) for col in range(len(maze[row])) if
                 maze[row][col] == " " and (row == rows - 1 or row == 0 or col == 0 or col == len(maze[1]) - 1)][0]
except IndexError:
    try:
        exitPoint = [(row, col) for row in range(rows) for col in range(len(maze[row])) if
                     maze[row][col] == "k" and (row == rows - 1 or row == 0 or col == 0 or col == len(maze[1]) - 1)][0]
    except IndexError:
        exitPoint = []

was_here = []
correct_path = []
for row in range(rows):
    was_here.append([])
    correct_path.append([])
    for col in range(len(maze[row])):
        was_here[row].append(False)
        correct_path[row].append(False)


def recursive_solve(x, y):
    if not exitPoint:
        return False
    if x == exitPoint[0] and y == exitPoint[1]:
        return True  # Exit point
    elif maze[x][y] == "#" or was_here[x][y]:
        return False  # Wall or was_here

    # mark as visited
    was_here[x][y] = True

    if x != 0:  # Top check
        if recursive_solve(x - 1, y):  # Recalls method one up
            correct_path[x][y] = True  # Sets that path value to True;
            return True
    if x != rows - 1:  # Bottom check
        if recursive_solve(x + 1, y):  # Recalls method one down
            correct_path[x][y] = True
            return True
    if y != 0:  # Left edge check
        if recursive_solve(x, y - 1):  # Recalls method one to the left
            correct_path[x][y] = True
            return True
    if y != len(maze[x]) - 1:  # Right edge check
        if recursive_solve(x, y + 1):  # Recalls method one to the right
            correct_path[x][y] = True
            return True
    return False


counter = 1
kate_out = recursive_solve(start_pos[0], start_pos[1])
counter += sum(sum(row) for row in correct_path)
if not kate_out:
    print("Kate cannot get out")
else:
    print(f"Kate got out in {counter} moves")
