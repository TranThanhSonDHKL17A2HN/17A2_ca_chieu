a, b = map(float, input("Nhap he so goc va he so tu do cua duong thang thu nhat: ").split())
c, d = map(float, input("Nhap he so goc va he so tu do cua duong thang thu hai: ").split())

if a * c == -1:
    print("Hai duong thang vuong goc!!!!!!!")
elif a == c and b != d:
    print("Hai duong thang song song!!!!")
elif a != c:
    print("Hai duong thang cat nhau!!!!!!!")