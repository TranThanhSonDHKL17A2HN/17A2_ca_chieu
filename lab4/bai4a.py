n = int(input("Nhập số nguyên n (n > 10): "))
a = 1
s1 = 6

while a <= n:
  s1 += 6 ** a
  a += 1
print("S1=", s1)