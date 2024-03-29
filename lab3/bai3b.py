#b) In ra các số chính phương từ 1 đến 1000 (kể cả số 1000)
for i in range(1,1001):
    for j in range(1,i+1):
        if j*j == i:
            print(i, end = ' ')