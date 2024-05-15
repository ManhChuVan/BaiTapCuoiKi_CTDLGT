class Fibonacci:

  def recursive_fibonacci(n):
      if n <= 0:
          return 0
      elif n == 1:
          return 1
      else:
          return Fibonacci.recursive_fibonacci(n - 1) + Fibonacci.recursive_fibonacci(n - 2)

  def iterative_fibonacci(n):
      if n == 0:
        return 0
      elif n == 1:
          return 1
      else:
          a, b = 0, 1
          for _ in range(2, n + 1):
              c = a + b
              a, b = b, c
          return c

n = int(input("Nhập số nguyên n (n>=0): "))
while n < 0:
  print("Số nguyên n không đúng điều kiện, hãy nhập lại!")
  n=int(input("Nhập số nguyên n (n>=0): "))
recursive_result = Fibonacci.recursive_fibonacci(n)
iterative_result = Fibonacci.iterative_fibonacci(n)
print("Sử dụng đệ quy: F{} = {}".format(n, recursive_result))
print("Không sử dụng đệ quy: F{} = {}".format(n, iterative_result))