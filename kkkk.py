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

# 137


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


# 138


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




