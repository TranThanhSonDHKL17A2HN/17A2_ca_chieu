n = int(input("Nhập số lượng số nguyên n: "))
mang = [int(input(f"Nhập vào phần tử thứ {i + 1}: ")) for i in range (n)]
nguyen_to = []
# Kiểm tra số nguyên tố
for so in mang:
    if so <= 1:
        continue
    check = True
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            check = False
            break
    if check:
        nguyen_to.append(so)
print(f"Các số nguyên tố trong mảng:{nguyen_to}")

# Kiểm tra số hoàn hảo
hoan_hao = []
for number in mang:
    tong_uoc = 0
    for j in range(1, number):
        if number % j == 0:
            tong_uoc += j
    if tong_uoc == number:
        hoan_hao.append(number)
print(f"Các số hoàn hảo trong mảng là:{hoan_hao}")