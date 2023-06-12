class Subsystem1:
    def ready(self) -> str:
        return "{} ready!".format(self.__class__.__name__)
    def go(self) -> str:
        return "{}: Go!".format(self.__class__.__name__)

class Subsystem2:
    def ready(self) -> str:
        return "{} ready!".format(self.__class__.__name__)
    def fire(self) -> str:
        return "{}: Fire!".format(self.__class__.__name__)

class Facade:
    def __init__(self, sub1: Subsystem1, sub2: Subsystem2) -> None:
        self.sub1 = sub1 or Subsystem1()
        self.sub2 = sub2 or Subsystem2()
    def operation(self) -> str:
        result = []
        result.append("Facade initializes subsystems:")
        result.append(self.sub1.ready())
        result.append(self.sub2.ready())
        result.append("Facade order subsystems to perform the action:")
        result.append(self.sub1.go())
        result.append(self.sub2.fire())
        return "\n".join(result)

def ClientCode(facade: Facade):
    print(facade.operation())

if __name__ == '__main__':
    facade = Facade(Subsystem1(), Subsystem2())
    ClientCode(facade)
