#b
s2 =0
n = int(input("Nhập n : "))
if n <= 0:
    print("Xin mời nhập lại!!!")
for i in range(1,n+1):
    s2 += 1/i
print(s2)