list1 = range(1, 10)
list2 = range(3, 15, 2)
print("List1: ", list(list1))
print("List2: ", list(list2))

intersection = []

for x in list1:
    for y in list2:
        if x == y:
            intersection.append(x)
print("Intersection1: ", intersection)

intersection = [x for x in list1 for y in list2 if x == y]
print("Intersection2: ", intersection)

non_commom_nums = [(x, y) for x in list1 for y in list2 if x != y]
print("Non Commom Nums: ", non_commom_nums)
