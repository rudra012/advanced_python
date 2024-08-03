def square(x):
    return x ** 2


print([square(x) for x in range(1, 11)])
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(list(map(lambda x: x ** 2, range(1, 11))))
# OP: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print([square(x) for x in range(1, 11) if x % 2 == 0])
# OP: [4, 16, 36, 64, 100]

print(list(map(lambda x: x ** 2, (x for x in range(1, 11) if x % 2 == 0))))
# OP: [4, 16, 36, 64, 100]

print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(1, 11)))))
# OP: [4, 16, 36, 64, 100]

print("End")
