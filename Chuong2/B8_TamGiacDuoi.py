def TamGiacDuoi(mang):
  n = len(mang)
  for i in range(n):
      for j in range(i + 1, n):
          if mang[i][j] != 0:
              return False
  return True

mang = [[1, 0, 0],
        [5, 4, 0],
        [2, 3, 6]]
print(TamGiacDuoi(mang))