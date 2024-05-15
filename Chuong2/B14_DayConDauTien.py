def DayConDauTien(a, b):
  c = []
  for i in range(len(a)):
    for j in range(len(b)):
      while i < len(a) - 1 and j < len(b) - 1 and a[i] == b[j]:    
        m = i+1
        n = j+1
        if a[m] == b[n]:
          c.append(a[i])
          c.append(a[m])
          return c
        else:
          break
  return c

a = [1, 6, 2, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 5, 3, 7, 8]
print("Dãy con đầu tiên: ", DayConDauTien(a, b))
