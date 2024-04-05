n = int(input("Nhập số nguyên n (n > 10): "))
a = 1
s2 = 1 / 3

while a <= n:
    s2 += 1 / (3 ** (2 * a + 1))
    a += 1

print("S2=", s2)
