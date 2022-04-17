# 1. Find The Largest
# command_number = input()
# number_to_string = str(command_number)
# list_of_digits = [int(j) for j in command_number]
# sorted_reversed_list = sorted(list_of_digits, reverse=True)
# print(*sorted_reversed_list, sep="")

# 2. Find The Capitals
# command_string = input()
# list_of_letters = list(command_string)
# list_of_capitals = []
# for i in range(0, len(list_of_letters)):
#     if list_of_letters[i].isupper():
#         list_of_capitals.append(i)
# print(list_of_capitals)

# 3. Wolf In Sheep's Clothing
# command_list = input()
# list_of_herd = list(command_list.split(", "))
# if list_of_herd.index("wolf") == len(list_of_herd)-1:
#     print("Please go away and stop eating my sheep")
# else:
#     print(f"Oi! Sheep number {len(list_of_herd)-1-list_of_herd.index('wolf')}! You are about to be eaten by a wolf!")

# 4. Sum Of A Beach
# command_word = input().lower()
# counter = 0
# sand_counter = command_word.count("sand")
# water_counter = command_word.count("water")
# fish_counter = command_word.count("fish")
# sun_counter = command_word.count("sun")
# print(sand_counter + water_counter + fish_counter + sun_counter)

# 5. How Much Coffee Do You Need?
command_event = input()
coffee_count = 0
while command_event != "END":
    if command_event.lower() in ("coding", "dog", "cat", "movie"):
        if command_event.isupper():
            coffee_count += 2
        else:
            coffee_count += 1
    command_event = input()
if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)
