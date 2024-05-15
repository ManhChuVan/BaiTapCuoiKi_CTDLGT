# Viết phương thức Neper( ) như sau:
# - Số e là tổng của các số hạng ak = 1/(k!) với k = 0, 1, 2, ...
# - Nhập vào số nguyên n ≥ 0.
# - Phương thức trả về tổng của a0 + a1 + ... +an.
# - Gợi ý:
# Xét sự liên hệ giữa hai số hạng kế tiếp nhau ai và ai+1.

def giaiThua(n):
  return 1 if n == 0 else n * giaiThua(n - 1)

def neper(n):
  sum = 0
  for i in range(n + 1):
    sum += 1 / giaiThua(i)
  return sum

# def neper_DeQuy(n):
#     if n == 0:
#         return 1
#     else:
#         return 1/(giaiThua(n)) + neper_DeQuy(n-1)

n = int(input("Nhập vào số nguyên n (n >= 0): "))
while n < 0:
  print("Vui lòng nhập số nguyên không âm.")
  n = int(input("Nhập vào số nguyên n (n >= 0): "))
print("Tổng của các số hạng a0 + a1 + ... + an:", neper(n))