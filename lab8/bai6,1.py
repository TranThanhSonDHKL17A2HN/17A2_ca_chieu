def is_odd(x):
  return x % 2 != 0


def main():
  numbers = [int(num) for num in input("Nhập các số, cách nhau bằng dấu cách: ").split()]
  odd_numbers = list(filter(is_odd, numbers))
  print(f"Các số lẻ trong danh sách: {odd_numbers}")


if __name__ == "__main__":
  main()
