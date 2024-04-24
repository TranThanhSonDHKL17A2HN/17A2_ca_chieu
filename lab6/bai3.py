n = int(input("Nhập số lượng số nguyên n: "))
mang = [float(input(f"Nhập vào phần tử thứ  {i + 1}: ")) for i in range (n)]
max = mang[0]
min = mang[0]
for a in mang:
    if max < a:
        max = a
    if a < min:
        min = a
print(f"Max: {max}\nMin: {min}")