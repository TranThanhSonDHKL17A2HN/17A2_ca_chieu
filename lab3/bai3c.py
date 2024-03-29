#c) In ra chuỗi Fibonacci sao cho số cuối cùng trong chuỗi nhỏ hơn 100
x, y = 0, 1
for _ in range(100):
    if x >= 100:
        break
    print(x, end=' ')
    x, y = y, x + y
