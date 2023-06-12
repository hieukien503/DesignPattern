from typing import Any


class SingletonMeta(type):
    __instances = {} # Create an empty dictionary
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls.__instances:
            instance = super().__call__(*args, *kwds)
            cls.__instances[cls] = instance
        return cls.__instances[cls]

class Singleton(metaclass = SingletonMeta):
    pass

def main():
    s1, s2 = Singleton(), Singleton()
    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, both variables contain the different instance.")

if __name__ == '__main__':
    main()