#d
s4 = 0
n = int(input("Nhập n : "))
if n <= 0:
    print("Xin mời nhập lại!!!")
for i in range(1,n+1):
    s4 += ((-1)**(i+1))/i
print(s4)