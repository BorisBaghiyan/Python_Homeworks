# x=10
# print(type(x))

# a=7.5
# print(type(a))

# b='Barev'
# print(type(b))

# print(type(9>5))


# name=input('greq dzer anun@: ')
# print('Barev',name)


# print('Anun\nAzganun')

# text='boris bagiyan'
# print(text.capitalize())
# print(text.upper())
# print(text.lower())
# print(text.title())

# number1=int(input('Greq dzer tiv@: '))
# number2=int(input('Greq dzer tiv@: '))
# print(number1+number2)


# number1=float(input('Greq dzer tiv@: '))
# number2=float(input('Greq dzer tiv@: '))
# print(number1+number2)

# qanak=int(input('Greq grichneri qanak: '))
# tokos=0.9
# print(f'Amboxj gumar = {qanak * tokos}$')

# name=input('Greq anun: ')
# tariq=int(input('Greq tariq: '))
# print(f'Barev {name} {tariq} tarekan')


# x=19
# y=7
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x**y)
# print(x//y)
# print(x%y)

# print(x<y)
# print(x>y)
# print(x>=y)
# print(x<=y)
# print(x!=y)
# print(x==y)


# balance=0
# balance +=2000
# print(balance)


# x= int(input('Greq tiv: '))
# print(x ** 0.5)

# x=6.71879234
# print(round(x, 4))


# number=int(input('Greq dzer tiv: '))
# print(number %2 == 0)


# print(5 & 6)



# number=int(input('greq tiv: '))
# print(f'{number * (number + 1)/2}')

# print(bool(5 and 7))

# print(bool(0))

# x=5
# y=7
# print(id(x))
# print(id(y))

# import math

# print(math.factorial(4))

# import math

# r=1809
# print(math.pi *r **2)

# r=74
# print(math.pi * r ** 2)

# print(math.e)
# print(math.pi)
# print(math.inf)
# print(math.nan)
# print(math.tau)

# print(math.log2(16))

# print(round(2.36))
# print(math.floor(2.89))
# print(math.ceil(1.0005))

# import datetime
# print(datetime.datetime.now())

# import time
# print(3)
# time.sleep(2)
# print(2)
# time.sleep(2)
# print(1)
# time.sleep(2)
# print('Start game!!!')
# time.sleep(1)

# import random

# random.seed(13)
# print(random.randint(1, 45))

# print(random.randrange(1, 100, 3))
# tareberak= 'qar', 'tuxt', 'mkarat' 
# print(random.choice(tareberak))

# x='4'
# print(x.isdigit())
# x='a'
# print(x.isdigit())
# print(x.isalpha())


# x='BAREV'
# print(x.isupper())
# x='barev'
# print(x.islower())
# x='GEXAM'
# print(x.islower())
# x='gexam'
# print(x.isupper())

# text='p,y,t,h,o,n'
# text=text.replace(',', '', 3)
# print(text)


# text='p,y,t,h,o,n'
# text=text.split(',')
# print(text)


# text='python'
# print(text[5])
# print(len(text))



# text='python'
# print(text[-3:])
# print(text[:5])
# print(text[::-1])
# print(text[:4:2])

# x=['p','y','t','h','o','n']
# print(''.join(x))
# print('$'.join(x))

# text='python39'
# text='python 3.9'

# print(text.isalnum())
# for x in range(10,1000):
#     print(x)

# for i in range(1,11):
#     print(i)



# for i in range(22, 5, -3):
#     print(i)




# for i in range(6, 100, 14):
#     print(i)




# count=0
# for i in range(1, 100):
#     if i % 5==0:
#         count +=1
# print(count)





# qanak=0
# for i in range(1,200):
#     if i % 4 == 0:
#         qanak +=1
# print(qanak)





# for i in range(1, 100):
#     if i % 36 == 0:
#         break
#     else:
#         print(i) 


# for i in range(1, 100):
#     if i % 36 == 0:
#         continue
#     else:
#         print(i) 


# number=(1,2,3,4,5,6,8,9)
# for i in number:
#     if i % 7 ==0:
#         print(i ,'ka')
#         break
# else:
#     print('chka')

# number=int(input("greq tiv: "))
# for i in range(2, int(number ** 0.5)+1):
#     print('Baxadryal')
#     break
# else:
#     print('Parz')



# number1=12
# number2=15
# for i in range(1,100):
#     if i % number1 == 0 and i % number2 == 0:
#         print(i)
#         break
# else:
#     print('Chak')


# kent=0
# zuyg=0
# for i in range(1,101):
#     if i % 2 == 0:
#         zuyg += 1
#     else:
#         kent += 1
# print(kent)
# print(zuyg)


# text = 'pythone 3.9'
# tar = 0
# tiv = 0
# nshan = 0
# for i in text:
#     if i.isdigit():
#         tiv += 1
#     elif i.isalpha():
#         tar += 1
#     else:
#         nshan +=1
# print(f'Tar={tar},Tiv={tiv},Nshan={nshan}')

# a = 0
# b = 1
# n = int(input('Greq tiv: '))
# for i in range(1,n+1):
#     print(a)
#     a,b = b, a+b


# count = 0
# for i in range(1,101, 4):
#     count+=1
#     print(i)
# print(count)


# a=int(input('Greq skzbi tiv: '))
# b=int(input('Greq verji tiv: '))
# summ=0
# count=0
# for i in range(a, b):
#     if i % 3 == 0:
#         summ += i
#         count += 1
# print(summ / count)

# a=int(input('Greq skzbnakan arjeq 1 - 4: '))
# b=int(input('Greq verjnakan arjeq 1 - 4: '))
# for i in range(a, b):
#     y=(i**3) + (2 * (i**2))-(4 * i) + 1
# print(y)




# summ=0
# krtatosak=int(input('Greq gumar: '))
# for i in range(1, 12):
#     if i>1:
#         summ=krtatosak * 3 // 100 
#         krtatosak += summ
# print(krtatosak)



# day=int(input('Greq shabatva oreric mek@ tvov 1-8: '))
# for i in (1,day,+1):
#     if i == 1:
#         print('Erkushabti')
#         break
#     if i == 2:
#         print('Ereqshabti')
#         break
#     if i == 3:
#         print==('Choreqshabti')
#         break
#     if i == 4:
#         print('Hingshabti')
#         break
#     if i == 5:
#         print('Urbat')
#         break
#     if i == 6:
#         print('Shabat')
#         break
#     if i == 7:
#         print('Kiraki')
#         break
#     else:
#         print('Mutqareq chisht tiv')
      
# 63, 64, 69, 75, 81, 82, 83, 84


# n1=int(input('Greq tiv: '))
# n2=int(input('Greq tiv: '))
# count=(n1 + n2) // 2
# while n1 > 0 or n2 > 0:
#     print(count)
#     break 



# n1=4.95 
# n2=9.95
# n3=14.95
# n4=19.95
# n5=24.95
# count1 = 0
# count2 = 0
# count3 = 0
# count4 = 0
# count5 = 0
# while n1 * 60 / 100 != 0:
#     count1 = n1 * 60 / 100
#     print(count1)
#     count2 = n2 * 60 / 100
#     print(count2)
#     count3 = n3 * 60 / 100
#     print(count3)
#     count4 = n4 * 60 / 100
#     print(count4)
#     count5 = n5 * 60 / 100
#     print(count5)
#     break

# price = 0
# while True:
#     tariq = int(input('Greq dzer tariq@: '))
#     if tariq <= 0:
#         break
#     elif 3 <= tariq <= 12:
#         price += 14
#     elif tariq >= 65:
#         price += 18
#     elif 12 < tariq < 65:
#         price += 23

# print(price)

# n1 = 12
# n2 = 15
# for i in range(15,n1 * n2 +1):
#     if i % 12 == 0 and i % 15 == 0:
#         print(i)
#         break

# count1=0
# count2=0
# for i in range(1,101):
#     if i % 2 == 0:
#         count1+=1
#     else:
#         count2+=1
# print(count2)
# print(count1)

# a = 0
# b = 1
# n = int(input('Greq tiv: '))
# for i in range(1,n+1):
#     print(a)
#     a,b = b, a+b


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
# count=0
# tiv=int(input('Greq tiv: '))
# for i in range(tiv,-1):
#     count=i[i]+i
# print(count)

# tariq = int(input('Greq dzer tariq@: '))
# ser= input('Greq ser Txa and Axjik: ')
# if 18<tariq<24 and ser == 'Txa':
#     print('Ashxatelu e qaxaqic durs')
# elif tariq>24 and ser == 'Axjik':
#     print('Qaxaqum')


# count=0
# ashxatavardz=int(input('Greq ashxatavardzi qanak: '))
# for i in range(1,13):
#     count=ashxatavardz * i
# print(count)


# tiv = int(input('Greq tiv: '))
# count = 1
# for i in range(1, tiv+ 1):
#     count *= (i)
# print(count)

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

# summ = 0
# count = 0
# a=int(input('Greq tiv: '))
# b=int(input('Greq tiv: '))
# for i in range(a,b):
#     if i % 3 == 0:
#         summ += i
#         count += 1
# print(summ / count)

# a=int(input('Greq tiv: '))
# b=int(input('Greq tiv: '))
# summ=(a ** 3)+(b ** 3)
# for i in range(10,100):
#     if summ % i == 0:
#         print(i)




# cart=int(input('Greq tiv 1-5: '))
# count1=0
# count2=0
# for i in range(cart-1):
#     tiv=int(input('Greq tiv; '))
#     count2+=tiv
# for i in range(1,cart + 1):
#     count1+=i
# print(count1-count2)


# n = 5
# summ1 = 0
# summ2 = 0
# for i in range(n - 1):
#     number = int(input('Enter catd: '))
#     summ2 += number
# for i in range(1, n + 1):
#     summ1 += i
# print(summ1 - summ2)

# hamar = int(input('Greq dzer hamar: '))
# for i in range(1,11):
#     if hamar % 2 == 0:
#         print('Lav')
#         break
# else:
#     print('Vat') 


# for i in range(1,101,4):
#     print(i)

# count=0
# partqatereri_qanak=int(input('Greq qanak: '))
# for i in range(1,partqatereri_qanak,5):
#     gumar=int(input('Greq gumar: '))
#     count += gumar
# print(f'Amboxj gumar@={count}')

# jamanak=int(input('Greq jamanak: '))
# for i in range(jamanak,-1,-1):
#     harc=int(input('0 sharunakel,1 patrast e'))
#     if harc == 0:
#         print('Patrast e')
#         break
#     else:
#         print(i)


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

# a=int(input('Greq tiv: '))
# b=int(input('Greq tiv: '))
# for i in range(a,b+1):
#     print(f'Y={i ** 3 + 2 * i ** 2 - 4 * i + 1}')


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


# n = 5
# a = 2
# s = 1
# for i in range(1,n + 1):
#     s += (1 / n) * ((-1) ** i)
#     a *= 2
# print(s)



# x=int(input('Greq dzer tiv@: '))
# res=(x-1)/(x-2)
# for i in range(1,x+1):
#     res+=2
# print(res)
    
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

# text = input('Greq bar: ')
# polidrom = True
# for i in range(len(text) // 2):
#     if text[i] != text[-(i + 1)]:
#         polidrom = False
#         break
# if polidrom:
#     print('Polidrom')
# else:
#     print('Polidrom chi')



# a=2
# b=3
# c=4
# p=3
# P=p+(4/(a*b*c))
# for i in range(1,16):
#     a+=2
#     b+=2
#     c+=2
#     if i % 1 == 0:
#         P*=-1
#         P+=(4/(a*b*c))
# print(P*-1)

# for i in range(0,6):
#     for j in range(0,11,2):
#         print(f'{i+j:>4}',end='')
#     print()

# n=int(input('Greq tiv: '))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==j:
#             print(j,end='')
#         elif i>=j:
#             print(j,end=' ')
#     print()

# for i in range(1,12):
#     print('|',end='')
#     for j in range(1,21,):
#         print('-',end='')
#     print()




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


# count=0
# n=int(input('Greq tiv: '))
# while True:
#     if n<2:
#         break
#     elif n>2:
#         count+=n%2
#         print(count)
#         count==0
#         break

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



# import random
# while True:
#     number=int(input('Greq tiv: '))
#     tiv=random.randint(1,10)
#     if number==tiv:
#         break
#     else:
#         print(tiv)


# while True:
#     number = int(input('Greq tiv: '))
#     if number>=1:
#         print(number ** 3)
#     else:
#         break

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


# count=0
# tiv=input('greq tiv: ')
# for i in tiv:
#     if i.isdigit():
#         count+=i.isdigit()
# print(count)

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


# n=int(input('greq tiv: '))
# for i in range(1,n):
#     if n % i ==0:
#         print(True)
#     else:
#         print(False)


# count=[]
# summ=[]
# while True:
#     number=(input('Greq tiver: '))
#     if number=='':
#         print('Verj')
#         break
#     else:
#         count.append(int(number)//2)
#         summ.append(int(number))
#         print(count)
#         print(summ)


# mylist=[]
# while True:
#     bar=input('greq bar: ')
#     mylist.append(bar)
#     print(' i '.join(mylist))
    

# import random

# lottery_ticket = []
# while len(lottery_ticket) < 6:
#     number = random.randint(1, 49)  
#     if number not in lottery_ticket:  
#         lottery_ticket.append(number)
# lottery_ticket.sort()
# print(lottery_ticket)



# mydict_={
#     'D':56,
#     'E':12,
#     'F':69,
#     'C':45,
#     'B':23,
#     'A':67
# }
# sort=sorted(mydict_.get, reverse=True)[:3]
# newdict={}
# for i in sort:
#     newdict[i]=mydict_
# print(newdict)      


# s = 'a,2,b,5,c,8,a,4,e,11'
# s=s.split(',')
# mydict={}
# for i in range(0,len(s),2):
#     if s[i] in mydict:
#         mydict[s[i]]+=int(s[i+1])
#     else:
#         mydict[s[i]]=int(s[i+1])
# print(mydict)
# print(s)
    

# import random
# tiv = {
#     2:0,
#     3:0,
#     4:0,
#     5:0,
#     6:0,
#     7:0,
#     8:0,
#     9:0,
#     10:0,
#     11:0,
#     12:0
# }
# for i in range(1000):
#     zar1 = random.randint(1,6)
#     zar2 = random.randint(1,6)
#     tiv[zar1+zar2]+=1
# print(tiv)

# tar={
#     '1':'.,?!:',
#     '2':'ABC',
#     '3':'DEF',
#     '4':'GHI',
#     '5':'JKL',
#     '6':'MNO',
#     '7':'PQRS',
#     '8':'TUV',
#     '9':'WXYZ',
#     '0':' '
# }
# bar=input('Greq bar: ').upper()
# for i in bar:
#     for j in tar:
#         if i in tar[j]:
#             print(j * (tar[j].index(i)+1),end='')


# text='Barev Boris'
# textdict={}
# for i in text:
#     if text.count==i:
#         textdict.update(text)
# print(textdict)



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
        
# def taxi(km):
#     minimal=4
#     return minimal+(km*1000/140)*0.25
# print(taxi(12))


# def ux_er(a,b,c):
#     if a**2+b**2==c**2:
#         return'Uxankyun eraknkyun'
#     elif a**2+b**2!=c**2:
#         return'Uxankyun eraknyun chi'
# print(ux_er(1,4,5))

# def patver(count):
#     apranq=10.95
#     return apranq+(count-1)*2.95
# print(patver(14))

# def mijin():
#     return (a+b+c)//3
# a=int(input('Greq tiv: '))
# b=int(input('Greq tiv: '))
# c=int(input('Greq tiv: '))
# print(mijin())

print(10)





            


            



    




   




