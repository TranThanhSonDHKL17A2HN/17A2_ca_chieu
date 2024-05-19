def cubesum(n):
    sum_of_cubes = 0
    for digit in str(n):
        sum_of_cubes += int(digit) ** 3
    return sum_of_cubes

def PrintArmstrong():
    for num in range(1000):
        if cubesum(num) == num:
            print(num)

def isArmstrong():
    number = int(input("Nhập số bất kì: "))
    digit_sum = sum(int(digit) ** 3 for digit in str(number))
    if digit_sum == number:
        print(f"Số {number} là số Armstrong")
    else:
        print(f"Số {number} không là số Armstrong")

PrintArmstrong()
isArmstrong()

