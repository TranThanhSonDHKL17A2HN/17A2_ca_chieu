tong=0
so_da_nhap=""
so_chan=""
so_le=""
i=0
while True:
    a=int(input("Nhap so nguyen duong:"))
    i += 1
    so_da_nhap += str(a) + " "
    tong += a 
    if a <= 0:
        break
    elif tong > 1000:
        break
    elif a % 2 ==0:
        so_chan += str(a) + " "
    else:
        so_le += str(a) + " "

print("a) Các số lẻ đã nhập:", so_le)
print("b) Các số chẵn đã nhập:", so_chan)
print("c) Đếm số lượng số nguyên đã nhập:",i )






