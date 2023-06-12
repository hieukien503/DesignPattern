from abc import ABC, abstractmethod
import random

class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass
    @abstractmethod
    def detach(self, observer):
        pass
    @abstractmethod
    def notify(self):
        pass

class SubjectA(Subject):
    _state: int = None
    _observers = []
    def attach(self, observer):
        print("Attach an observer")
        self._observers.append(observer)
    def detach(self, observer):
        print("Detach an observer")
        self._observers.remove(observer)
    def notify(self):
        print("Notify observers...")
        for x in self._observers:
            x.update(self)
    def operation(self):
        print("Subject doing...")
        self._state = random.randrange(0, 10)
        print(f"Change state to {self._state}")
        self.notify()

class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject):
        pass

class ObserverA(ABC):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ObserverA: Reacted to the event")

class ObserverB(ABC):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state > 2:
            print("ObserverB: Reacted to the event")

if __name__ == "__main__":
    # The client code.

    subject = SubjectA()

    observer_a = ObserverA()
    subject.attach(observer_a)

    observer_b = ObserverB()
    subject.attach(observer_b)

    subject.operation()
    subject.operation()

    subject.detach(observer_a)

    subject.operation()