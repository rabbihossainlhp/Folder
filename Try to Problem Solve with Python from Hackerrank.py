##from this plartform some problem did solve in previous time,,,,,,,,

#1st Problem
#if else
# n = int(input("Just drop your thinking number to ditect that is it even or odd::"))
#
# if n%2!=0:
#     print("Weird")
# elif n%2==0 and 2<=n<=5:
#     print("Not Weird")
# elif n%2==0 and 6<=n<=20:
#     print("Weird")
# elif n%2==0 and n>20:
#     print("Not Weird")         ##Accepted##

#2nd Proble
#write a functon

# def is_leap(y):
#     if y%4 == 0:
#         return True
#     elif y%400 == 0:
#         return True
#     elif y % 100 == 0:
#         return False      #......without this statesment this programme will run safely.....#
#     return False
#
# year =int(input())
# print(is_leap(year))
#
# ## new another function to ditected the leap year
# def iisleap(u):
#     if u%4==0:
#         return True
#     if u%400==0:
#         return
#     if u%100==0:
#         return False
#     return False
#
# p = int(input())
# print(iisleap(p))
#
#
# ##another function for learn
# def is_leap(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False
#
# # Read the input year
# year = int(input())
#
# # Check if it's a leap year and print the result
# print(is_leap(year))



#3rd Problem
#Arithmetics operator

# n = int(input())
# for i in range(n):
#     i*=i
#     print(i)       ##...Accepted...#


#4th problem
#swap_case
# Ul_case = str(input())
# New_Ul = Ul_case.swapcase()
# print(New_Ul)                   ##..Accepted..#


##5th problem
#Lists
# my_list=[]
# n = int(input())
#
# for i in range(n):
#     cd = input().split()
#     ncd = cd[0]
#     if ncd =="insert":
#         i,e = map(int,cd[1:])
#         my_list.insert(i,e)
#     elif ncd == "print":
#         print(my_list)
#     elif ncd=="remove":
#         e = int(ncd[1])
#         my_list.remove()
#     elif ncd == "append":
#         e = int(ncd[1])
#         my_list.append(e)
#     elif ncd == "sort":
#         my_list.sort()
#     elif ncd == "pop":
#         my_list.pop()
#     elif ncd == "reverse":
#         my_list.reverse()...........#do not und#


#6th Problem
#Full Name
'''
first_name = input()
last_name = input()

def full_name(first,last):
    print(f"Hello {first}{last}! you just delved into python")

print(f"Hello {first_name+last_name}!you just delved into python")        #did not accepted
full_name(first_name,last_name)                                              #did not accepted
'''



#7th Problem
#Runner up scores finder
#
# n = int(input())
# s = map(int,input().split())
# '''sLine = list(set(s))
# sLine.sort()
# print(sLine[-2])'''
#
# score = []
#
# for i in s:
#     if i not in score:
#         score.append(i)
#         print(score)
# score.sort()
# print(score[-2])



## Fizz  and buzz from hackerrank's certification simple try
# Bismillahir rahmanir rahim


'''User_input = int(input())

for l in range(1,User_input+1):
    print(l)
    User_input = int(input())
    if User_input%3 == 0 and User_input%5 ==0:
        print("FizzBuzz")
    elif User_input%3 == 0 and User_input%5 != 0:
        print("Fizz")
    elif User_input%3 != 0 and User_input%5 == 0:
        print("Buzz")
    else:
        print(l)'''                                      '''This code is invalid'''


                  ### both are the same problem just first solution done by using simple methode and the next
                         # solution is done by using a function method .... That's all
# def fizzBuzz(User_input):
#     for l in range(1, User_input + 1):
#             if l % 3 == 0 and l % 5 == 0:
#                 print("FizzBuzz")
#             elif l % 3 == 0 and l% 5 != 0:
#                 print("Fizz")
#             elif l % 3 != 0 and l % 5 == 0:
#                 print("Buzz")
#             else :
#                 print(l)
#
#
# #v = int(input())
# #fizzBuzz(v)
#                                                     ## I think it will be really helpfull ##
#
#
#                             ##neww problem
#
# def filledOrders(order, k):
#     order.sort()
#     fulfilledOrders = 0
#     for o in order:
#         if k >= o:
#             k -= o
#             fulfilledOrders += 1
#         else:
#             break
#
#     return fulfilledOrders                  ### this all problems are not effected right now just have to tryanna new solution
#
# orders = [30, 10, 40]
# available_widgets = 40
# result = filledOrders(orders, available_widgets)
# print(result)
#
# t = "my is name"
# s = t.swapcase()
# aa = "" .join(reversed(s))
# print(aa)


'''kk = " runs dogs"
spliti = kk.split()
reverso = reversed(spliti)
joi = "".join(reverso)

print(joi)

'''                                              ##not solved#


##another problem from hackerrank
#'''#capitali..tion
'''def capitalize_name(full_name):
    user_input = full_name.split()
    capital_word = " ".join(word.capitalize() for word in user_input)
    return capital_word




N = input()
print((capitalize_name(N)))'''


# def solution (s):
#     g = s.capitalize()
#     print(g)
#
# ij = input()
# solution(ij)                      ### did not know about capitalise method ##




# again = int(input("Enter number:"))
# again_again = int(input("Enter one more number:"))
#
# for i in range(again):
#     if i%2 ==0:
#         continue
#     print(i)
#


#This is actually new problem from a relative bro,,,

user_input = input("Enter the Strings")
Cap_letters = ""
Sma_letters = ""
Digits = ""
Spec_chars = ""

for i in user_input:
    if i.isupper():
        Cap_letters+=i
    elif i.islower():
        Sma_letters+=i
    elif i.isdigit():
        Digits+=i
    else:
        Spec_chars+=i
#Now time to print result....
print(Cap_letters)
print(Sma_letters)
print(Digits)
print(Spec_chars)



