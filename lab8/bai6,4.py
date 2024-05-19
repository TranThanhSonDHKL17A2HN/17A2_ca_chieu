def is_even(x):
  return x % 2 == 0

def cube(x):
  return x * x * x

def main():
  numbers = [int(num) for num in input("Nhập các số, cách nhau bằng dấu cách: ").split()]
  even_numbers = list(filter(is_even, numbers))  # Lọc số chẵn
  cubed_even_numbers = list(map(cube, even_numbers))  # Tính lập phương số chẵn
  print(f"Danh sách lập phương các số chẵn: {cubed_even_numbers}")


if __name__ == "__main__":
  main()
