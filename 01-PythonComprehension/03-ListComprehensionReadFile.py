fp = open("file.txt")

op = [x for x in fp if "Shailesh" in x]

print(op)
