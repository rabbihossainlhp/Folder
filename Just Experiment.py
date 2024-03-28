# New_word = "G"
# Opper = 3
# Add = []
# cl = False
#
# while cl:
#     for Ad in New_word:
#         if Ad in Ad.lower():
#             print(Ad,end = " ")
#         else:
#             print(Ad,end = "")
#
#     Guesting = input(f"You have only {Opper} chances.....Enter Your Guessting Number::")
#     Add.append(Guesting.lower())
#     if Guesting.lower() not in New_word.lower():
#         Opper -= 1
#         if Opper == 0:
#             break
#
#     cl = True
#     for Ad in New_word:
#         if Ad.lower() in New_word:
#             cl = False
# if cl:
#     print(f"You win Your Giving Number is {Add}")
# else:
#     print("You loss")






#input value of R

n = int(input())
r = ""
dy = list(range(1,n+1))
for ii in dy:
    r+=str(ii)
print(r)                 ##actually that was a problem from hackerrank and finally done...................
