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

marcacar= input("elige la marca")

modelocar= input("elige el modelo")

colorcar= input("elige  el color")

añocar= input("elige el año")





car1 = Car(marcacar,modelocar,colorcar,añocar)
print(car1.show_attr())
car2 = Car("Lamborghini","Urus","Amarillo",2017)
print(car2.show_attr())
