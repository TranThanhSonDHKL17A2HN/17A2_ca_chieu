n = int(input("Nhập số nguyên n (n > 10): "))
a = 1
s3 = -1

while a <= n:
  s3 += ((-1) ** a) * (a ** 2)
  a += 1

print("S3=", s3)