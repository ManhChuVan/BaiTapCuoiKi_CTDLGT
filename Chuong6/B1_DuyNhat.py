def Duynhat(a):
  # Loại bỏ các phần tử trùng lặp bằng cách chuyển a thành một set
  unique_set = set(a)
  # Sắp xếp lại các phần tử của set để có thứ tự tăng dần
  unique_sorted = sorted(unique_set)
  # Chuyển kết quả từ set đã sắp xếp thành một list
  result = list(unique_sorted)
  return result

# Test
a = [1, 5, 3, 7, 5, 9, 7]
print("Mảng ban đầu:", a)
print("Mảng chỉ chứa các số duy nhất và có thứ tự tăng dần:", Duynhat(a))
