def myAdd(a, b, c, e):
    print(a + b - c * e)

myAdd(5, 6, 123, 2)
myAdd(10, 20, 123, 1)

# ==================================================

bigList = [123, 1231, 12, 3123, 2111, 12, 2, 2, 2, 5124, 1241, 122, 2424, 2, 2, 2,123, 1231, 12, 3123, 2111, 12, 2, 2, 2, 5124, 1241, 122, 2424, 2, 2, 2,123, 1231, 12, 3123, 2111, 12, 2, 2, 2, 5124, 1241, 122, 2424, 2, 2, 2,123, 1231, 12, 3123, 2111, 12, 2, 2, 2, 5124, 1241, 122, 2424, 2, 2, 2]
smallList = [12, 2, 2, 3, 4, 5]


def findTwo(lis):
    # Количество двоек
    twoRes = 0

    for i in lis:
        if i == 2:
            twoRes += 1

    print(twoRes)


findTwo(smallList)
findTwo(bigList)
