def Hop(a, b):
  # Kết hợp hai mảng a và b và loại bỏ các phần tử trùng lặp
  merged = set(a + b)
  # Sắp xếp lại các phần tử của set để có thứ tự tăng dần
  sorted_merged = sorted(merged)
  # Chuyển kết quả từ set đã sắp xếp thành một list
  result = list(sorted_merged)
  return result

# Test
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
print("Mảng a:", a)
print("Mảng b:", b)
print("Mảng chứa các số có trong mảng a và / hoặc mảng b và có thứ tự tăng dần:", Hop(a, b))
