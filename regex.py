# import re
# text= "aamar sonar bangla a ami "
# v = re.findall(["a_m"],text)
# print(v)


###

text= "aamar sonar bangla a ami "
if text:
    print("this is really right")
else:
    print("its not right")



while True:
    try:
        mn1= int(input("Please Enter Your Expected Multiplication Number:"))
        for p in range(1,11):
            e_mno = mn1*p
            print(f"{mn1}*{p} = {e_mno}")
    except KeyboardInterrupt:
        print("\n Programe Stoped")
    except ValueError:
        print("Invisible Input::Please Enter a Input")



while True:
    try:
      nu1 = int(input("Enter Your number"))
      for ccjy in range(1,11):
           new = nu1*ccjy
           print(f"{nu1}*{ccjy} = {new}")
    except KeyboardInterrupt:
        print("\n Programe Stoped")
    except ValueError:
        print("Invisible : Please Input Another")
