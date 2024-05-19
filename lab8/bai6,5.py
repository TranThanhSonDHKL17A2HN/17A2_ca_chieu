def is_odd(x):
  return x % 2 != 0

def square(x):
  return x * x

def main():
  numbers = [int(num) for num in input("Nhập các số, cách nhau bằng dấu cách: ").split()]
  odd_numbers = list(filter(is_odd, numbers))  # Lọc số lẻ
  squared_odd_numbers = list(map(square, odd_numbers))  # Tính bình phương số lẻ
  print(f"Danh sách bình phương các số lẻ: {squared_odd_numbers}")


if __name__ == "__main__":
  main()
