def Tru(a, b):
    if len(a) < len(b):
        return None  # Hoặc xử lý theo ý định của bạn khi độ dài của a nhỏ hơn b

    # Điều chỉnh độ dài của a và b để có cùng độ dài
    b = [0] * (len(a) - len(b)) + b

    result = []
    borrow = 0

    for i in range(len(a) - 1, -1, -1):
        digit_a = int(a[i])
        digit_b = int(b[i]) + borrow

        if digit_a < digit_b:
            digit_a += 10
            borrow = 1
        else:
            borrow = 0

        result.insert(0, str(digit_a - digit_b))

    # Xóa các số 0 không cần thiết ở đầu kết quả
    while len(result) > 1 and result[0] == '0':
        del result[0]

    return result


a = [2, 2, 6]
b = [3, 5]
print(Tru(a, b))