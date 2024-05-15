def Cong(a, b):
  n = len(a)
  m = len(b)

  # Xác định độ dài của mảng kết quả
  max_len = max(n, m)
  result = [0] * (max_len + 1)

  # Biến đếm để theo dõi việc tràn số
  carry = 0

  # Thực hiện cộng từ hàng đơn vị đến hàng cao nhất
  for i in range(max_len - 1, -1, -1):
      if n > 0:
          digit_a = int(a[n - 1])
          n -= 1
      else:
          digit_a = 0

      if m > 0:
          digit_b = int(b[m - 1])
          m -= 1
      else:
          digit_b = 0

      # Thực hiện cộng từng cặp số và cập nhật kết quả
      temp_sum = digit_a + digit_b + carry
      if temp_sum > 9:
          carry = 1
          result[i + 1] = temp_sum - 10
      else:
          carry = 0
          result[i + 1] = temp_sum

  # Nếu carry vẫn còn, có nghĩa là kết quả đã tràn
  if carry == 1:
      return [-1]

  # Loại bỏ các số 0 ở đầu nếu có
  if result[0] == 0:
      result = result[1:]

  return result

# Test phương thức Cong
a = [2, 9, 3]
b = [3, 5, 4]

print(Cong(a, b))  # Kết quả: [1, 1, 2, 2]


# a = [2, 5, 9]
# b = [7, 6, 7]


# def Cong(a, b):
#     c = []
#     for i in range(len(a)):
#         temp = a[i] + b[i]
#         if temp>9:
#            c.append(-1)
#         else:
#            c.append(temp)
#     return c

# print(Cong(a,b))