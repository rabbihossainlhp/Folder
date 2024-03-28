class new_items:
    def __init__(self,Name,Brand,year,Model):
        self.Name=Name
        self.Brand=Brand
        self.year=year
        self.Model=Model

class Proxyit(new_items):
    pass

vari=Proxyit("Toyota","ninjaCHR",2014,"shlk222kfh")
print(vari.Name,vari.Model,vari.year,vari.Brand)




