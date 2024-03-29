#e) In ra tổng của các số ngũ giác trong đoạn từ 1 đến 200 (kể cả số 200)
for i in range(1, 201):
    ngu_giac = (i * (3 * i - 1)) / 2
    if ngu_giac <= 200:
        print(ngu_giac, end=' ')
        