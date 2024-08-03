num = range(1, 20, 2)
print("Nums: ", list(num))

squares = [n ** 2 for n in num]
print("Squares: ", squares)

print("Multiple data: ", [[x, x ** 2, x ** 3] for x in range(1, 11)])
