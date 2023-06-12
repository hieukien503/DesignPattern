from abc import ABC, abstractmethod

class Context:
    def __init__(self, strategy):
        self.__strategy = strategy
    def strategy(self):
        return self.__strategy
    def strategy(self, strategy):
        self.__strategy = strategy
    def operation(self):
        print("Sort list using Strategy:")
        result = self.__strategy.sortList([10, 9, 49, -7, 190, -20])
        print(",".join([str(x) for x in result]))

class Strategy(ABC):
    @abstractmethod
    def sortList(lst: list):
        pass

class ConcreteStrategyA(Strategy):
    def sortList(self, lst: list):
        lst.sort()
        return lst

class ConcreteStrategyB(Strategy):
    def sortList(self, lst: list):
        lst.sort(reverse = True)
        return lst

def ClientCode(ctx: Context):
    ctx.operation()

if __name__ == '__main__':
    ctx1, ctx2 = Context(ConcreteStrategyA()), Context(ConcreteStrategyB())
    print("Sort list using strategy normal sort:")
    ClientCode(ctx1)
    print("Sort list using strategy normal sort and reverse the result:")
    ClientCode(ctx2)
