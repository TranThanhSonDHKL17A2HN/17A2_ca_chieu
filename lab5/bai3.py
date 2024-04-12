chuoi = input("Nhập chuỗi văn bản: ")
tu_can_tim = input("Nhập từ cần tìm kiếm: ")

vi_tri = chuoi.find(tu_can_tim)

if vi_tri != -1:
  print(f"Từ '{tu_can_tim}' xuất hiện tại vị trí {vi_tri} trong chuỗi.")
else:
  print(f"Không tìm thấy từ '{tu_can_tim}' trong chuỗi.")

tu_xuat_hien_nhieu_nhat = ""
so_lan_xuat_hien_toi_da = 0

danh_sach_tu = chuoi.split()

for tu in danh_sach_tu:
  so_lan_xuat_hien_tu = danh_sach_tu.count(tu)
  if so_lan_xuat_hien_tu > so_lan_xuat_hien_toi_da:
    so_lan_xuat_hien_toi_da = so_lan_xuat_hien_tu
    tu_xuat_hien_nhieu_nhat = tu


print("Từ xuất hiện nhiều nhất trong chuỗi là:",tu_xuat_hien_nhieu_nhat)


