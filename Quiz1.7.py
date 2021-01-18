def max(a, b, c):
    if a >= b:
        b = a
    if (b >= c):
        c = b
    return c


print(max(1, 100, 1000))
print(max(50, 25, 1))
print(max(3, 9, 6))
