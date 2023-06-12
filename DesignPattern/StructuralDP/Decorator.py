from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def doPizza(self) -> str:
        pass


class TomatoPizza(Pizza):
    def doPizza(self) -> str:
        return "Tomato Pizza"

class ChickenPizza(Pizza):
    def doPizza(self) -> str:
        return "Chicken Pizza"

class PizzaDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza
    
    def doPizza(self) -> str:
        pass

class PepperDecorator(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
    
    def addPepper(self) -> str:
        return ' + Pepper'
    
    def doPizza(self) -> str:
        typ: str = self.pizza.doPizza()
        return typ + self.addPepper()

class CheeseDecorator(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
    
    def addCheese(self) -> str:
        return ' + Cheese'
    
    def doPizza(self) -> str:
        typ: str = self.pizza.doPizza()
        return typ + self.addCheese()

def ClientCode():
    tomato, chicken = TomatoPizza(), ChickenPizza()
    print(tomato.doPizza())
    print(chicken.doPizza())

    pep_decor = PepperDecorator(tomato)
    print(pep_decor.doPizza())

    cheese_decor = CheeseDecorator(tomato)
    print(cheese_decor.doPizza())

    cheese_decor2 = CheeseDecorator(pep_decor)
    print(cheese_decor2.doPizza())

if __name__ == '__main__':
    ClientCode()
    