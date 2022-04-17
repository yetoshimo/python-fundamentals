# 01. Secret Chat
# secret_message = input()
# command_input = input()
# while command_input != "Reveal":
#     command = command_input.split(":|:")[0]
#
#     if command == "InsertSpace":
#         index = int(command_input.split(":|:")[1])
#
#         secret_message = secret_message[:index] + " " + secret_message[index:]
#
#         print(secret_message)
#
#     if command == "Reverse":
#         substring = command_input.split(":|:")[1]
#
#         if substring in secret_message:
#             secret_message = secret_message.replace(substring, "", 1)
#             secret_message = secret_message + substring[::-1]
#
#             print(secret_message)
#
#         else:
#             print("error")
#
#     if command == "ChangeAll":
#         substring = command_input.split(":|:")[1]
#         replacement = command_input.split(":|:")[2]
#
#         secret_message = secret_message.replace(substring, replacement)
#
#         print(secret_message)
#
#     command_input = input()
#
# print(f"You have a new text message: {secret_message}")

# 02. Mirror Words
# from re import findall
# input_string = input()
# regex = r"([@|#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
# matches = findall(regex, input_string)
#
# pair_list = []
#
# for matched in matches:
#     pair_list.append(matched)
#
# word_pairs = len(pair_list)
#
# mirror_list = []
#
# for i in pair_list:
#     if i[1] == i[2][::-1]:
#         word_to_append = i[1] + " <=> " + i[2]
#         mirror_list.append(word_to_append)
#
# if pair_list:
#     print(f"{len(pair_list)} word pairs found!")
# else:
#     print(f"No word pairs found!")
#
# if mirror_list:
#     print(f"The mirror words are:")
#     print(", ".join(mirror_list))
# else:
#     print(f"No mirror words!")

# 03. Need for Speed III
class Car:
    def __init__(self, car, mileage, fuel):
        self.car = car
        self.mileage = mileage
        self.fuel = fuel


MAX_FUEL = 75

number_of_cars = int(input())

main_car_dictionary = {}

for i in range(number_of_cars):
    car_inputs = input().split("|")
    main_car_dictionary[car_inputs[0]] = Car(car_inputs[0], int(car_inputs[1]), int(car_inputs[2]))

input_command = input()

while input_command != "Stop":
    command = input_command.split(" : ")[0]

    if command == "Drive":
        selected_car = input_command.split(" : ")[1]
        distance = int(input_command.split(" : ")[2])
        fuel_needed = int(input_command.split(" : ")[3])

        if main_car_dictionary[selected_car].fuel < fuel_needed:
            print(f"Not enough fuel to make that ride")
        else:
            main_car_dictionary[selected_car].mileage += distance
            main_car_dictionary[selected_car].fuel -= fuel_needed
            print(f"{selected_car} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")

        if main_car_dictionary[selected_car].mileage >= 100000:
            print(f"Time to sell the {selected_car}!")
            main_car_dictionary.pop(selected_car)

    if command == "Refuel":
        selected_car = input_command.split(" : ")[1]
        refuel = int(input_command.split(" : ")[2])

        if refuel <= MAX_FUEL - main_car_dictionary[selected_car].fuel:
            main_car_dictionary[selected_car].fuel += refuel
            print(f"{selected_car} refueled with {refuel} liters")
        else:
            refuel = MAX_FUEL - main_car_dictionary[selected_car].fuel
            main_car_dictionary[selected_car].fuel = MAX_FUEL
            print(f"{selected_car} refueled with {refuel} liters")

    if command == "Revert":
        selected_car = input_command.split(" : ")[1]
        kilometers = int(input_command.split(" : ")[2])

        main_car_dictionary[selected_car].mileage -= kilometers

        if main_car_dictionary[selected_car].mileage < 10000:
            main_car_dictionary[selected_car].mileage = 10000
        else:
            print(f"{selected_car} mileage decreased by {kilometers} kilometers")

    input_command = input()

sorted_car_dictionary = sorted(main_car_dictionary.values(), key=lambda kv: (-kv.mileage, kv.car))

for i in sorted_car_dictionary:
    print(f"{i.car} -> Mileage: {i.mileage} kms, Fuel in the tank: {i.fuel} lt.")
