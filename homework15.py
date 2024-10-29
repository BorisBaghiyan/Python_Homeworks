# 86

# def taxi(km):
#     minimal=4
#     return minimal+(km*1000/140)*0.25
# print(taxi(12))

# 85

# def ux_er(a,b,c):
#     if a**2+b**2==c**2:
#         return'Uxankyun eraknkyun'
#     elif a**2+b**2!=c**2:
#         return'Uxankyun eraknyun chi'
# print(ux_er(1,4,5))

# 87

# def patver(count):
#     apranq=10.95
#     return apranq+(count-1)*2.95
# print(patver(14))

# 88

# def mijin():
#     return (a+b+c)//3
# a=int(input('Greq tiv: '))
# b=int(input('Greq tiv: '))
# c=int(input('Greq tiv: '))
# print(mijin())

# 98,99  chi stacvel 

# def is_prime(number):
#     if number <= 1:
#         return False
#     if number == 2:
#         return True
#     if number % 2 == 0:
#         return False
#     for i in range(3, int(number ** 0.5) + 1, 2):
#         if number % i == 0:
#             return False
#     return True
# if __name__ == "__main__":
#     number = int(input('Greq tiv: '))
#     if is_prime(number):
#         print(f"{number}")
#     else:
#         print(f"{number}")