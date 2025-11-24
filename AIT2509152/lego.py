import math

class Circle:
    def __init__(self, r):
        self.__radius = r

    def perimeter(self):
        return 2*self.__radius*math.pi
    
    def area(self):
        return self.__radius**2 * math.pi
    
    def getRadius(self):
        return self.__radius
    
a = Circle(1)
b = Circle(2)

print(a.perimeter(), a.area(), a.getRadius())
print(b.perimeter(), b.area(), b.getRadius())