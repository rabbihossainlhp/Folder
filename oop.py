'''class nmethod:
    def mym(self):
        print("hello")

    @classmethod
    def classmethod(cls):
        print("newmethod")
class hayat:
        @staticmethod
        def staticmethod():
            print("this is new method")

vr=hayat
vr.staticmethod()





##poiymorphism

class vehicles:
    def __init__(self,model,brand,component):
        self.model=model
        self.brand=brand
        self.component=component

class plane(vehicles):
    pass
class car(vehicles):
    pass

vri=plane("newmd344","hayat","all")
print(vri.model,vri.component,vri.brand)

cr=car("bm2","fj34","anoother")
print(cr.component)'''




###tryanna as new oop

class try_new_class:
    def mycs(self):
        print("new_mycs")

    @classmethod
    def classmethod(cls):
        print("another method")

    @staticmethod
    def statisticmethod():
        print("another new method")
# gy=staticmethod
# gy.statisticmethod()




'''another new class'''


class ar_class:
    def __init__(self,model,year,component):
        self.model=model
        self.year=year
        self.component=component

# class new_plane(ar_class):
#     pass
# variable=new_plane("BD airlines",2023,"there is too much another component")
# print(variable.model,variable.year,variable.component)
class ghari(ar_class):
    pass
var=ghari("tata",2022,"not too much but has some component")
print(var.model,var.year,var.component)