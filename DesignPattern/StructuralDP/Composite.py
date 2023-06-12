from abc import ABC, abstractmethod
from typing import List

class Box(ABC):
    @property
    def parent(self):
        return self._parent
    @parent.setter
    def parent(self, parent):
        self._parent = parent
    
    def add(self, box):
        pass

    def remove(self, box):
        pass

    def is_composite(self):
        return False
    
    @abstractmethod
    def operation(self) -> int:
        pass

class Products(Box):
    def operation(self) -> int:
        return 1

class Composite(Box):
    def __init__(self) -> None:
        self.__children: List[Box] = []
    def add(self, box: Box):
        self.__children.append(box)
        box.parent = self
    def remove(self, box: Box):
        self.__children.remove(box)
        box.parent = None
    def is_composite(self):
        return True
    def operation(self) -> int:
        result = 0
        for box in self.__children:
            result += box.operation()
        return result

def ClientCode(box: Box):
    print(f"Total price: {str(box.operation())}")

def ClientCode2(box1: Box, box2: Box):
    if box1.is_composite():
        box1.add(box2)
    print(f"Total price: {str(box1.operation())}")

def main():
    simple = Products()
    print("Simple Products:")
    ClientCode(simple)

    tree = Composite()

    branch1 = Composite()
    branch1.add(Products())
    branch1.add(Products())

    branch2 = Composite()
    branch2.add(Products())
    
    tree.add(branch1)
    tree.add(branch2)

    print("Using ClientCode:")
    ClientCode(tree)

    print("Using ClientCode2:")
    ClientCode2(tree, simple)

if __name__ == '__main__':
    main()