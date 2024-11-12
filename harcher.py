# 43

# Rekursiv funkcianer@ aveli chshgri patasxan en talis banc avli dandax en ashxatum ev aveli shat hishoxutyun en zabaxecnum vochrekursiv@ hakarak@

# 44

# def sortAndDisplay(data):
#     for i in range(len(data)):
#         for j in range(len(data) - 1, i, -1):
#             if data[j] < data[j - 1]:
#                 t = data[j]
#                 data[j] = data[j - 1]
#                 data[j - 1] = t
#     print(data)

# 46 chem haskanum inchna sxal

# filename = input("greq file anun: ")
# toxeri_count = {}
# with open(filename, 'r') as file:
#     for i in file:
#         i = i.strip()
#         if i in toxeri_count:
#             toxeri_count[i] += 1
#         else:
#             toxeri_count[i] = 1
# if toxeri_count:
#     for i in toxeri_count:
#         for j in toxeri_count:
#             print(f"{i}: {j}")
# else:
#     print("Error")

# 49,50

# def count_occurrences(character, string):
#     count = 0
#     for char in string:
#         if char == character:
#             count += 1
#     return count
# print(count_occurrences('a, e, i, o, u, y ','hello Word'))

