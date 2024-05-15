# def TrungCot(mang):
#   n = len(mang)
#   for i in range(n - 1):
#     for j in range(i+1, n):
#       for k in range(n):
#         if mang[k][i] != mang[k][j]:
#           break
#       else:
#         print("Cột " + str(i) + " và cột " + str(j) + " giống nhau")

#   print("Không có cột nào giống nhau")


# mang = [[2, 1, 2, 1], 
#         [3, 2, 3, 2], 
#         [4, 4, 4, 4],
#         [5, 5, 5, 5]]

# print(TrungCot(mang))


def NhomCot(matrix):
    m = len(matrix[0])
    groups = []

    for j in range(m):
        found = False
        col_value = [matrix[i][j] for i in range(len(matrix))]
        for group in groups:
            if group[0] == col_value:
                group.append(j)
                found = True
                break
        if not found:
            groups.append([col_value, j])

    for group in groups:
        print("Group:", group[1:])


mang = [[2, 1, 2, 1], 
        [3, 2, 3, 2], 
        [4, 4, 4, 4],
        [5, 5, 5, 5]]

NhomCot(mang)
