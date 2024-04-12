chuoi = input("Nhập chuỗi ký tự: ")

chuoi_so = ""
for ky_tu in chuoi:
  if ky_tu.isnumeric():
    chuoi_so += ky_tu

print(f"Chuỗi sau khi được tách: {chuoi_so}")
so = int(chuoi_so)
ket_qua = True

if so < 2:
    ket_qua = False
else:
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            ket_qua = False
            break

if ket_qua:
    print(f"{so} là số nguyên tố.")
else:
    print(f"{so} không phải là số nguyên tố.")
