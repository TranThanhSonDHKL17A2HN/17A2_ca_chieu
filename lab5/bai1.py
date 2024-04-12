n = int(input("Nhập số thập phân: "))
so_nhi_phan = ""
while n > 0:
  so_du = n % 2
  so_nhi_phan = str(so_du) + so_nhi_phan
  n //= 2

print(f"Số nhị phân của {n} là: {so_nhi_phan}")
