# 110

# count=[]
# while True:
#     number=int(input('greq tver: '))
#     if number==0:
#         break
#     count.append(number)
#     count.sort()
# print(count)

# 112 chi stacvel 

# count=[]
# while True:
#     number=int(input('greq tver: '))
#     if number<4:
#         print("Sxal qanaki arjeq")
#         break
#     count.append(number)
#     for i in count:
#         for j in count:
#             if count[j]<count[j+1]:
#                 count[j],count[j+1]==count[j+1],count[i]
#     print(count)


# 113

# text_list=[]
# while True:
#     text = input('Greq bar: ').lower()
#     if text== '':
#         break
#     if text not in text_list:
#         text_list.append(text)
#         continue
# print(text_list)

# 116

# n=int(input('greq tiv: '))
# for i in range(1,n):
#     if n % i ==0:
#         print(True)
#     else:
#         print(False)

# 119

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


# 120

# mylist=[]
# while True:
#     bar=input('greq bar: ')
#     mylist.append(bar)
#     print(' i '.join(mylist))

# 121

# import random

# lottery_ticket = []
# while len(lottery_ticket) < 6:
#     number = random.randint(1, 49)  
#     if number not in lottery_ticket:  
#         lottery_ticket.append(number)
# lottery_ticket.sort()
# print(lottery_ticket)
    
