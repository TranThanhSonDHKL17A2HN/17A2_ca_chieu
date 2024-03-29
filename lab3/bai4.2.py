a = 7
for i in range(1, a + 1):
    print(" " * (a - i) + "*" * (2 * i - 1))
b = 3
for i in range(1, b + 1):
    print(" " * ((a - b) + 1) + "*" * b)