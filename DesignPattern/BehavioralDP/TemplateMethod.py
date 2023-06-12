from abc import ABC, abstractmethod
class BaseClass(ABC):
    def template_method(self):
        self.op1()
        self.override_op1()
        self.op2()
        self.hook1()
        self.override_op2()
        self.op3()
        self.hook2()
    def op1(self):
        print("op1 from Base Class")
    def op2(self):
        print("op2 from Base Class")
    def op3(self):
        print("op3 from Base Class")
    @abstractmethod
    def override_op1(self):
        pass
    @abstractmethod
    def override_op2(self):
        pass
    
    def hook1(self):
        pass
    def hook2(self):
        pass

class A(BaseClass):
    def override_op1(self):
        print("op1 from class A")
    def override_op2(self):
        print("op2 from class A")

class B(BaseClass):
    def override_op1(self):
        print("op1 from class B")
    def override_op2(self):
        print("op2 from class B")
    def hook1(self):
        print("hook1 from class B")
    def hook2(self):
        print("hook2 from class B")

def ClientCode(abs_class: BaseClass):
    abs_class.template_method()

if __name__ == '__main__':
    a, b = A(), B()
    print("Template Method from A:")
    ClientCode(a)
    print("Template Method from B:")
    ClientCode(b)
