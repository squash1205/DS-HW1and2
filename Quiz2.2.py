def cutList(toBeCut):
    if len(toBeCut) == 2:
        return toBeCut
    else:
        return [toBeCut[0], toBeCut[len(toBeCut) - 1]]


a = [5, 10, 15, 20, 25]
b = [1, 10]
print(cutList(a))
print(cutList(b))
