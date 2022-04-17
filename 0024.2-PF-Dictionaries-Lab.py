# 1. Bakery
# input_command = input().split(" ")
# bakery = {}
# for i in range(0, len(input_command), 2):
#     key = input_command[i]
#     value = input_command[i + 1]
#     bakery[key] = int(value)
# print(bakery)

# 2. Stock
# input_command = input().split(" ")
# search_products = input().split(" ")
# stock_dictionary = {}
# for i in range(0, len(input_command), 2):
#     key = input_command[i]
#     value = input_command[i + 1]
#     stock_dictionary[key] = int(value)
# for j in search_products:
#     if j in stock_dictionary.keys():
#         print(f"We have {stock_dictionary[j]} of {j} left")
#     else:
#         print(f"Sorry, we don't have {j}")

# 3. Statistics
# input_command = input().split(": ")
# dict_statistics = {}
# while input_command[0] != "statistics":
#     if input_command[0] not in dict_statistics.keys():
#         dict_statistics[input_command[0]] = int(input_command[1])
#     else:
#         dict_statistics[input_command[0]] += int(input_command[1])
#     input_command = input().split(": ")
# print(f"Products in stock:")
# for key, value in dict_statistics.items():
#     print(f"{'- '}{key}: {value}")
# print(f"Total Products: {len(dict_statistics)}")
# print(f"Total Quantity: {sum(dict_statistics.values())}")

# 4. Odd Occurrences
# input_command = input().lower().split(" ")
# word_dictionary = {}
# for i in input_command:
#     if i in word_dictionary.keys():
#         word_dictionary[i] += 1
#     else:
#         word_dictionary[i] = 1
# for key, value in word_dictionary.items():
#     if value % 2 != 0:
#         print(f"{key}", end=" ")

# 5. Word Synonyms
word_count = int(input())
counter = 0
word_dictionary = {}
while counter < word_count:
    word = input()
    synonym = input()
    if word in word_dictionary.keys():
        word_dictionary[word].append(synonym)
    else:
        word_dictionary[word] = [synonym]
    counter += 1
for key, value in word_dictionary.items():
    print(f"{key} - {', '.join(value)}")
