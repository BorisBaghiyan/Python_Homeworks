# 1

# for i in range(1,101,4):
#     print(i)

# 2

# count=0
# partqatereri_qanak=int(input('Greq qanak: '))
# for i in range(1,partqatereri_qanak,5):
#     gumar=int(input('Greq gumar: '))
#     count += gumar
# print(f'Amboxj gumar@={count}')

# 3

# jamanak=int(input('Greq jamanak: '))
# for i in range(jamanak,-1,-1):
#     harc=int(input('0 sharunakel,1 patrast e'))
#     if harc == 0:
#         print('Patrast e')
#         break
#     else:
#         print(i)

# 4

# a=int(input('Greq tiv: '))
# b=int(input('Greq tiv: '))
# c=int(input('Greq tiv: '))
# count=0
# summ=0
# for i in range(a,b+1):
#     if i % c == 0:
#         count+=i
#         summ+=1
# print(count / summ)

# 5

# a=int(input('Greq tiv: '))
# b=int(input('Greq tiv: '))
# for i in range(a,b+1):
#     print(f'Y={i ** 3 + 2 * i ** 2 - 4 * i + 1}')

# 6

# crarki_chap = 12
# for i in range(2):
#     chap = float(input('Greq crari qanak: '))
#     if i == 0:
#         lenutyun = chap
#     else:
#         erkarutyun = chap
#         calelu_erkar = lenutyun,crarki_chap
#         calelu_len = erkarutyun,crarki_chap
#         qanak_calelu = calelu_erkar, calelu_len
#         print(qanak_calelu)

# 7

# summ=0
# krtatosak=int(input('Greq gumar: '))
# for i in range(1, 12):
#     if i>1:
#         summ=krtatosak * 3 / 100 
#         krtatosak += summ
# print(krtatosak)

# 8

# n = 5
# a = 2
# s = 1
# for i in range(1,n + 1):
#     s += (1 / n) * ((-1) ** i)
#     a *= 2
# print(s)

# 9

# x=int(input('Greq dzer tiv@: '))
# res=(x-1)/(x-2)
# for i in range(1,x+1):
#     res+=2
# print(res)

# 10

# txa=int(input('Greq qanak: '))
# axjik=int(input('Greq qanak: '))
# nshan=''
# if txa==axjik:
#     for i in range(txa):
#         nshan += 'BG'
# elif txa - axjik == 1:
#     for i in range(axjik):
#         nshan+='BG'
#     for i in nshan:
#         if i == 'G':
#             nshan+='B'
#             break
# elif txa - axjik == 2:
#     for i in range(axjik):
#         if i == 'G':
#             nshan+='B'
#             break
# elif txa - axjik == 3:
#     for i in range(axjik):
#         if i == 'G':
#             nshan+='B'
#             break
# else:
#     print('hnaravor che')
# print(nshan)
# -------------------------------------------------------------------------------------------------------------------------------


