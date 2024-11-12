# 149,150

# def head(file):
#     try:
#         with open('myfile.txt','r') as newfile:
#             print(newfile.read())
#     except:
#         print('Tenc file chka')
# head(input('Greq File anun: '))

# 151

# def head(file):
#     try:
#         with open('myfile.txt','r') as newfile:
#             print(newfile.read())
#     except:
#         with open('myfile.txt','r') as newfile1:
#             x=newfile1.readlines()[:10]
#         x=''.join()
#         with open('newfile.txt','w') as newfile2:
#             newfile2.write(x)
#             print(newfile2.txt())
# head(input('Greq File anun: '))

# 152

# with open('myfile.txt','r')as file1:
#     mylist=file1.readlines()
# with open('new_myfile.txt','a')as file2:
#     for i in range(len(mylist)):
#         file2.write(f'{i+1}.{mylist[i]}')

# 153

# with open('myfile.txt','r') as file:
#     f=file.readlines()
# for i in range(1):
#     print(max(f))


# 154,155

# def files(filename):
#     try:
#         with open('myfile.txt','r') as file:
#             f=file.read().replace('\n',' ').split(' ')
#             mydict={i:f.count(i) for i in f}
#         print(sorted(mydict, key=mydict.get)[-1])
#     except:
#         print('Error')
# files(input('greq file anun: '))

# 156 harc ka---------

with open('myfile.txt','r')as file:
    x=file.read().replace('\n',' ').split(' ')
    x.sort()
    print(x)
