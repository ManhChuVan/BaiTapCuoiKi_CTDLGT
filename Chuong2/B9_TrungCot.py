def TrungCot(mang):
  n = len(mang)
  for i in range(n - 1):
    for j in range(i+1, n):
      for k in range(n):
        if mang[k][i] != mang[k][j]:
          break
      else:
        return True
  return False
          

mang = [[2, 1, 2, 1], 
        [3, 2, 3, 2], 
        [4, 4, 4, 4],
        [5, 5, 5, 5]]

print(TrungCot(mang))
