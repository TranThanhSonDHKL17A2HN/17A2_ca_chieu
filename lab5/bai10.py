chuoi = input("Nhập chuỗi: ")
chuoi_moi = ""
for ky_tu in chuoi:
    if ky_tu != " ":
        chuoi_moi += ky_tu


print(f"Chuỗi sau khi xóa khoảng trắng thừa: {chuoi_moi}")
