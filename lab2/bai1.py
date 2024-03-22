a,b=map(int,input("Nhap hai so a,b:").split())
if a==0:
    if b==0:
        print('Phuong trinh vo so nghiem')
    else:
        print('Phuong trinh vo nghiem')
else:
    x=-b/a
    print("Nghiem cua phuong trinh la:",x)



