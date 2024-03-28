import math

a = int(input())
b = int(input())
c = int(input())
d = b*b-4*a*c
if d>0:
    x1 = -b+math.sqrt(d)/2*a
    x2 = -b-math.sqrt(d)/2*a
    print(x1)
elif d==0:
    x = -b*(2+b)
    print(x)
elif d<0:
    print("Not correct")

# if a+b>c and a+c>b and c+b>a:
#     s = (a+b+c)/2
#     area = math.sqrt((s-a)*(s-b)*(s-c))
#     print(area)
# else:
#     print("Triangle is no possible")