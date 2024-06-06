list_1 = [1, 2, 2, 2, 3, 4, 5]

result = 0
for index, value in enumerate(list_1):
    print(index, value)

list_2 = [(1, 2, 3), (1, 2, 3, 5, 6), (1, 2, 3, 2, 2), (1, 2, 3, 222), (1, 2, 3)]

for x, y, *extra in list_2:
    print(x, y,  extra)
