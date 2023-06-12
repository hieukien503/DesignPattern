from abc import ABC, abstractmethod # for Abstract Base Class and abstractmethod

# Builder base class
class HouseBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass
    @abstractmethod
    def buildWalls(self):
        pass
    @abstractmethod
    def buildDoors(self):
        pass
    @abstractmethod
    def buildWindows(self):
        pass
    @abstractmethod
    def buildRoof(self):
        pass
    @abstractmethod
    def buildGarage(self):
        pass
    @abstractmethod
    def getResult(self):
        pass

# Derived Class and override method
class RegularBuilder(HouseBuilder):
    def reset(self):
        print("Reset to Regular Builder")
    def buildWalls(self):
        print("Regular Builder: Build Walls")
    def buildDoors(self):
        print("Regular Builder: Build Doors")
    def buildWindows(self):
        print("Regular Builder: Build Windows")
    def buildRoof(self):
        print("Regular Builder: Build Roof")
    def buildGarage(self):
        print("Regular Builder: Build Garage")
    def getResult(self):
        print("Finish Regular House")

class PalaceBuilder(HouseBuilder):
    def reset(self):
        print("Reset to Palace Builder")
    def buildWalls(self):
        print("Palace Builder: Build Walls")
    def buildDoors(self):
        print("Palace Builder: Build Doors")
    def buildWindows(self):
        print("Palace Builder: Build Windows")
    def buildRoof(self):
        print("Palace Builder: Build Roof")
    def buildGarage(self):
        print("Palace Builder: Build Garage")
    def getResult(self):
        print("Finish Palace")

class CastleBuilder(HouseBuilder):
    def reset(self):
        print("Reset to Castle Builder")
    def buildWalls(self):
        print("Castle Builder: Build Walls")
    def buildDoors(self):
        print("Castle Builder: Build Doors")
    def buildWindows(self):
        print("Castle Builder: Build Windows")
    def buildRoof(self):
        print("Castle Builder: Build Roof")
    def buildGarage(self):
        print("Castle Builder: Build Garage")
    def getResult(self):
        print("Finish Castle")

# Director Class, not neccesary since builder can be customized
class Director:
    def __init__(self, builder: HouseBuilder | None = None): # Constructor
        self.__builder = builder # double underscore __builder means private attribute 'builder' in Python
    def setBuilder(self, builder: HouseBuilder):
        self.__builder = builder
    def doTask(self):
        self.__builder.reset()
        self.__builder.buildWalls()
        self.__builder.buildWindows()
        self.__builder.buildDoors()
        self.__builder.buildRoof()
        self.__builder.buildGarage()
        self.__builder.getResult()

def ClientCode(director: Director):
    print("Using Director:")
    regularHouse = RegularBuilder()
    director.setBuilder(regularHouse)
    director.doTask()

    print("Custom (Not using Director):")
    regularHouse.buildWalls()
    regularHouse.buildWindows()
    regularHouse.buildRoof()
    regularHouse.buildDoors()
    regularHouse.buildGarage()
    regularHouse.getResult()

def main():
    director = Director()
    ClientCode(director)

if __name__ == '__main__':
    main()

