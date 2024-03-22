chieu_cao=float(input("Nhap chieu cao(m):"))
can_nang=float(input("Nhap can nang(kg):"))
bmi= can_nang / (chieu_cao ** 2)
if bmi < 18.5:
    print("Gầy")
elif 18.5 <= bmi <= 24.9:
    print("Bình thường")
elif 25 <= bmi < 29.9:
    print("Hơi béo") 
else:
    print("Béo")
          




