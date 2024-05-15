def NhomHang(matrix):
  n = len(matrix)
  groups = []

  for i in range(n):
      found = False
      row_value = matrix[i]
      for group in groups:
          if matrix[group[0]] == row_value:
              group.append(i)
              found = True
              break
      if not found:
          groups.append([i])
        
  for group in groups:
      print("Group:", group)

mang = [[1, 2, 3],
        [5, 5, 6],
        [1, 4, 3]]
NhomHang(mang)