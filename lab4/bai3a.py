so = int(input("Nhập vào số nguyên: "))
dem_chu_so = 0

while so > 0:
  dem_chu_so += 1
  so //= 10
print("Số chữ số của số nguyên đã nhập là:", dem_chu_so)