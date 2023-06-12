from abc import ABC, abstractmethod

class Color (ABC):
    pass

class Red(Color):
    pass

class Blue(Color):
    pass

class Shape (ABC):
    def __init__(self, color: Color):
        self.color = color

    def operation(self) -> str:
        return "{} has color {}".format(self.__class__.__name__, self.color.__class__.__name__)

class Square(Shape):
    pass

class Circle(Shape):
    pass

def ClientCode(shape: Shape):
    print(shape.operation())

def main():
    red = Blue()
    circle = Circle(red)
    ClientCode(circle)

if __name__ == '__main__':
    main()
    