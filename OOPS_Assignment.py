# Manufacturer class and  Car class

class Manufacturer:

    def __init__(self, name , location):   #intialize #constructor #inside ur class method-magic meth, dunder meth, self--current object reference
        self.ProdName = name
        self.Name = name # string
        self.Location  = location  # string
        self.Brands = []  #list
        

    def add_brand(self, brands): #self.Brands  = brands # list
        self.Brands.append(brands)

    def get_brands(self):
        return self.Brands


class Car:
    def __init__(self, brand, model, year):
        self.Brand = brand # string
        self.Model  = model  # string
        self.Year  = year # integer
        
    def get_details(self):
        print(f'''brand = {self.Brand}, 
              model = {self.Model}, 
              year =  {self.Year}''')

if __name__ == "__main__":  
    obj1 = Manufacturer("Nexon", "Pune")
    obj2 = Manufacturer("Tata", "Mumbai")

    obj1.add_brand("Tata")
    obj1.add_brand("Maruti")
    obj2.add_brand("Hyundai")
    obj2.add_brand("Mahindra")

    car_details1 = Car("Tata", "Harrier", 2022)
    car_details2 = Car("Maruti", "Swift", 2021)
    car_details3 = Car("Hyundai", "Creta", 2019)
    car_details4 = Car("Mahindra", "Bolero", 2020)

    car_details1.get_details()
    car_details2.get_details()
    car_details3.get_details()
    car_details4.get_details()
    