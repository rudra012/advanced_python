class Person:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self):
        print("Getting the Name")
        return self._name

    @name.setter
    def name(self, value):
        print(f"Setting the name to {value}")
        self._name = value

    @name.deleter
    def name(self):
        print("Deleting the name")
        del self._name


x = Person("Shailesh")
print(x.name)
x.name = "Rudra"
del x.name
