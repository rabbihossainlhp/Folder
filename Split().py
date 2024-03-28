line_for_try = "FirstProgram: Hello World"
final = line_for_try.split(":")
print(final)






# n1 = int(input())
# t = 0
# while t<n1:
#     print(t)
#     t+=1                          ###This tow type of loop is not connected with split
#
# n = int(input())
# for l in range(n):
#     print(l * l)

first_number = int(input())
second_number = int(input())
third_number = int(input())
if first_number>second_number and first_number>third_number:
    print("first number is big")
elif second_number>first_number and second_number>third_number:
    print("second number is big")
elif first_number==second_number==third_number:
    print("All number is same that you given")
elif first_number==second_number:
    print("first and second number is same")
elif first_number==third_number:
    print("first and third number is same")
elif second_number==first_number:
    print("second and first number is same")
elif second_number==third_number:
    print("secod and third number is same")
elif third_number==first_number:
    print("third and first number is same")
elif third_number==second_number:
    print("third and second number is same")
else:
    print("third number is big")


# another way to findout that which is biggest number
another_var = max(first_number,second_number,third_number)
if another_var==first_number==second_number==third_number:
    print("all number is same in here")
print(another_var)

