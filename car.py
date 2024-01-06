#Blueprint
class Car(object):
    #properties
    def _init_(self,brand,color,price,year,condition):
        self.brand=brand
        self.color=color
        self.price=price
        self.year=year
        self.condition=condition

        #functions
    def display_details(self):
        print("Brand : ", self.brand)
        print("color :" ,self.color)
        print("price : " ,self.price)
        print("year :", self.year)
        print("condition :", self.condition)

    def greet(self):
        self.brand = input("What is the brand of your car?" )
        print("The brand is: ", self.brand)

    def getDetails(self):
        self.color=input ("What color is your car?")
        print("The color of the car is:", self.color)

    def cost(self):
        self.price=input("What was the price of your car?")
        print("The price of the car is:", self.price)

#Create Objects
c1=Car("toyota", "gray", 20000, 2015, "used")
#objectname.functionname()
c1.greet()
c1.display_details()
c1.getDetails()
c1.cost()

c2=Car("honda", "red", 15000, 2003, "used")
#objectname.functionname()
c2.greet()
c2.display_details()
c2.getDetails()
c2.cost()

c3=Car("Tesla", "black", 30000, 2019, "new")
#objectname.functionname()
c3.greet()
c3.display_details()
c3.getDetails()
c3.cost()