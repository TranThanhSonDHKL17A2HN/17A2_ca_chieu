n = int(input("Nhập n: "))
nguyen_to = [so for so in range(2, 100) if all(so % i != 0 for i in range(2, int(so ** 0.5) + 1))][:n]
print(f"Danh sách {n} số nguyên tố đầu tiên: {nguyen_to}")