'''Iterator'''
new_List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
load = iter(new_List)
# print(next(load))
# print(next(load))
# print(next(load))
# print(next(load))
# print(next(load))

for i in load:
    print(i)

'''Genarator'''


def For_genr():
    yield 1
    yield 2
    yield 3
    yield 4


#
f = For_genr()

# print(next(f))
# print(next(f))
# print(next(f))

##usee for loop

for i in f:
    print(i)

    ##Solving the fibonacci series problem using this genarator::::


def cal_fibio(limt):
    a = 0
    b = 1
    while a < limt:
        yield a
        a = b
        b = a + b

v = cal_fibio(10)

for i in v:
    print(i)

#
# print(next(v))
# print(next(v))
# print(next(v))
# print(next(v))
# print(next(v))
#Now it will be exicute by using simple for loop

'''Decorator'''

def Dis():
    print('Helloworld')

Dis()

def modify(fn):
    def inn():
        print('You have to write this sents')
        fn()
    return inn()

de_fnc = modify(Dis)
