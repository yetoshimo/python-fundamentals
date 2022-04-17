# 1. Capture the Numbers
# from re import findall
# matches = []
# while True:
#     input_strings = input()
#     if input_strings:
#         matches.append(findall("\\d+", input_strings))
#     else:
#         break
# matches = filter(None, matches)
# for match in matches:
#     print(" ".join(match), end=" ")

# 2. Find Variable Names in Sentences
# from re import findall
# variable_string = input()
# regex = r"\b\_(?!\_)(\w+)(?<!\_)\b"
# matches = findall(regex, variable_string)
# print(",".join(matches), end="")

# 3. Find Occurrences of Word in Sentence
# from re import finditer
# given_sentence = input().lower()
# search_string = input().lower()
# regex = fr"\b{search_string}\b"
# matches = sum(1 for _ in finditer(regex, given_sentence))
# print(matches)

# 4. Extract Emails
# from re import findall
# email_line = input()
# regex = r"(^|(?<=\s))(([a-zA-Z0-9]+)([\.\-_]?)([A-Za-z0-9]+)(@)([a-zA-Z]+([\.\-_][A-Za-z]+)+))(\b|(?=\s))"
# matches = findall(regex, email_line)
# for i in matches:
#     print(i[1])

# 5. Furniture
# from re import findall
# purchase_input = input()
# money_spent = 0
# furniture = []
# while purchase_input != "Purchase":
#     regex = r">>(?P<furniture>[A-Za-z]+)<<(?P<price>\d+(\.\d+)?)!(?P<quantity>\d+)"
#     matches = findall(regex, purchase_input)
#     if matches:
#         furniture.append(matches[0][0])
#         money_spent += float(matches[0][1]) * int(matches[0][3])
#     purchase_input = input()
# print(f"Bought furniture:")
# if len(furniture) > 0:
#     print("\n".join(furniture))
# print(f"Total money spend: {money_spent:.2f}")

# 6. Extract the Links
from re import findall

regex = r"(www\.[A-Za-z0-9-]+(\.([a-z]+))+)"
web_links = []
while True:
    links_text = input()
    if links_text:
        matches = findall(regex, links_text)
        if matches:
            web_links.append(matches[0][0])
    else:
        break
print("\n".join(web_links))
