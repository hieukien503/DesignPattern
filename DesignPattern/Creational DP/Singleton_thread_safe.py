from threading import Lock, Thread
from typing import Any


class SingletonMeta(type):
    __instances = {} # Create an empty dictionary
    _lock = Lock() # Thread Lock
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        with cls._lock:
            if cls not in cls.__instances:
                instance = super().__call__(*args, *kwds)
                cls.__instances[cls] = instance
        return cls.__instances[cls]

class Singleton(metaclass = SingletonMeta):
    def __init__(self, val: str | None = None):
        self.val = val

def test(val: str) -> None:
    singleton = Singleton(val)
    print(singleton.val)

def main():
    print("If two results are the same, Singleton works. Otherwise, Singleton failed")
    p1, p2 = Thread(target = test, args = ("p1",)), Thread(target = test, args = ("p2", ))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()