def Giao(a, b):
  # Chuyển mảng a thành set để loại bỏ các phần tử trùng lặp
  set_a = set(a)
  # Khởi tạo một set mới để chứa các phần tử giao nhau của mảng a và b
  intersect_set = set()
  # Duyệt qua từng phần tử của mảng b
  for num in b:
      # Nếu phần tử này có trong set của mảng a thì thêm vào set mới
      if num in set_a:
          intersect_set.add(num)
  # Sắp xếp lại các phần tử của set để có thứ tự tăng dần
  sorted_intersect = sorted(intersect_set)
  # Chuyển kết quả từ set đã sắp xếp thành một list
  result = list(sorted_intersect)
  return result

# Test
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]
print("Mảng a:", a)
print("Mảng b:", b)
print("Mảng chứa các số giao nhau của mảng a và mảng b và có thứ tự tăng dần:", Giao(a, b))
