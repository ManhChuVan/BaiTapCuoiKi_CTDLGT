# Viết phương thức Pascal( ) như sau:
# - Nhập vào số nguyên dương n.
# - Phương thức này sẽ in ra tam giác Pascal ứng với bậc n.
# - Ví dụ n = 4 thì tam giác Pascal là:
# n=0 1
# n=1 1 1
# n=2 1 2 1
# n=3 1 3 3 1
# n=4 1 4 6 4 1

def Pascal(n):
    for i in range(n):
        coef = 1
        print(" " * (n - i), end="")
        for j in range(i + 1):
            print(coef, end=" ")
            coef = coef * (i - j) // (j + 1)
        print()

n = int(input("Nhập vào số nguyên dương n: "))

while n <= 0:
    print("Vui lòng nhập một số nguyên dương.")
    n = int(input("Nhập vào số nguyên dương n: "))

Pascal(n)
