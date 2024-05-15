# Viết phương thức Number( ) như sau:
# - n là một số nguyên dương và s là tổng các ước số của nó (kể cả số 1).
# - n là deficient nếu s < n
# - n là perfect nếu s = n

# - n là abundant nếu s = n.
# - Nhập vào hai số nguyên dương x và y với x ≤ y.
# - Phương thức sẽ in ra phân loại (deficient, perfect, abundant) của các số từ x đến y.
# - Ví dụ: số 8 là deficient vì 1 + 2 + 4 < 8; số 6 là perfect vì 1 + 2 + 3 = 6; số 12 là abundant vì 1 + 2 + 3 + 4 + 6 > 12.

#----

def calculate_divisors_sum(n):
  divisors_sum = 1 
  for i in range(2, n):
    if n % i == 0:
      divisors_sum += i
  return divisors_sum

def Number(x, y):
  for num in range(x, y + 1):
    div_sum = calculate_divisors_sum(num)
    if div_sum < num:
      print(f"{num} là deficient")
    elif div_sum == num:
      print(f"{num} là perfect")
    else:
      print(f"{num} là abundant")


x = int(input("Nhập vào số nguyên dương x: "))
y = int(input("Nhập vào số nguyên dương y (y ≥ x): "))


while y < x:
  print("Vui lòng nhập y lớn hơn hoặc bằng x.")
  y = int(input("Nhập vào số nguyên dương y (y ≥ x): "))

Number(x, y)
