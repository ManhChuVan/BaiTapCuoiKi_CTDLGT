def TrungHang(mang):
  n = len(mang)
  for i in range(n - 1):
      for j in range(i + 1, n):
          if mang[i] == mang[j]:
              return True
  return False

mang = [[0, 2, 3],
        [5, 5, 6],
        [5, 5, 6]]

print(TrungHang(mang))  