n = int(input("Nhập số lượng số nguyên n: "))
ds = [int(input(f"Nhập vào phần tử thứ {i + 1}: ")) for i in range (n)]
ds_chan = []
ds_le = []
tong_chan = 0
tong_le = 0
for a in ds:
    if a % 2 == 0:
        ds_chan.append(a)
        tong_chan += a
    else:
        ds_le.append(a)
        tong_le += a
print(f"Mảng gồm các số chẵn {ds_chan}")
print(f"Tổng các số chẵn trong mảng: {tong_chan}")
print(f"Mảng gồm các số lẻ {ds_le}")
print(f"Tổng các số lẻ trong mảng: {tong_le}")