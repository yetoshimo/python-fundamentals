# 01. Computer Store
# command_input = input()
# tax_total = 0
# total_price = 0
# while command_input not in ("special", "regular"):
#     price = float(command_input)
#     if price < 0:
#         print(f"Invalid price!")
#     else:
#         tax_total += price * 0.2
#         total_price += price * 1.2
#     command_input = input()
# if total_price == 0:
#     print(f"Invalid order!")
# else:
#     print(f"Congratulations you've just bought a new computer!")
#     print(f"Price without taxes: {total_price - tax_total:.2f}$")
#     print(f"Taxes: {tax_total:.2f}$")
#     print(f"-----------")
#     if command_input == "special":
#         total_price = total_price * 0.9
#     print(f"Total price: {total_price:.2f}$")

# 02. The Lift
# number_of_people = int(input())
# lift_spaces = [int(i) for i in input().split(" ")]
# for i in range(len(lift_spaces)):
#     cabin_space = 4 - lift_spaces[i]
#     if cabin_space < number_of_people:
#         number_of_people -= cabin_space
#         lift_spaces[i] = lift_spaces[i] + cabin_space
#     elif cabin_space >= number_of_people:
#         lift_spaces[i] = lift_spaces[i] + number_of_people
#         number_of_people = 0
# if sum(lift_spaces) < 4 * len(lift_spaces) and number_of_people == 0:
#     print(f"The lift has empty spots!")
#     print(*lift_spaces, sep=" ")
# elif sum(lift_spaces) == 4 * len(lift_spaces) and number_of_people == 0:
#     print(*lift_spaces, sep=" ")
# else:
#     print(f"There isn't enough space! {number_of_people} people in a queue!")
#     print(*lift_spaces, sep=" ")

# 03. Memory Game
list_of_numbers = [i for i in input().split()]
sequence_of_numbers = list(filter(None, list_of_numbers))
command_input = input()
number_of_tries = 0
all_matched = False

while command_input != "end" and sequence_of_numbers:

    number_of_tries += 1
    index_one = int(command_input.split(" ")[0])
    index_two = int(command_input.split(" ")[1])

    if (0 <= index_one <= len(sequence_of_numbers) - 1) and (0 <= index_two <= len(sequence_of_numbers) - 1) \
            and (index_one != index_two):

        if sequence_of_numbers[index_one] == sequence_of_numbers[index_two]:
            print(f"Congrats! You have found matching elements - {sequence_of_numbers[index_one]}!")
            matched_number = sequence_of_numbers[index_one]
            sequence_of_numbers.remove(matched_number)
            sequence_of_numbers.remove(matched_number)

        else:
            print(f"Try again!")
    else:
        index_start = int(len(sequence_of_numbers) / 2)
        sequence_of_numbers.insert(index_start, f"-{number_of_tries}a")
        sequence_of_numbers.insert(index_start, f"-{number_of_tries}a")
        print(f"Invalid input! Adding additional elements to the board")

    command_input = input()

if not sequence_of_numbers:
    print(f"You have won in {number_of_tries} turns!")

else:
    print(f"Sorry you lose :(")
    print(" ".join(sequence_of_numbers))
