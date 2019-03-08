__author__ = 'aganiger'


class Circle():

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14

circle= Circle(8)

print(circle.area())

class Rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        return self.length*self.breadth


rectangle=Rectangle(10,3)
print(rectangle.area())

import re
class CustomizeString():
    def getString(self):
        string=input("Enter the string: ")
        self.string=string

    def printString(self):
        print(self.string.upper())

    def reversString(self):
        print(self.string[::-1])

customizeString=CustomizeString()
customizeString.getString()
customizeString.printString()
customizeString.reversString()