# number = int(input("Enter the number:"))
# sum = 0
# i = 1
#
# for i in range(number):
#     sum = sum+i
# print(sum)

# '''import math
# a = int(input("Enter the value of a "))
# b = int(input("Enter the value of b"))
# c = int(input("Enter the value of c"))
#
# d = b*b-4*a*c
#
# if d>0:
#     aa1 = -2+math.sqrt(d)/2*a
#     aa2 = -2-math.sqrt(d)/2*a
#     print((aa1,aa2))
# elif d==0:
#     aaa = -b/2*a
#     print(aaa)
# else:
#     print("Roots are imaginery..")'''
'''fdsf'''

#
# user_in = int(input())
# if user_in > 0:
#     print("The number is positive")
# elif user_in < 0:
#     print("The number is Negative")
# else:
#     print("The number is JJero")
#
#
# first_in = int(input("FIrst number:"))
# second_in = int(input("SEcond number:"))
# third_in = int(input("THird number:"))
#
# if first_in> second_in and first_in>third_in :
#     print("FIrst number is BIg")
# elif second_in>first_in and second_in>third_in:
#     print("SEcond number is BIg")
# else:
#     print("Third number is BIg")



#another Proogramme::::

# n = int(input("Enter your range:"))
# sum = 0
# for i in range(1,n+1):
#     sum+=i
# print("The number is : ", sum)

#
#
# def factorial(n):
#     if n == 0 or n==1:
#         return 1
#     else:
#         return ( n* factorial(n-1))
#
# number = int(input("for f num:"))
# print("The Factorial is :" ,factorial(number))

first_i = int(input("Enter A:"))
second_i = int(input("Enter B:"))
third_i = int(input("Enter C:"))

if first_i>second_i and third_i:
    print("A is BIG")
    if first_i == second_i == third_i:
        print("All number are Similar:")
    elif first_i == second_i:
        print("A&B is similar")
    elif second_i == third_i:
        print("B&C is similar")
    elif third_i == first_i:
        print("A&C is similar")
elif second_i>third_i and first_i:
    print("B is BIG")
    if first_i == second_i == third_i:
        print("All number are Similar:")
    elif first_i == second_i:
        print("A&B is similar")
    elif second_i == third_i:
        print("B&C is similar")
    elif third_i == first_i:
        print("A&C is similar")

else:
    print("C is BIG")
    if first_i == second_i == third_i:
        print("All number are Similar:")
    elif first_i == second_i:
        print("A&B is similar")
    elif second_i == third_i:
        print("B&C is similar")
    elif third_i == first_i:
        print("A&C is similar")

from datetime import  time
ff = time
print(ff)