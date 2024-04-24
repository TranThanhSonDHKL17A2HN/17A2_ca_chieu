n = int(input("Nhập số lượng số nguyên n: "))
ds = [int(input(f"Nhập vào phần tử thứ {i + 1}: ")) for i in range (n)]
khoang_cach = [ds[i + 1] - ds[i] for i in range(1, len(ds)- 1)]
check = all(kc ==  khoang_cach[0] for kc in khoang_cach)
if check:
    print("Đây là cấp số cộng")
else:
    print("Đây không là cấp số cộng")