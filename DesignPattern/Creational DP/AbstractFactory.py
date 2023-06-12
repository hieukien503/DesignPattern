from abc import ABC, abstractmethod # import Abstract Base Class and abstractmethod

# Chair Class
class Chair (ABC):
    # Some abstract method
    @abstractmethod
    def hasLegs(self):
        pass
    @abstractmethod
    def sitOn(self):
        pass

# Create Derived Class and override method in base class
class ModernChair(Chair):
    def hasLegs(self):
        print("Modern Chair has 4 legs")
    def sitOn(self):
        return False

class VictorianChair(Chair):
    def hasLegs(self):
        print("Victorian Chair has 4 legs")
    def sitOn(self):
        return False

class ArtDecoChair(Chair):
    def hasLegs(self):
        print("ArtDeco Chair has 4 legs")
    def sitOn(self):
        return False

# Sofa Class
class Sofa (ABC):
    # May have some abstract method
    pass

# Derived Class and override method
class ModernSofa(Sofa):
    pass

class VictorianSofa(Sofa):
    pass

class ArtDecoSofa(Sofa):
    pass

# CoffeeTable Class
class CoffeeTable (ABC):
    # May have some abstract method
    pass

# Derived Class and override method
class ModernCoffeeTable(CoffeeTable):
    pass

class VictorianCoffeeTable(CoffeeTable):
    pass

class ArtDecoCoffeeTable(CoffeeTable):
    pass


# Abstract Class: FurnitureFactory
class FurnitureFactory(ABC):
    # 3 abstract method for creating abstract object
    @abstractmethod
    def createChair(self) -> Chair:
        pass
    @abstractmethod
    def createSofa(self) -> Sofa:
        pass
    @abstractmethod
    def createCoffeeTable(self) -> CoffeeTable:
        pass

# Derived Class and override method
class VictorianFurnitureFactory(FurnitureFactory):
    def createChair(self) -> Chair:
        return VictorianChair()
    def createSofa(self) -> Sofa:
        return VictorianSofa()
    def createCoffeeTable(self) -> CoffeeTable:
        return VictorianCoffeeTable()

class ModernFurnitureFactory(FurnitureFactory):
    def createChair(self) -> Chair:
        return ModernChair()
    def createSofa(self) -> Sofa:
        return ModernSofa()
    def createCoffeeTable(self) -> CoffeeTable:
        return ModernCoffeeTable()

class ArtDecoFurnitureFactory(FurnitureFactory):
    def createChair(self) -> Chair:
        return ArtDecoChair()
    def createSofa(self) -> Sofa:
        return ArtDecoSofa()
    def createCoffeeTable(self) -> CoffeeTable:
        return ArtDecoCoffeeTable()

def ClientCode (abs_factory: FurnitureFactory):
    chair = abs_factory.createChair()
    sofa = abs_factory.createSofa()
    coffee_table = abs_factory.createCoffeeTable()
    chair.hasLegs()

def main():
    print("Testing with Victorian Factory")
    vic_factory = VictorianFurnitureFactory()
    ClientCode(vic_factory)
    print("Testing with Modern Factory")
    modern_factory = ModernFurnitureFactory()
    ClientCode(modern_factory)
    print("Testing with ArtDeco Factory")
    artdeco_factory = ArtDecoFurnitureFactory()
    ClientCode(artdeco_factory)

if __name__ == '__main__':
    main()