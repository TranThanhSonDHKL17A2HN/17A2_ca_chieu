def giai_thua(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def hoan_vi(n, r):
    return giai_thua(n) // giai_thua(n - r)

def to_hop(n, r):
    return hoan_vi(n, r) // giai_thua(r)

def main():
  n = int(input("Nhập số lượng phần tử (n): "))
  r = int(input("Nhập số lượng phần tử được lấy mỗi lần (r): "))

  print(f"Số hoán vị của {n} phần tử lấy {r} phần tử mỗi lần (p(n, r)): {hoan_vi(n, r)}")
  print(f"Số tổ hợp của {n} phần tử lấy {r} phần tử mỗi lần (c(n, r)): {to_hop(n, r)}")


if __name__ == "__main__":
  main()