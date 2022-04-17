# 01. Black Flag
# number_of_days = int(input())
# daily_plunder = int(input())
# expected_plunder = float(input())
# total_plunder = 0
# for i in range(1, number_of_days + 1):
#     total_plunder += daily_plunder
#     if i % 3 == 0:
#         total_plunder += 0.5 * daily_plunder
#     if i % 5 == 0:
#         total_plunder = total_plunder * 0.7
# if total_plunder >= expected_plunder:
#     print(f"Ahoy! {total_plunder:.2f} plunder gained.")
# else:
#     print(f"Collected only {(total_plunder/expected_plunder)*100:.2f}% of the plunder.")

# 02. Treasure Hunt
# initial_loot = input().split("|")
# command_input = input()
# while command_input != "Yohoho!":
#     command_list = command_input.split(" ")
#
#     if command_list[0] == "Loot":
#         for i in range(1, len(command_list)):
#             if command_list[i] not in initial_loot:
#                 initial_loot.insert(0, command_list[i])
#
#     if command_list[0] == "Drop":
#         index = int(command_list[1])
#         if 0 < index < len(initial_loot) - 1:
#             temp_item = initial_loot[index]
#             initial_loot.pop(index)
#             initial_loot.append(temp_item)
#
#     if command_list[0] == "Steal":
#         count = int(command_list[1])
#         stolen_items = initial_loot[-count:]
#         print(", ".join(stolen_items))
#         for j in stolen_items:
#             initial_loot.remove(j)
#
#     command_input = input()
#
# if initial_loot:
#     average_gain = sum(len(i) for i in initial_loot) / len(initial_loot)
#     print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
# else:
#     print(f"Failed treasure hunt.")

# 03. Man-o-War
pirate_ship_status = [int(i) for i in input().split(">")]
warship_status = [int(j) for j in input().split(">")]
max_health_cap = int(input())
command_input = input()
warship_live = True
pirate_ship_live = True
while command_input != "Retire":
    command = command_input.split(" ")[0]

    if command == "Fire":
        index = int(command_input.split(" ")[1])
        damage = int(command_input.split(" ")[2])

        if 0 <= index <= len(warship_status) - 1:
            warship_status[index] -= damage
            if warship_status[index] <= 0:
                print(f"You won! The enemy ship has sunken.")
                warship_live = False
                break

    if command == "Defend":
        start_index = int(command_input.split(" ")[1])
        end_index = int(command_input.split(" ")[2])
        damage = int(command_input.split(" ")[3])

        if 0 <= start_index <= len(pirate_ship_status) - 1 and 0 <= end_index <= len(pirate_ship_status) - 1:
            for j in range(start_index, end_index + 1):
                pirate_ship_status[j] -= damage
                if int(pirate_ship_status[j]) <= 0:
                    print(f"You lost! The pirate ship has sunken.")
                    pirate_ship_live = False
                    break

    if command == "Repair":
        index = int(command_input.split(" ")[1])
        health = int(command_input.split(" ")[2])

        if 0 <= index <= len(pirate_ship_status) - 1:
            pirate_ship_status[index] += health
            if pirate_ship_status[index] > max_health_cap:
                pirate_ship_status[index] = max_health_cap

    if command == "Status":
        repair_needed = len([i for i in pirate_ship_status if int(i) < max_health_cap * 0.2])
        print(f"{repair_needed} sections need repair.")

    command_input = input()

if warship_live and pirate_ship_live:
    print(f"Pirate ship status: {sum([int(k) for k in pirate_ship_status])}")
    print(f"Warship status: {sum([int(h) for h in warship_status])}")
