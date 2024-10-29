# 78

# n = int(input('Greq tiv: '))
# k = 0
# while n != 1:
#     if n % 2 == 0:
#         n = n / 2
#         k += 1
#     else:
#         n = 3 * n + 1
#         k += 1
#         print(k)

# 79

# n = int(input('Greq drakan tiv: '))
# m = int(input('Greq drakan tiv: '))
# if n>m:
#     d=n
# else:
#     m>n
#     d=m
# for i in range(1,d+1):
#     if n % i==0 and m % i==0:
#         print(i)
#     else:
#         continue

# 82 

# q = int(input('Greq tiv: '))
# result = ""
# while q != 0:
#     r = q % 2             
#     result = str(r) + result
#     q = q // 2
#     print(result)


# 126

# import random
# mast = ['♥', '♦', '♣', '♠']
# kart = ['2','3','4','5','6','7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# xaxacoxner = ['Xaxacox 1', 'Xaxacox 2', 'Xaxacox 3', 'Xaxacox 4']
# kalod = [i + j for i in mast for j in kart]
# nor_kalod = []
# while kalod != []:
#     random_kart = random.choice(kalod)
#     nor_kalod.append(random_kart)
#     kalod.remove(random_kart)
# for i in xaxacoxner:
#     print(i, nor_kalod[:5])
#     nor_kalod = nor_kalod[5:]
# kalod2=kalod.pop(nor_kalod)
# print(kalod2)

