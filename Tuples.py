# # # # Newtuples=(1,2,3,"halu","ARAMARI")
# # # # print(type(Newtuples))
# # # #
# # # #
# # # # #Negative index
# # # # print(Newtuples[-1])
# # #
# # # #RANGE
# # # # fruites = ("apple", "banana", "mango", "lichi", "pineapple","Nala")
# # # # print(fruites[2:6])
# # #
# # # #update tuples
# # #
# # # fruites = ("apple", "banana", "mango", "lichi", "pineapple","Nala")
# # #
# # # b=list(fruites)
# # #
# # # b.append("doi")
# # # print(b)
# # #
# # # fruites=tuple(b)
# # # print(fruites)
# #
# #
# #
# #
# #
# #
# # '''tryana one more'''
# #
# # fruites = ("apple", "banana", "mango", "lichi")
# #
# # # nv=list(fruites)
# # # # nv.append("hollicros")
# # # #
# # # #
# # # # print(nv)
# # # # fruites=tuple(nv)
# # # # print(fruites)
# # #
# # # nv.insert(2,"aam")
# # # print(nv)
# # #
# # # # fruites=tuple(nv)
# # # # print(fruites)
# # #
# # # ty=list(fruites)
# # # ty[3]="aaaaam"
# # #
# # # fruites=tuple(ty)
# # # print(fruites)
# #
# #
# #
# # ##unpack Tuples
# # fruites = ("apple", "banana", "mango", "lichi")
# #
# # (a,*b,c)=fruites
# # print(a)
#
#
#
#
#
#
# ####revise that all
#
# # fruites = ("apple", "banana", "mango", "lichi", "pineapple", "Nala")
# # print(fruites)
#
# #
# # tes=list(fruites)
# # tes[4]="anaros"
# # # print(tes)
# #
# # fruites=tuple(tes)
# #
# # print(fruites)
#
# fruites = ("apple", "banana", "mango", "lichi", "pineapple", "Nala")
# print(fruites)
# # trt=list(fruites)
# # trt[4]="boro anaros"
# # print(trt)
# #
# # fruites=tuple(trt)
# # print(fruites)
#
# #
# # ty=list(fruites)
# # ty.insert(2,"aaaaaam")
# # fruites=tuple(ty)
# # print(fruites)
#
#
# ##Unpack the tuple
# # flist=('apple', 'banana', 'aaaaaam', 'mango', 'lichi', 'pineapple', 'Nala')
# # # a,b,c,d,e,f,g =flist
# # # print(b)
# # # print(g)
# #
# # a,b,c,*d=flist
# # print(b)
# #
# #
# # #tuple loop
# #
# # for t in flist:
# #     print(t)
# #
# #
# #
# #
# #     for g in range(len(flist)):
# #         print(flist[g])
# #
#
# #
# # flist = ('apple', 'banana', 'aaaaaam', 'mango', 'lichi', 'pineapple', 'Nala')
# #
# # hi=2
# # while hi< len(flist):
# #     print(flist[hi])
# #     hi=hi+2
#
#
# #join tuple
#
# # t1=(1,2,3,4,5,6)
# # t2=(7,8,9,10,11)
# #
# # t3=t1+t2
# # print(t3)
#
# #multyply
# t1 = (1, 2, 3, 4, 5, 6)
# print(t1*5)
#
#
# ##tuple method
#
# list=('apple', 'banana', 'aaaaam', 'mango')
#
# li=list.index("apple")
# print(li)
#
#
#
#
# ##exersice#
# #1
# # fruits=("apple","banana","cherry")
# # print(fruits[0])
#
# # #2
# # print=range(fruits)
# #
# # hii=len(fruits)
# # print(hii)
#
# fruits=("apple","banana","cherry")
# for yu in range(len(fruits)):
#     print(yu)
#
#                                            ###thats was learn from previous tutorial
# ty=2
# while ty<len(fruits):
#     print(fruits)




ic=(1,2,3,4,5,3,6,3)
print(ic.count(3))

