def Hieu(a, b):
  # Chuyển mảng a và b thành set để loại bỏ các phần tử trùng lặp
  set_a = set(a)
  set_b = set(b)
  # Tạo một set mới chứa các phần tử chỉ có trong mảng a (không có trong mảng b)
  diff_set = set_a.difference(set_b)
  # Sắp xếp lại các phần tử của set để có thứ tự tăng dần
  sorted_diff = sorted(diff_set)
  # Chuyển kết quả từ set đã sắp xếp thành một list
  result = list(sorted_diff)
  return result

# Test
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
print("Mảng a:", a)
print("Mảng b:", b)
print("Mảng chứa các số chỉ có trong mảng a và có thứ tự tăng dần:", Hieu(a, b))
