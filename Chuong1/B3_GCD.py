# Viết phương thức GCD( ) như sau:
# - Nhập vào hai số nguyên dương m và n.
# - Phương thức này trả về ước số chung lớn nhất (GCD – Greatest Common Divisor) của m và n theo hai cách: dùng giải thuật đệ qui và dùng giải thuật không đệ qui.
# - Ví dụ: ước số chung lớn nhất của 372 và 84 là 12.
# - Gợi ý:
# Tìm GCD(372, 84): 372 chia 84 dư 36
# Tìm GCD(84, 36): 84 chia 36 dư 12
# Tìm GCD(36, 12): 36 chia 12 dư 0
# Tìm GCD(12, 0): kết thức. Vậy ước số chung lớn nhất của 372 và 84 là 12.


def gcd_recursive(m, n):
  if n == 0:
    return m
  return gcd_recursive(n, m % n)


def gcd_iterative(m, n):
  while n != 0:
    m, n = n, m % n
  return m


m = int(input("Nhập vào số nguyên dương m: "))
n = int(input("Nhập vào số nguyên dương n: "))

while m <= 0 or n <= 0:
  print("Vui lòng nhập hai số nguyên dương.")
  m = int(input("Nhập vào số nguyên dương m: "))
  n = int(input("Nhập vào số nguyên dương n: "))

print("Ước số chung lớn nhất của", m, "và", n, "sử dụng giải thuật đệ qui:",
      gcd_recursive(m, n))
print("Ước số chung lớn nhất của", m, "và", n,
      "sử dụng giải thuật không đệ qui:", gcd_iterative(m, n))
