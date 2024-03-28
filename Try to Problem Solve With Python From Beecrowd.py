#from today tryanna solve some problem with python programming

                                               ##   from beecrowd!   ##
### onemore thing that, in here all the problem and there solve is not consistance from "beecrowd" > this is just solve for my benifites bcz one n only reason of it is I have no enough Internet resource right now###

#First Problem>>1000
#print(Hello World)...........................................................................
#
# X = "Hello World!"
# print(X)            #........Accepted......#
#
#
#
# #Second Problem>>1002
# #Area of circle...........................................................................
# n = 3.13421
# R = float(input())
# A = n*R**2
# print("A =",A)     #........Accepted......#
#
#
#
# #Third Problem>>1003
# #Simple Sum...........................................................................
# a = int(input())
# b = int(input())
# SOMA = a+b
# print("SOMA =",SOMA)   #........Accepted......#
#
#
#
# #Fourth Problem>>1004
# #Simple Product...........................................................................
# x = int(input())
# y = int(input())
# PROD = x*y
# print("PROD =",PROD)      #........Accepted......#
#
#
#
# #Fifth Problem>>1007
# #Difference...........................................................................
# Aa = int(input())
# Bb = int(input())
# Cc = int(input())
# Dd = int(input())
# DIFERENCA = (Aa*Bb-Cc*Dd)
# print("DIFERECA =",DIFERENCA)    #........Accepted......#



#Sixth Problem>>1008
#Salary...........................................................................
# a = int(input())
# b = int(input())
# c = float(input())
# aa = b*c
# print("NUMBER =",a)
# print("SALARY = U$ {:.2f}".format(aa))   #........Accepted......#


# #7th Problem>>1009
# #Salary with Bonus...........................................................................
# name_of_seller = input()
# total_salary = float(input())
# total_commision_from_sell = float(input())
# another_calculation = total_salary+(total_commision_from_sell*0.15)
# print("TOTAL = R$ {:.2f}".format(another_calculation))                     #........Accepted......#




#8th Problem>>1010
#Simple Calculate...........................................................................

'''product1 = int(input()),int(input()),float(input())
product2 = int(input()),int(input()),float(input())
print(product1,product2)'''



#9th Problem>>1011
#Sphere...........................................................................
#
# R = float(input())
# pi =3.14159
# calculate_volume = (4/3)*pi*(R*R*R)
# print("VOLUME = {:.3f}".format(calculate_volume))    #........Accepted......#



#10th Problelm>>1013
#The Greatest...........................................................................

# a,b,c = map(int,input())
# print(c)
# print(a)
# print(b)                                             #........Uncompleated.......#



'''
n = list(range(1,21))         ##This all is not involved in this problem solve code###
print(n)                       ##This all is not involved in this problem solve code###
def ghy (h):                    ##This all is not involved in this problem solve code###
    return h*h*h                 ##This all is not involved in this problem solve code###
nnew = map(ghy,n)                 ##This all is not involved in this problem solve code###
print(list(nnew))                  ##This all is not involved in this problem solve code###
                                    ##This all is not involved in this problem solve code###
# def ff(c):                      ##This all is not involved in this problem solve code###
#     return c*c*c               ##This all is not involved in this problem solve code###
# ncube = map(ff,n)             ##This all is not involved in this problem solve code###
# print(ncube)                 ##This all is not involved in this problem solve code###
# h=list(ncube)               ##This all is not involved in this problem solve code###
# print(h)                   ##This all is not involved in this problem solve code###
'''                         ##This all is not involved in this problem solve code###



#11th Problem>>1015
#Distance between tow points...........................................................................


# x1 = float(input())
# y1 = float(input())
#
# calculation = y1-x1
#
# print("{:.4f}".format(calculation))                                #....Uncompleated....#








#12th problem>>1012
#Area...........................................................................




#13th Problem>>1005
#Avareg...........................................................................

# A = float(input("Input Your First Number:"))
# B = float(input("Input Your Second Number:"))
#
# Gread_first = (A * 3.5 + B * 7.5)/(3.5+7.5)
# print("MEDIA = {:.5f}".format(Gread_first))                          #.....Accepted........#



#14th Problem>>1014
#Consumption...........................................................................

# X = int(input())
# Y = float(input())
#
# consump = X/Y
# print("{:.3f} km/l".format(consump))                               #.......Accepted......#


#15th Problem>>1017
#Fule Spent...........................................................................

# Time_spend_in_the_trip = int(input())
# Avarage_speed_during_in_the_trip = int(input())
#
# Total_Distance = Time_spend_in_the_trip * Avarage_speed_during_in_the_trip
# F_calculate = Total_Distance/12
#
# print("{:.3f}".format(F_calculate))
# print(f"{F_calculate:.3f}")                                      #.....Accepted......#


#16th Problem>>1019
#Time conversion...........................................................................

# N = int(input())
# hours = N//3600
# N %= 3600
# minutes = N//60
# N %=60
# print(f"{hours}:{minutes}:{N}")                  #....Accepted....#


#17th Problem>>Un
#Age in days...........................................................................

'''days = int(input())
year = days//365
days %= 365
month = days//30
days %=30
print(year,"ano(s)")
print(month,"mes(s)")
print(days,"dia(s)")'''                              #...did not submited...#


#18th Problem>>Un
#Selection test 1...........................................................................

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# if b>c and d>a:
#     if (c+d)>(a+b):
# elif c,d is == !+:


#19t Problem
#Snack...........................................................................
#
# product_Table ={
#     1: 4.00,
#     2: 4.50,
#     3: 5.00,
#     4: 2.00,
#     5: 1.50
# }
# x = int(input("Product code"))
# y = int(input("Product quantity"))
#
# total_price = product_Table.get(x,0)*y
# print(f"Total:R$ {total_price:.2f}")             #.....Un....#



##20th Problem
#Simple sort...........................................................................
# first_number = list(map(int,input().split()))
# the_sorted_number = sorted(first_number)
# for for_list_m in the_sorted_number:
#     print(for_list_m)
# print()
# for num in first_number:
#     print(num)                                   ##Accepted##

#21th Problem
#Multiples...........................................................................

# A, B = map(int, input().split())
#
# if A % B == 0 or B % A == 0:
#     print("Sao Multiplos")
# else:
#     print("Nao sao Multiplos")         ##Accepted##
#
# ### Another way to solve this problem
#
# a,b = map(int,input().split())
# if a % b == 0:
#     print("Sao Multiplos")
# elif a % b == 0 :
#     print("Sao Multiplos")
# else:
#     print("Nao sao Multiplos")###############Donno that what is the problem in this code



#22th Problem
#Odd Numbers...........................................................................

# x = int(input())
# for line_b_ in range(x):
#     if line_b_%2 != 0:
#         print(line_b_)
#
#
# X = int(input())
# for number in range(1, X + 1, 2):
#     print(number)             #,,,,this code accepted,,,,#

#23th Problem
#six odd numbers...........................................................................

# X = int(input())
# another_X = range(X,X+12)
# for i in another_X:
#     if i%2 !=0:
#         print(i)                     ##Accepted##


#24th Problem
#even number...........................................................................

# for i in range(2,102,2):
#     print(i)                       #Accepted###

#25th Problem
#even squre...........................................................................
# N = int(input())
# for calN in range(2,N+2):
#     if calN%2==0:
#         calculationN = calN*calN
#         print(f"{calN}^{2} = {calculationN}")              #Accepted#


#26th Problem
#five even numbers...........................................................................

# ec = 0
# for _ in range(5):
#     nu = int(input())
#
#
#     if nu%2==0:
#         ec=ec+1
#
# print(f"{ec} valores pares")             ##Accepted##



# 27th Problem
# DDD phone calling location showing...........................................................................

#
# code_number_for_phone_calling ={
#     61: "Brasilia",
#     72: "Salvador",
#     11: "Sao Paulo",
#     21: "Rio de Janeiro",
#     32: "Juiz de Fora",
#     19: "Campians",
#     27: "Vitoria",
#     31: "Belo Horizonte"
# }
# User_input = int(input("Just type a integer type key for finding:"))
# p = code_number_for_phone_calling
# if User_input in code_number_for_phone_calling:
#     print(p.get(User_input))
# else:
#     print("DDD nao cadastrado")                                                  ##all clear but donno that why did not accepted###



# 28th Problem
#odd,even , positive,negative............................................................................

# N = int(input())
# for i in range(N):
#     X = int(input())
#
#     if X==0:
#         print("NULL")
#     elif X % 2 == 0:
#         if X>0:
#             print("EVEN POSITIVE")
#         else:
#             print("EVEN NEGATIVE")
#     else:
#         if X>0:
#             print("ODD POSITIVE")
#         else:
#             print("ODD NEGATIVE")                   ##Accepted##

#
#
# # ##another solving code of this problem:
# # New = int(input())
# # for ii in range(New):
# #     another_ii = int(input())
# #
# #     if another_ii == 0:
# #         print("NULL")
# #     elif another_ii % 2 == 0 and another_ii > 0:
# #         print("EVEN POSITIVE")
# #     elif another_ii % 2 == 0 and another_ii < 0:
# #         print("EVEN NEGATIVE")
# #     elif another_ii % 2 != 0 and another_ii > 0:
# #         print("ODD POSITIVE")
# #     else:
# #         print("ODD NEGATIVE")                         ##Both was accepted##
#
#
#
# # 29th Problem
# #Highest and position............................................................................
# #
#
# # collect_from_loop = []
# #
# # for i in range(3):
# #     User_input = int(input())
# #     collect_from_loop.append(User_input)
# #
# # Determine_maximum = max(collect_from_loop)
# # len_determiner = len(str(Determine_maximum))
# # print(Determine_maximum)
# # print(len_determiner - 1)                            ###did not accepted donno why###
#
# #another way to solving this
# max_num = -1
# max_position = 0
#
# for position in  range(1,4):
#     num = int(input())
#     if num>max_num:
#         max_num = num
#         max_position = position
#
# print(max_num)
# print(max_position)


# # 30th Problem
# #The Greatest............................................................................
# first,second,third = map(int,input().split())
# print(max(first,second,third), "eh o maior")                          ## simple problem bt did not submit##


##31th Problem
##Experiment

'''
total_animal = 0
total_rabit = 0
total_rat = 0
total_frog = 0

N = int(input())
for r in range(N):
    amount,animal_type = input().split()
    amount = int(amount)
    animal_type = str(animal_type)

    total_animal += amount
    ## Now we have to use some condition for define an integer type and a string type

    if animal_type == "C":
        total_rabit += amount
    if animal_type == "R":
        total_rat += amount
    if animal_type == "S":
        total_frog += amount

percentage_0f_rabit = (total_rabit/total_animal)*100
percentage_of_rat = (total_rat/total_animal)*100
percentage_of_frog = (total_frog/total_animal)*100


print(f"Total: {total_animal} cobaias")
print(f"Total de coelhos: {total_rabit}")
print(f"Total de ratos: {total_rat}")
print(f"Total de sapos: {total_frog}")
print(f"Percentual de coelhos: {percentage_0f_rabit:.2f} %")
print(f"Percentual de ratos: {percentage_of_rat:.2f} %")
print(f"Percentual de sapos: {percentage_of_frog:.2f} %")                          ##Acceopted##



##32th Problem
##Banknotes..
#
#

N = int(input("Please import your money number it will automatically convert in notes: okey"))

hundred = N//100
fiftee = N%100
fifteefi = fiftee//50
twenti = fiftee%50
twentifi = twenti//20
ten = twenti%20
tenfi = ten//10
five = ten%10
fivefi = five//5
two = five%5
towfi = two//2
one = two%2
onefi  = one//1

print(N)
print(f"{hundred} nota(s) de R$ 100,00")
print(f"{fifteefi} nota(s) de R$ 50,00")
print(f"{twentifi} nota(s) de R$ 20,00")
print(f"{tenfi} nota(s) de R$ 10,00")
print(f"{fivefi} nota(s) de R$ 5,00")
print(f"{towfi} nota(s) de R$ 2,00")
print(f"{onefi} nota(s) de R$ 1,00")                      #Accepted##





######Another way to solve this problem##
N = int(input())

banknotes = [100,50,20,10,5,2,1]

print(N)

for note in banknotes:
    count = N // note
    N %= note
    print(f"{count} nota (s) de R$ {note},00")                ## this is also logical##




'''
#
#
#
#
#
#
#
#
#
#
#
#

'''

def operation(selecthn):
    print(f"{selecthn} salar pagol re etodin pore toke k aste koiche ekhane ha sumin")

aaha = input("after too much day letar")

this_is = "Allah please save our palestine's brothers and sister"
def iii__printting(anythings):
    print(anythings)

iii__printting(this_is)'''

##
##
##
##
##
##
##
##
##
##
##
##33th Problem
#sum of od numbers

# first_integer = int(input("first value:"))
# second_integer = int(input("second value:"))
# convert_into_list = []
#
#
# for i in range(first_integer+1,second_integer):
#     if i%2 !=0:
#         convert_into_list.append(i)
# print(sum(convert_into_list))                            ##compleated but still did not submitted##


#
# total_animal = 0
# total_rabit = 0
# total_rat = 0
# total_frog = 0
#
# N = int(input("jsut no:"))
# for r in range(N):
#     amount,animal_type = input().split()
#     amount = int(amount)
#     animal_type = str(animal_type)
#
#     total_animal += amount
#     ## Now we have to use some condition for define an integer type and a string type
#
#     if animal_type == "C":
#         total_rabit += amount
#     if animal_type == "R":
#         total_rat += amount
#     if animal_type == "S":
#         total_frog += amount
#
# percentage_0f_rabit = (total_rabit/total_animal)*100
# percentage_of_rat = (total_rat/total_animal)*100
# percentage_of_frog = (total_frog/total_animal)*100
#
#
# print(f"Total: {total_animal} cobaias")
# print(f"Total de coelhos: {total_rabit}")
# print(f"Total de ratos: {total_rat}")
# print(f"Total de sapos: {total_frog}")
# print(f"Percentual de coelhos: {percentage_0f_rabit:.2f} %")
# print(f"Percentual de ratos: {percentage_of_rat:.2f} %")
# print(f"Percentual de sapos: {percentage_of_frog:.2f} %")








##............Simple calculator..........##
#
# First_Input = int(input("Enter number:"))
# Operator = str(input("Select an operator: +, -, *, /"))
# Second_Input = int(input("Enter number"))
#
# if Operator == "+":
#     print(First_Input + Second_Input)
# elif Operator == "-":
#     print(First_Input - Second_Input)
# elif Operator == "*":
#     print(First_Input * Second_Input)
# elif Operator == "/":
#     print(First_Input / Second_Input)
# else:
#     print("Something else please check again & try again::")           ##It was really very simple calculator by using pythone:
#


#Again try this problem
# 28th Problem
#odd,even , positive,negative............................................................................

for i in range(5):
    user_input = int(input())
    if user_input > 0 and user_input%2 == 0:
        print('EVEN Positive')
    elif user_input >0 and user_input%2 != 0:
        print('ODD Positive')
    elif user_input <0 and user_input%2==0:
        print('Even Negative')
    elif user_input <0 and user_input%2 !=0:
        print('ODD Negative')
    else:
        print('The number is zero')