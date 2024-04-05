n = int(input("Nhập số nguyên n (n > 10): "))
a = 1
s4 = 1

while a <= n:
  s4 *= (a + 2)
  a += 1

print("S4=", s4)
