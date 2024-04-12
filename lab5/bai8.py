chuoi = input("Nhập chuỗi ký tự: ")

if len(chuoi) <= 10:
    print("Độ dài chuỗi phải lớn hơn 10 ký tự. Vui lòng nhập lại!")
#a
chuoi_a = chuoi[2:8]
print(f"Chuỗi con từ vị trí 2 đến 8: {chuoi_a}")
#b
chuoi_b = chuoi[5:9]
print(f"Chuỗi con gồm 5 ký tự từ vị trí 5: {chuoi_b}")
#c
chuoi_c = chuoi[-3:]
print(f"Chuỗi con từ cuối chuỗi gồm 3 ký tự: {chuoi_c}")
#d
chuoi_d = chuoi.lower()
print(f"Chuỗi sau khi chuyển đổi sang chữ thường: {chuoi_d}")
#e
chuoi_hoa = chuoi.upper()
print(f"Chuỗi sau khi chuyển đổi sang chữ hoa: {chuoi_hoa}")
#f
chuoi_f = chuoi[::-1]
print(f"Chuỗi sau khi đảo ngược: {chuoi_f}")
