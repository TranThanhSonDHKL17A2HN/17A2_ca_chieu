#a) In ra các số nguyên tố từ 100 đến 1000 (kể cả số 1000)
for i in range(100, 1001):
    if i > 1:
        kiem_tra = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                kiem_tra = False
                break
        if kiem_tra:
            print(i, end=" ")
