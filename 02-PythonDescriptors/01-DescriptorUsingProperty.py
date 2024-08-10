class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print("Getting name")
        return self._name

    def set_name(self, name):
        print(f"Setting name: {self._name} to {name}")
        self._name = name

    def del_name(self):
        print(f"Deleting name: {self._name}")
        del self._name

    name = property(get_name, set_name, del_name)


p = Person("Rudra")
print(p.name)
p.name = "Shailesh"
print(p.name)
# del p.name

print("*"*10)

p1 = Person("Rakesh")
print(p1.name)
p1.name = "Sharma"
print(p1.name)
print(p.name)
