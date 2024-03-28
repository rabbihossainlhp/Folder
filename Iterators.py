list = [1,2,3,4,"kar name"]
#for j in list:
 #   print(j)



#= iter(list)

#print(next(t))


lis=iter(list)
#print(lis.__next__())
#print(lis.__next__())

print(next(lis))

##new list for iterators

nlist=[1,2,3,4,5,"amar","sonar","bangla","ami ","bhalobasi"]

# for ii in nlist:
#     print(ii)


#try to another way
#
# ff= iter(nlist)
# print(ff)

n=iter(nlist)

print(n.__next__())
print(n.__next__())
print(n.__next__())










##try one more time with newllist

nnist=["aam","jaam","kathal","kola","lichu","peyara","bedana","dalim","apple"]
#
# for new in nnist:
#     print(len(new))


nt=iter(nnist)
print(next(nt))
print(next(nt))


# print(nt.__next__())
# print(nt.__next__())
# print(nt.__next__())




flist=[1,2,3,4,5,6]
ff=iter(flist)
# print(ff.__next__())
# print(ff.__next__())

print(next(ff))
print(next(ff))
print(next(ff))








nnlist=[1,2,3,47,8]
j=iter(nnlist)
print(j.__next__())

print(next(j))



new_list = [111,222,333,444,777,888,999,000]
nn = iter(new_list)
print(nn)
print(nn.__next__())
print(nn.__next__())
print(next(nn))