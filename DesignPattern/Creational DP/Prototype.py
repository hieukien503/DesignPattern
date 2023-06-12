from abc import ABC, abstractmethod # for Abstract Base Class and abstractmethod
import copy # for deepcopy, since Python does not have copy constructor

# Create a prototype
class Prototype(ABC):
    def __init__(self, name: str):
        self.name = name
        self.id = 0.0
    @abstractmethod
    def clone(self):
        pass

    def Method(self, id: float):
        self.id = id
        print("Call Method from " + self.name + " with id: " + str(self.id))

# Derived Class
class Concrete1(Prototype):
    def __init__(self, name: str, id: float):
        self.name = name
        self.id = id
    def clone(self):
        return copy.deepcopy(self)

class Concrete2(Prototype):
    def __init__(self, name: str, id: float):
        self.name = name
        self.id = id
    def clone(self):
        return copy.deepcopy(self)

class Factory:
    def __init__(self):
        self.prototypes = dict()
        self.prototypes[1] = Concrete1("prototype_1", 50.0)
        self.prototypes[2] = Concrete2("prototype_2", 60.0)
    def createPrototype(self, typ: int) -> Prototype:
        return self.prototypes[typ].clone()
    
def ClientCode(factory: Factory):
    print("Create Prototype 1:")
    prototyp = factory.createPrototype(1)
    prototyp.Method(90)

    print("Create Prototype 2:")
    prototyp = factory.createPrototype(2)
    prototyp.Method(10)

def main():
    factory = Factory()
    ClientCode(factory)

if __name__ == '__main__':
    main()



    