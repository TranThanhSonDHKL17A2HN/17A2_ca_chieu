def cube(x):
  return x * x * x

def main():
  numbers = [int(num) for num in input("Nhập các số, cách nhau bằng dấu cách: ").split()]
  cubed_numbers = list(map(cube, numbers))
  print(f"Danh sách lập phương: {cubed_numbers}")


if __name__ == "__main__":
  main()
