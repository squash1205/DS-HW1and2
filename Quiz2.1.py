def CheckA(toBeCheck):
    i = 0
    found = 0
    while i < len(toBeCheck):
        if toBeCheck[i] == "a":
            found = found + 1
        i = i + 1
    if found > 0:
        print("Yes")
    else:
        print("No")


checker = input()
CheckA(checker)
