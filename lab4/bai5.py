
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))

while True:
  print("Chọn phép toán bạn muốn thực hiện:")
  print("1. Cộng (+)")
  print("2. Trừ (-)")
  print("3. Nhân (*)")
  print("4. Chia (/)")
  print("5. Lũy thừa (**)")
  print("6. Tính căn bậc hai (√)")

  lua_chon = int(input("Lựa chọn của bạn (1-6): "))


  if lua_chon == 1:
    ket_qua = a + b
    print(f"{a} + {b} = {ket_qua}")
  elif lua_chon == 2:
    ket_qua = a - b
    print(f"{a} - {b} = {ket_qua}")
  elif lua_chon == 3:
    ket_qua = a * b
    print(f"{a} * {b} = {ket_qua}")
  elif lua_chon == 4:
    if b == 0:
      print("Lỗi: Không thể chia cho 0!")
    else:
      ket_qua = a / b
      print(f"{a} / {b} = {ket_qua}")
  elif lua_chon == 5:
    ket_qua = a ** b
    print(f"{a} ** {b} = {ket_qua}")
  elif lua_chon == 6:
    if a < 0:
      print("Lỗi: Căn bậc hai của số âm không tồn tại!")
    else:
      ket_qua = a ** 0.5
      print(f"Can bac hai cua {a} = {ket_qua}")
    if b < 0:
      print("Lỗi: Căn bậc hai của số âm không tồn tại!")
    else:
      ket_qua = b ** 0.5
      print(f"Can bac hai cua {b} = {ket_qua}")
  else:
    print("Lựa chọn không hợp lệ!")


  tiep_tuc = input("Bạn muốn tiếp tục không (y/n): ")

  if tiep_tuc == "n":
    print("Ket thuc chuong trinh!!!!!")
    break

