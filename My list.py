# ####access my list
# Amlu=["channel name","website","group","page","AFHAAHF"]
# print(Amlu[1])
#
# Amlu[4]="linked in page"
#
# print(Amlu[4])
# print(Amlu)
#
# #append and insert using to add new items in list
# Amlu.append("this is my new name")
# print(Amlu)
#
# Amlu.insert(0,"google plus")
#
# print(Amlu)
#
#
#
# #actually now am tryanna one more time
# solavp=["osokhina","gechos kina","vuila amare"]
# print(solavp)
#
# solavp[2]="notun ta hbe ekdin"
# print(solavp)
#
# solavp.append("ki ar jogii ba kobo ami")
# print(solavp)
#
# #another addition by the insert
#
# solavp.insert(2,"bhabtechi j ki ar add korbo")
# print(solavp)


#remove from list by the using remove() method


fornew=["anonymuse","mayabolo","sahil","dutturi","sokhina","achos kina",465]
# fornew.remove(465)
# print(fornew)

#anothr way with pop

# fornew.pop(1)
# print(fornew)

#remove frome list by the using del specified

del fornew[2]

print(fornew)


#clear the list

fornew.clear()
print(fornew)


'''now tryanna to short list'''
utu=[23,33,32,3,42,6,6,7,8,5,3,9]

utu.sort()
print(utu)


eng=["h","s","g","s"]
eng.sort()
print(eng)

'''reverse'''
mun=[1,2,3,5,6,7,]

mun.sort(reverse=True)
print(mun)



'''copy list'''

number=[1,3,4,6,7,8,9,0]

byg=number.copy()
print(byg)
print(number)


mun.copy()
print(mun)




# llsit comprehenshion

# jangal=["ameaa","jhimuya","sela soud","tripplle hteraphy. del"]

otun=[1,3,34,33,65,65,23]
# for gh in otun:
#     print(gh**2)


# hhy=[ccg*3 for ccg in otun]
# print(hhy)

ttu=[bblR%2 for bblR in otun]
print(ttu)








##tryanna another

number=[1,3,4,6,7,8,9,0]
print(number)
cghy=number.copy()
print(cghy)





#taryanna onemore time

#
filist=[2,4,5,6,7,8,45,3,23,54,2,13,1]
filist.sort()
print(filist)

solist=[1, 2, 2, 3, 4, 5, 6, 7, 8, 13, 23, 45, 54]
solist.sort(reverse=True)
print(solist)



finelist=["Arab Amirat","Middle State","Canada","Hongkong"]
gh=range(len(finelist))
print(gh)

for h in gh:
    print(h)


for y in finelist:
    print(y)

ffg=1
# while ffg<len(finelist):
#     print(finelist)


#
#
#
# ki=li2.copy()
# print(ki)
#





####python join list

li1=[1,2,3,4,5,6]
li2=[7,8,9,10]
print(li2)
li3=li1+li2
print(li3)

##another way to join this list

li1.extend(li2)
print(li1)


##onemore

nl=["Asiya Khatun"]
nl1=["Maine"]

nl.extend(nl1)
print(nl)
