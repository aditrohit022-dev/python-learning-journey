# basics of object : create a class named Car in which add attributs like brand and model of car

class Car:
    def __init__ (self,brand,model):
        self.brand=brand
        self.model=model 

my_car= Car("maruti suzuki","swift")  
print(my_car.brand)
print(my_car.model) 
print(" ")
my_car2= Car("toyota","supra M37") 
print(my_car2.brand)
print(my_car2.model)

#class method and self: add a method to the class Car that dislpy full name of a car with brand and model 

class Car:
    def __init__ (self,brand,model):
        self.brand=brand
        self.model=model 
    def full_name(self):
        return f"{self.brand} {self.model}"
my_car=Car("toyota","supra")
print(my_car.full_name())
print("")
print(my_car.brand)
print(my_car.model)

# inheritance: createa class Elactriccar that inherits Car class and add a attribute--"bettry_size"

class Car:
    def __init__ (self,brand,model):
        self.brand=brand
        self.model=model 
    def full_name(self):
        return f"{self.brand} {self.model}"
class Electriccar(Car):
    def __init__(self,brand,model,bettry_size):
        super().__init__(brand,model) 
        self.bettry_size=bettry_size 
my_ele_car=Electriccar("tesla","tesla s ","85kWh") 
print(my_ele_car.full_name()),print("battry size"),print(.bettry_size())

#encapuslation: modify the car class to encapuslate the brand attribute,making it private, and provide a getter method
          
class Car:      
    def __init__ (self,brand,model):
        self.__brand=brand
        self.model=model 
    def full_name(self):
        return f"{self.__brand} {self.model}" 
    def get_brand(self):
        return __brand+" !"

class Electriccar(Car):
    def __init__(self,brand,model,bettry_size):
        super().__init__(brand,model) 
        self.bettry_size=bettry_size 
my_ele_car=Electriccar("tesla","tesla s ","85kWh") 
print(my_ele_car.full_name())
print(my_ele_car.get_brand())

#polymorphism: define a method fule_type in both car and electric car classes with diff behaviors


class Car: 
    def __init__ (self,brand,model):
        self.__brand=brand
        self.model=model 
    def full_name(self):
        return f"{self.__brand} {self.model}" 
    def get_brand(self):
        return __brand+" !"
    def fule_type(self): 
        return "petrol or diesel"


class Electriccar(Car):
    def __init__(self,brand,model,bettry_size):
        super().__init__(brand,model) 
        self.bettry_size=bettry_size 
    def fule_type(self):
        return "electric charge"
my_ele_car=Electriccar("tesla","tesla s ","85kWh") 
print(my_ele_car.full_name())
print(my_ele_car.get_brand())
print(my_ele_car.fule_type())
my_car=Car("tata","safari") 
print(my_car.full_name())
print(my_car.fule_type())


# class veriable: add a veriable in Car that keeps trake of  number of car created
class Car: 
    total_car=0

    def __init__ (self,brand,model):
        self.__brand=brand
        self.model=model 
        Car.total_car+=1
    def full_name(self):
        return f"{self.__brand} {self.model}"
    def get_brand(self):
        return self.__brand+" !"
    def fuel_type(self):
        return "petrol or diesel"
        
        
        
class Electriccar(Car):
    def __init__(self,brand,model,bettry_size):
        super().__init__(brand,model) 
        self.bettry_size=bettry_size 
    def fuel_type(self):
        return "electric charge " 
my_ele_car=Electriccar("tesla","tesla s ","85kWh") 
my_car=Car("tata","safari")
print(Car.total_car)

# static method: add a static to the Car class that returns genroual disription of that car 
class Car: 
    total_car=0

    def __init__ (self,brand,model):
        self.__brand=brand
        self.model=model 
        Car.total_car+=1
    def full_name(self):
        return f"{self.__brand} {self.model}"
    def get_brand(self):
        return self.__brand+" !"
    def fuel_type(self):
        return "petrol or diesel" 
    @staticmethod
    def genroual_discrription():
        return " cars are mean of transport"
        
        
        
class Electriccar(Car):
    def __init__(self,brand,model,bettry_size):
        super().__init__(brand,model) 
        self.bettry_size=bettry_size 
    def fuel_type(self):
        return "electric charge " 
my_el_car=Electriccar("tesla","tesla s ","85kWh") 
my_car=Car("tata","safari")

print(Car.genroual_discrription())

# property decoretors: use a prperty decoretr in the car class to make the model attribute read only


class Car: 
    total_car=0

    def __init__ (self,brand,model):
        self.__brand=brand
        self.__model=model 
        Car.total_car+=1
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    def get_brand(self):
        return self.__brand+" !"
    def fuel_type(self):
        return "petrol or diesel" 
    @staticmethod
    def genroual_discrription():
        return " cars are mean of transport"
    @property 
    def model(self):
        return self.__model
        
        
class Electriccar(Car):
    def __init__(self,brand,model,bettry_size):
        super().__init__(brand,model) 
        self.bettry_size=bettry_size 
    def fuel_type(self):
        return "electric charge " 
my_el_car=Electriccar("tesla","tesla s ","85kWh") 
my_car=Car("tata","safari")
#my_car.model="city"
print(my_car.model)










