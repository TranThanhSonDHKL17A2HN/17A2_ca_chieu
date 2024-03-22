import math
x1,y1 = map(float, input("Nhap toa do tam duong tron: ").split())
x2,y2 = map(float, input("Nhap he so goc va he so tu do cua duong thang: ").split())
r = float(input("Nhap ban kinh duong tron: "))
h = abs(x1*x2 + y1*y2 - y2) / math.sqrt(x2**2 + y2**2)
if h < r:
    print("Duong thang cat hoac nam trong duong tron!!!")
elif h == r:
    print("Duong thang tiep xuc duong tron!!!")
elif h > r:
    print("Duong thang nam ngoai duong tron!!!")