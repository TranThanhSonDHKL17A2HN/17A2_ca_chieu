#c
s3 =0
n = int(input("Nhập n : "))
if n <= 0:
    print("Xin mời nhập lại!!!")
for i in range(1,n+1):
    s3 += 1/((2*i)**0.5)
print(s3)