str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")

chuoi_moi = ""
for i in range(len(str1)):
  if i < len(str2):
    chuoi_moi += str1[i] + "-" + str2[i]
  else:
    chuoi_moi += str1[i]

print(f"Chuỗi sau khi trộn: {chuoi_moi}")
