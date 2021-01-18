def findLargestNum(toBeFind):
    i = 0
    while i < len(toBeFind) - 1:
        if toBeFind[i] >= toBeFind[i + 1]:
            toBeFind[i + 1] = toBeFind[i]
        i = i + 1
    print(toBeFind[len(toBeFind) - 1])


findLargestNum([1000, 1001, 857, 1])
findLargestNum([10000, 1000, 100, 10, 1, 0, -1])
findLargestNum([-1,-2,-3])
