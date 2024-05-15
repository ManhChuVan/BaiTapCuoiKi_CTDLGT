def TamGiacTren(mang):
    n = len(mang)
    for i in range(n):
      for j in range(i + 1, n):  
        print(mang[j][i])
        if mang[j][i] != 0:  
          return False
    return True

mang = [[1, 2, 3, 4],
        [0, 4, 5, 8],
        [0, 0, 6, 9],
        [0, 0, 0, 10]]
print(TamGiacTren(mang))  
