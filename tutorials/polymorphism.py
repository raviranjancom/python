from abc import ABC, abstractmethod
class shape:

    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (3.14*self.radius*self.radius)

class square(shape):
    def __init__(self,side):
        self.side=side
    def area(self): 
        return self.side*self.side

class triangle(shape):
    def __init__(self,height,width):
        self.height=height
        self.width=width
    def area(self):
        return self.height*self.width*(0.5)

shapes=[circle(10) , square(10), triangle(3,4)]

for i in shapes:
    print(i.area())
