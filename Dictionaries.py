# Studentinfo={
#     "Hayat":{
#         "Name":"Hayat",
#         "location":"Magura",
#         "Study":"Magura Polytechnic Institute",
#         "Subject":"A nameless Depertment",
#         "Class Roll":85123025,
# "Number":25
#     },
#   "haya": {
#       "location":"Magura",
#         "Study":"Magura Polytechnic Instjjitute",
#         "Subject":"A nameless Depertment",
#         "Class Roll":851230898625,
# "Number":25}
# }
#
# print(Studentinfo["haya"]["location"])
#
#
#
#
#
# ###now tryanna one more this dictionaries
#
# # Friendss={
# #     "Asiya Khatun":{
# #         "Name":"Mst Asiya Khatun",
# #         "Location":"Sreepur Magura",
# #         "Study":"Alim__ Similar at Intermedeate",
# #         "Studet Type":"Brilliant with Attitude"
# #     },"Ghum Pagli":{
# #         "Name":"Din't Know",
# #         "Study":"Simmiler like Asiya Khatun"
# #     },"Anothr Public":{
# #         "Name":"Here Another many name",
# #         "others":"others is only others"
# #     }, "year":1975
# # }
# #
#
# #now
# # print(Friendss)
# #
# # print(Friendss["Ghum Pagli"])
# #
# # print(Friendss["Ghum Pagli"]["Study"])
# #
# # print(Friendss["year"])
#
#
# # fh=Friendss.get("Ghum Pagli")
# #
# # print(fh)
# #
# #
# # print(Friendss.keys())
#
#
#
# # print(Friendss.values())
#
#
# ###change the item of dictionaries
#
# Friendss={
#     "Asiya Khatun":{
#         "Name":"Mst Asiya Khatun",
#         "Location":"Sreepur Magura",
#         "Study":"Alim__ Similar at Intermedeate",
#         "Studet Type":"Brilliant with Attitude"
#     },"Ghum Pagli":{
#         "Name":"Din't Know",
#         "Study":"Simmiler like Asiya Khatun"
#     },"Anothr Public":{
#         "Name":"Here Another many name",
#         "others":"others is only others"
#     }, "year":1975
# }
#
# Friendss["year"]=2006
# print(Friendss["year"])
#
#
#
# Friendss.update({"Ghum Pagli":"She is a sub brillliant student"})
#
# print(Friendss["Ghum Pagli"])
#
#
# #remove items
# #pop
# #
# # Friendss.pop("Asiya Khatun")
# # print(Friendss)
# #
# # #pop item
# #
# # Friendss.popitem()
# # Friendss.popitem()
# # print(Friendss)
#
# # del Friendss
# # print(Friendss)
#
#
# # Friendss.clear()
# # print(Friendss)
#
#
#
# ###make loop in here
# for hh in Friendss:
#     print(hh)
#
# for a in Friendss.values():
#     print(a)
#
#
#
# #
# # fornew={
# #     "num1":27,
# #     "num2":56,
# #     "num3":678
# # }
# # for r in fornew.values():
# #     print(r)
# #
# #
# #     ##another
# #
# # for ff in fornew.keys():
# #     print(ff)
# #
# #
# # for hhy in fornew.items():
# #     print(hhy)
# #
#
#
#
#
# ####copy dictionaries
#
# fornew={
#     "num1":27,
#     "num2":56,
#     "num3":678
# }
#
# ad=fornew.copy()
# print(ad)
#
#
#
# #aw
#
#
#
# print(dict(fornew))









###trpyanna this all code one more time for revishion


Newdictionarie={
    "Author":{"He is an enteprenior , and also CEO at The daily Theater"},
    "store":{
        "Name":"New dokan chal dal",
        "Employ":"There is some employ although they are not many in number but they are not inactive person",
        "Opening time":"This store are opening saturday to thursday",
        "Salary":"Every employ's salary are a standerd salary than others salary"
    },"House":{
        "Location":"House location is opposit side of MK feature ",
        "Type":"This is a adjust house"
    }
}



'''now'''

#
# print(Newdictionarie)
# for uu in Newdictionarie.keys():
#     print(uu)
# #
# Newdictionarie.update({"store""Name":{"Actually he is a big person that also all about him"}})
# print(Newdictionarie["store"])
#
# Newdictionarie["stor"]="pader dokan"
# print(Newdictionarie["store"],["Name"])


#remove
#
# Newdictionarie.pop("store")
# print(Newdictionarie)

# #
# Newdictionarie.popitem()
# Newdictionarie.popitem()
# Newdictionarie.popitem()
# print(Newdictionarie)

#
#
# for iii in Newdictionarie.items():
#     print(iii)



hjh=Newdictionarie.get("store")
print(hjh)








####now time to given solve that means Exeersice all from w3schools
##1
car={
    "brand":"ford",
    "model":"mustang",
    "year":"1964"
}
'''print(car.get("model"))
#'''
'''#2
car["year"]=2020
print(car["year"])

##3

car.update({"color":"red"})
print(car)

##3'''

car.pop("model")
print(car)

# ##4
# car.clear()
# print(car)



#~~~
#
# jjj=0#####
# while jjj<len(car):
#     print(car[0])

for t in car:
    print(t)


