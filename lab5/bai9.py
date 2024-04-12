str1 = input("Nhập chuỗi 1: ")
str2 = input("Nhập chuỗi 2: ")

a = len(str1)
b = len(str2)
dem = abs(a - b)

if a == b:
    for i in range(a):
        if str1[i] != str2[i]:
            dem += 1

print(f"Có thể biến đổi chuỗi 1 thành chuỗi 2 bằng cách thêm, xóa hoặc thay đổi {dem} ký tự.")

