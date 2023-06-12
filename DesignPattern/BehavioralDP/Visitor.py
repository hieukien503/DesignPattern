from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visitA(self, a):
        pass
    @abstractmethod
    def visitB(self, b):
        pass

class Component(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

class A(Component):
    def accept(self, visitor: Visitor):
        return visitor.visitA(self)
    def __str__(self) -> str:
        return self.__class__.__name__

class B(Component):
    def accept(self, visitor: Visitor):
        return visitor.visitB(self)
    def __str__(self) -> str:
        return self.__class__.__name__

class ClientVisitor(Visitor):
    def visitA(self, a):
        return f"Visit component {str(a)}"
    def visitB(self, b):
        return f"Visit component {str(b)}"

if __name__ == '__main__':
    visitor = ClientVisitor()
    component = [A(), B(), A(), A(), B()]
    for x in component:
        print(x.accept(visitor))
    
