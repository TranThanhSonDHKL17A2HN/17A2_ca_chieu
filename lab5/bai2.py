str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")
chuoi =""
m = len(str1)
n = len(str2)
ky_tu_con= str1 if m < n else str2
for i in range(1,m+1):
    for j in range(1,n+1):
        a=0
        while (i+a)< m and (j+a) < n and str1[i + a] == str2[j + a]:
            chuoi += str1[i +a]
            a += 1
        if len(chuoi) > 0 and len(chuoi) < len(ky_tu_con):
            ky_tu_con=chuoi
        chuoi=""

if ky_tu_con:
    print("Chuỗi ký tự con chung ngắn nhất:", ky_tu_con)
else:
    print("Không có chuỗi ký tự con chung.")
