from abc import ABC, abstractmethod

class Context:
    _state = None
    def __init__(self, state):
        self.transition_to(state)
    
    def transition_to(self, state):
        print("Context: Transition to {}".format(type(state).__name__))
        self._state = state
        self._state.context = self
    
    def req1(self):
        return self._state.handle1()
    def req2(self):
        return self._state.handle2()

class State(ABC):
    @property
    def context(self):
        return self._context
    @context.setter
    def context(self, context: Context):
        self._context = context
    @abstractmethod
    def handle1(self):
        pass
    @abstractmethod
    def handle2(self):
        pass

class StateA(State):
    def handle1(self):
        print("A handles req1")
        print("A wants to change state")
        self.context.transition_to(StateB())
    def handle2(self):
        print("A handles req2")

class StateB(State):
    def handle1(self):
        print("B handles req1")
    def handle2(self):
        print("B handles req2")
        print("B wants to change state")
        self.context.transition_to(StateA())

if __name__ == '__main__':
    context = Context(StateA())
    context.req1()
    context.req2()

