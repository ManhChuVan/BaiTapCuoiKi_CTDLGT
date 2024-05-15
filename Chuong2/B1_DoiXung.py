def DoiXung(mang):
    n = len(mang)
    for i in range(n):
        for j in range(n):
            if mang[i][j] != mang[j][i]:
                return False
    return True

mang = [[1, 2, 3],
        [2, 4, 5],
        [5, 5, 6]]

print(DoiXung(mang))  


mang = [[1, 2, 3],
        [2, 4, 2],
        [3, 2, 1]]
print(DoiXung(mang))  