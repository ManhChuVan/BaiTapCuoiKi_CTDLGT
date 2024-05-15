def Nhan(a, b):
  # Chuyển đổi mảng a và b thành các số nguyên
  num1 = int(''.join(map(str, a)))
  num2 = int(''.join(map(str, b)))

  # Kiểm tra xem kết quả nhân có vượt qua giới hạn không
  result = num1 * num2
  if result > 10**len(a):
      return [-1] * (len(a) + len(b) - 1)

  # Chuyển đổi kết quả về dạng mảng
  return list(map(int, str(result)))

a = [2, 2, 1]
b = [1, 0, 3]
print(Nhan(a, b))