class boro:
    car="toyota"
    tk=100000000
    home="43 floor"



class bso1(boro):
    smartphone="samsung"
    ac="air conditiion"


class bso2(bso1):
    laptop="llenovo"


class bso3(bso2):
    komaphone=""

t=bso3()
print(t.laptop)
print(t.ac)











##tryanna another

class inm:
    hous="4 pice"
    car="hayundi"
    ammount="only $78k"
    prty="onk jomi ach"

class inm1(inm):
    tk="32k"

class inm2(inm):
    hous="only 1 house"

class in11(inm1):
    osome=""

class in22(inm2):
    some="something"


cgc=in22()
print(cgc.ammount)













#another inheritaance

class deff:
    TK="939k"
    hous="there is  no hous"

class de(deff):
    h="this value is invallid"
ho=de
print(ho.hous,ho.TK)


'''
user=int(input())

for i in range(1,user+1):
    print(" "*(user-i) ,end=" ")
    print("*"*(2*i-1))
for i in range(user-1,0,-1):
    print(" "*(user-i) ,end=" ")                       ##this is a simple code for understanding this loop mean, pattern thats it>>>>>>>
    print("*"*(2*i-1))'''