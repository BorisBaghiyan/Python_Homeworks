# 63

# count=0
# summ=0
# while True:
#     number=int(input('Greq tiv: '))
#     summ+=1
#     if number == 0:
#         break
#     else:
#         print(number)
#     count+=number
#     print(count/summ)

# 64

# count_a=0
# count_b=0
# count_c=0
# count_d=0
# count_x=0
# a=4.95
# b=9.95
# c=14.95
# d=19.95
# x=24.95
# while True:
#     count_a=(a * 60) /100
#     count_b=(b * 60) /100
#     count_c=(c * 60) /100
#     count_d=(d * 60) /100
#     count_x=(x * 60) /100
#     print(f'{a} zexchvel e {count_a} aysqan')
#     print(f'{b} zexchvel e {count_b} aysqan')
#     print(f'{c} zexchvel e {count_c} aysqan')
#     print(f'{d} zexchvel e {count_d} aysqan')
#     print(f'{x} zexchvel e {count_x} aysqan')
#     break

# 84

# import random

# for i in range(10):
#     nshat_P=0
#     nshat_O=0
#     while True:
#         nshan=random.choice('OP')
#         if nshat_O == 3 or nshat_P == 3:
#             break
#         if nshan == 'O':
#             nshat_O+=1
#             nshat_P==0
#         else:
#             nshat_P+=1
#             nshat_O==0
#         print(nshan, end='')
#     print()

# 79

# d=0
# n=int(input('Greq n arjeq: '))
# m=int(input('Greq m arjeq: '))
# if n>m:
#     d=n
# else:
#     d=m
#     while n % d != 0 or m % d != 0:
#         d -= 1
# print(d)



# Slaidi 7

# import random
# while True:
#     number=int(input('Greq tiv: '))
#     tiv=random.randint(1,10)
#     if number==tiv:
#         break
#     else:
#         print(tiv)
        
# Slaidi 1

# while True:
#     number = int(input('Greq tiv: '))
#     if number>=1:
#         print(number ** 3)
#     else:
#         break    

# Slaidi 2

# count=0
# Anun_Azganun=input('greq dzer anun@: ')
# Partq=int(input('Greq gumar: '))
# while True:
#     mucum=int(input('Greq gumar: '))
#     if Partq-mucum==0:
#         print('Duq partq chuneq')
#         break
#     elif Partq-mucum!=0:
#         print(int(input('Gumar@ bavara che nuric muceq: ')))
#         count-=Partq-mucum 
#         if count >= 0:
#             print('Duq partq chuneq')
#         else:
#             print(int(input('Gumar@ bavara che nuric muceq: ')))
#             count>=0
#             break

# Slaidi 3

# count=0
# tiv=input('greq tiv: ')
# for i in tiv:
#     if i.isdigit():
#         count+=i.isdigit()
# print(count)

# Slaidi 4

# gnahatoxneri_qanak=int(input('Mutqagreq gnahatoxneri qanak: '))
# count=0
# summ=0
# for i in range(gnahatoxneri_qanak):
#     while True:
#         ocenka=int(input('Greq -100 ic 100 mijakayqum gnahatakan: '))
#         if ocenka>0:
#             count+=1
#         elif ocenka<0:
#             summ+=1
# print(count)
# print(summ)