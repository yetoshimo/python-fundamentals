# 1. Strange Zoo
# command_tail = input()
# command_body = input()
# command_head = input()
# body_of_meerkat = [command_head, command_body, command_tail]
# print(body_of_meerkat)

# 2. Courses
# command_courses = int(input())
# courses_list = []
# for i in range(0, command_courses):
#     courses_list += [input()]
# print(courses_list)

# 3. List Statistics
# command_intervals = int(input())
# positives = []
# negatives = []
# for i in range(0, command_intervals):
#     command_number = int(input())
#     if command_number >= 0:
#         positives.append(command_number)
#     else:
#         negatives.append(command_number)
# print(positives)
# print(negatives)
# print(f"Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}")

# 4. Search
# command_intervals = int(input())
# command_word = input()
# list_of_strings = []
# for i in range(0, command_intervals):
#     command_strings = input()
#     list_of_strings.append(command_strings)
# print(list_of_strings)
# for j in range(len(list_of_strings)-1, -1, -1):
#     element = list_of_strings[j]
#     if command_word not in element:
#         list_of_strings.remove(element)
# print(list_of_strings)

# 5. Numbers Filter
command_intervals = int(input())
list_of_numbers = []
for i in range(0, command_intervals):
    command_input_numbers = int(input())
    list_of_numbers.append(command_input_numbers)
command_condition = input()
for j in range(len(list_of_numbers) - 1, -1, -1):
    element = list_of_numbers[j]
    if command_condition == "even" and element % 2 != 0 and element != 0:
        list_of_numbers.remove(element)
    if command_condition == "odd" and element % 2 == 0:
        list_of_numbers.remove(element)
    if command_condition == "positive" and element < 0:
        list_of_numbers.remove(element)
    if command_condition == "negative" and element >= 0:
        list_of_numbers.remove(element)
print(list_of_numbers)
