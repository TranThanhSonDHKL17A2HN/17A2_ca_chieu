#d) In ra các số hoàn hảo bé hơn 500
for i in range(2,501):
    tong = 0
    for  j in range(1,i+1):
        if i % j == 0:
            tong += j
            if tong == i:
                print(i, end = ' ')