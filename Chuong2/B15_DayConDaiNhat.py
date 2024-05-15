def DayConDaiNhat(a, b):
  c = []
  for i in range(len(a)):
    for j in range(len(b)):
      if a[i] == b[j]:
        temp_a = a[i:]
        temp_b = b[j:]
        subsequence = []
        while temp_a and temp_b and temp_a[0] == temp_b[0]:
          subsequence.append(temp_a[0])
          temp_a.pop(0)
          temp_b.pop(0)

        if len(subsequence) > len(c):
          c = subsequence

  return c

a = [1, 6, 2, 1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 5, 3, 7, 9, 8]
print("Dãy con dài nhất ", DayConDaiNhat(a, b)) 
