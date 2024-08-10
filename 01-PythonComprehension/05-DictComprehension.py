data = {"a": 1, "b": 2, "c": 3, "d": 4}
print(data)

# Make sure Dict keys should be immutable else you will get  unhashable type error
print({x * 2: y ** 2 for x, y in data.items()})
print({x * 2: y ** 2 for x, y in data.items()})
print({(x, x * 2, y): y ** 2 for x, y in data.items()})
