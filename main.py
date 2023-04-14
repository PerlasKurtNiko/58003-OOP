class Circ:
    def __init__(self, radius = 0):
        self.__radius = radius
       # self.__diameter = None
class Rad (Circ):
    def Area(self):
        return 3.14*(self.__radius ** 2)
    def Circumference_r(self):
        return 2*3.14*self.__radius
class Dia(Circ):
    def ArD (self):
        return 3.14*((self.__diameter/2)**2)
    def CircD (self):
        return 3.14*self.__diameter


r = float(input("Please input radius(if none input the number 0): "))
ArR = Rad(r)
print(str(Rad.Area()))
CircuR = Rad (r)
print(str(Rad.Circumference_r()))
