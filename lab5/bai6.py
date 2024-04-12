chuoi = input("Nhập chuỗi: ")

so_lan_xuat_hien = {}
tong_so_ky_tu = 0

for ky_tu in chuoi:
  if not ky_tu.isalnum():
    if ky_tu in so_lan_xuat_hien:
      so_lan_xuat_hien[ky_tu] += 1
    else:
      so_lan_xuat_hien[ky_tu] = 1
    tong_so_ky_tu += 1

print("Kết quả:")
for ky_tu, so_lan in so_lan_xuat_hien.items():
  ti_le_phan_tram = (so_lan / tong_so_ky_tu) * 100
  print(f"Ký tự '{ky_tu}': Xuất hiện {so_lan} lần, chiếm {ti_le_phan_tram:.2f}%")

