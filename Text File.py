# # # readtext=open("text","r")
# # #
# # # print(readtext.read())
# # #
# # # uu = open("text","r")
# # # print(uu.read())
# #
# #
# # wr=open("ami.txt","r")
# # wr.write("subscribe")
# # print(wr)
#
#
#
# #
# # new = open("thisisnewfile","r+")
# # new = write()
# # print(new.read())
#
#
# #
# # w=open("nfile1.txt","r+")
# # w.write("amar sonar ")
# # import os
# # # os.remove("nfile1.txt")
# # os.rmdir("galu")
#
#
#
# # import Modules
# # Modules.hayat()
#
# # import Modules as hayat
# # hayat.hayat()
#
# from Modules import hayat
# hayat()
#
#
# # import Modules
# #
# # Modules.thisnewmodules()
#
# # from Modules import thisnewmodules
# # thisnewmodules()
#
#
# # import Modules as thisnewmodules
# # thisnewmodules.thisnewmodules()
# #
# #
# #
# import Modules as another
# another.another()
#
#
#
# #
# # import Modules as hayati
# # hayati.hayati()
#
#
# from Modules import another
# another()
# print("Finished this programme")
import fileinput

with open("new_file.txt","r") as an_file:
    words = []
    for line in an_file.readlines():
        only_words = line.strip().split(" ")
        words +=only_words
        print(len(words))
print(len(only_words))


another_one = open("this_new_file","w")
print(another_one.read())
fileinput.close()


