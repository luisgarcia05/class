print("¿Qué tipo de vehículo desea registar?")
print("1. Carro")
print("2. Barco")
print("3. Avión")


#Class: Car
class Car:
    
    #Class Attribute

    seller = "M Car C.A."

    #Instance Attributes Init

    def __init__(self,brand,model,color,year):

        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    #Class Definition
        
    def show_attr(self):
        return "Marca: {}, Modelo: {}, Color: {}, Año: {}".format(self.brand,self.model,self.color,self.year)
    
#Class: Ship
class Ship:
    
    #Class Attribute

    seller = "M Ship C.A."

    #Instance Attributes Init

    def __init__(self,brand,model,color,year):

        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    #Class Definition
        
    def show_attr(self):
        return "Marca: {}, Modelo: {}, Color: {}, Año: {}".format(self.brand,self.model,self.color,self.year)

#Class: Airplane
class Airplane:
    
    #Class Attribute

    seller = "M Airplane C.A."

    #Instance Attributes Init

    def __init__(self,brand,model,color,year):

        self.brand = brand
        self.model = model
        self.color = color
        self.year = year

    #Class Definition
        
    def show_attr(self):
        return "Marca: {}, Modelo: {}, Color: {}, Año: {}".format(self.brand,self.model,self.color,self.year)