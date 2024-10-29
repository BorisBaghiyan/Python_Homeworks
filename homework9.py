# 1

# num1=int(input('Greq tiv: '))
# num2=int(input('Greq tiv: '))
# if num1 > num2:
#     for i in range(num1,num1 * num2 + 1, num1):
#         if i % num2 == 0:
#             print(i)
#             break
# elif num2 > num1:
#     for i in range(num2, num2 * num1 + 1,num2):
#         if i % num1 == 0:
#             print(i)
#             break
# else:
#     print(num1)


# 2

# count1=0
# count2=0
# for i in range(1,101):
#     if i % 2 == 0:
#         count1+=1
#     else:
#         count2+=1
# print(count2)
# print(count1)

# 3

# a = 0
# b = 1
# n = int(input('Greq tiv: '))
# for i in range(1,n+1):
#     print(a)
#     a,b = b, a+b

# 4

# text = 'python 3.9'
# tiv=0
# tar=0
# nshan=0
# for i in text:
#     if i.isdigit():
#         tiv+=1
#     elif i.isalpha:
#         tar+=1
#     else:
#         nshan+=1
# print(f'TAR={tar}\nTIV={tiv}\nNSHAN={nshan}')

# 5

# tiv = input('Greq tiv: ')
# count = 0
# for i in tiv:
#     count += int(i)
# print(count) 

# 6

# count = 1
# tiv = int(input('Greq tiv: '))
# for i in range(1,tiv+1):
#     count *= i
# print(count)

# 7

# tariq = int(input('Greq dzer tariq@: '))
# ser= input('Greq ser Txa and Axjik: ')
# if 18<tariq<24 and ser == 'Txa':
#     print('Ashxatelu e qaxaqic durs')
# elif tariq>24 and ser == 'Axjik':
#     print('Qaxaqum')
# --------------------------------------------------------------------------------------------------------------------------------
# 1

# hamar = int(input('Greq dzer hamar: '))
# for i in range(1,11):
#     if hamar % 2 == 0:
#         print('Lav')
#         break
# else:
#     print('Vat') 

# 2

# count=0
# ashxatavardz=int(input('Greq ashxatavardzi qanak: '))
# for i in range(1,13):
#     count=ashxatavardz * i
# print(count)

# 3

# tiv = int(input('Greq tiv: '))
# count = 1
# for i in range(1, tiv+ 1):
#     count *= (i)
# print(count)

# 4

# ashakertneri_qanak=int(input('Greq qanak: '))
# gnahatakan=int(input('Greq gnahatakan 1-5: '))
# for i in range(1,ashakertneri_qanak+1):
#     if gnahatakan == 3:
#         print('BAVARAR')
#         break
#     elif gnahatakan == 4:
#         print('LAV')
#         break
#     elif gnahatakan == 5:
#         print('GERAZANC')
#         break
# else:
#     print('CUYLIK')

# 5

# summ = 0
# count = 0
# a=int(input('Greq tiv: '))
# b=int(input('Greq tiv: '))
# for i in range(a,b):
#     if i % 3 == 0:
#         summ += i
#         count += 1
# print(summ / count)

# 6

# a=int(input('Greq tiv: '))
# b=int(input('Greq tiv: '))
# summ=(a ** 3)+(b ** 3)
# for i in range(10,100):
#     if summ % i == 0:
#         print(i)


# for i in range(10,100):
#     if ((i % 10)*(i // 10) * 3)==i:
#         print(i)

# 7

# cart=int(input('Greq tiv 1-5: '))
# count1=0
# count2=0
# for i in range(cart-1):
#     tiv=int(input('Greq tiv; '))
#     count2+=tiv
# for i in range(1,cart + 1):
#     count1+=i
# print(count1-count2)

