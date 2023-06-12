from abc import ABC, abstractmethod

# Base class for transport
class Transport(ABC):
    @abstractmethod
    def deliver(self):
        pass

# Derived class and override method
class Truck(Transport):
    def deliver(self):
        print("Deliver cargo by land")

class Ship(Transport):
    def deliver(self):
        print("Deliver cargo by sea")

# Base class for logistic app
class LogisticApp(ABC):
    @abstractmethod
    def planDelivery(self):
        pass
    @abstractmethod
    def createTransport(self):
        pass

# Derive Class and override method
class SeaLogistic(LogisticApp):
    def planDelivery(self):
        print("Ship delivery!")
    
    def createTransport(self):
        return Ship()

class RoadLogistic(LogisticApp):
    def planDelivery(self):
        print("Truck delivery!")
    
    def createTransport(self):
        return Truck()

def ClientCode(log_app: LogisticApp):
    log_app.planDelivery()
    transport = log_app.createTransport()
    transport.deliver()

def main():
    log_app = RoadLogistic()
    ClientCode(log_app)

if __name__ == '__main__':
    main()