#b
a = 0
for i in range(500,1001):
    if i % 4 == 0 and i % 6 != 0:
        a += i
print(a)