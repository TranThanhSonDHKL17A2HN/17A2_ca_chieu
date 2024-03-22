gia_ve_1_nguoi= 120000
so_luong_nguoi=int(input('Nhap so luong nguoi mua ve:'))
if so_luong_nguoi==1:
    print("So tien phai tra la:",gia_ve_1_nguoi)
elif 2<= so_luong_nguoi < 4:
    gia_ve1= (gia_ve_1_nguoi * so_luong_nguoi) - (gia_ve_1_nguoi * so_luong_nguoi) * 0.05
    print("So tien phai tra la",gia_ve1)
elif 4<= so_luong_nguoi < 10:
    gia_ve2 = (gia_ve_1_nguoi * so_luong_nguoi) - (gia_ve_1_nguoi * so_luong_nguoi) * 0.1
    print("So tien phai tra la",gia_ve2)
else:
    gia_ve3=(gia_ve_1_nguoi * so_luong_nguoi) - (gia_ve_1_nguoi * so_luong_nguoi) * 0.2
    print("So tien phai tra la",gia_ve3)