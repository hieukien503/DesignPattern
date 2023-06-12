class Target:
    def request(self) -> str:
        return "XML Format"

# This Adaptee represent the useful behavior but its inteface is incompatible with the existing code
# In this example, the interface supports JSON Format
class Adaptee:
    def special_request(self) -> str:
        return "JSON Format"

# Makes Adaptee compatible with the existing code
class Adapter(Target):
    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee
    def request(self):
        return f"Adapter: (Translated) {self.adaptee.special_request().replace('JSON', 'XML')}"

def ClientCode(target: Target):
    print(target.request())

def main():
    print("Default client:")
    client = Target()
    ClientCode(client)
    print("Incompatible interface from Adaptee:")
    adaptee = Adaptee()
    print(f"Adaptee request: {adaptee.special_request()}")
    print("Use Adapter to solve problem:")
    adapter = Adapter(adaptee)
    ClientCode(adapter)

if __name__ == '__main__':
    main()