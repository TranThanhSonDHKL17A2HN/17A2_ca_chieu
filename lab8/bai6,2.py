def is_even(x):
  return x % 2 == 0

def main():
  numbers = [int(num) for num in input("Nhập các số, cách nhau bằng dấu cách: ").split()]
  even_numbers = list(filter(is_even, numbers))
  print(f"Các số chẵn trong danh sách: {even_numbers}")


if __name__ == "__main__":
  main()
