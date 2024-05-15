class BieuThuc:
  def GiaTri(self, bt):
      if not bt:
          return None

      toan_hang_stack = []
      toan_tu_stack = []

      i = 0
      while i < len(bt):
          if bt[i].isdigit():
              operand = ""
              while i < len(bt) and bt[i].isdigit():
                  operand += bt[i]
                  i += 1
              toan_hang_stack.append(int(operand))
              i -= 1
          elif bt[i] in ['+', '-', '*', '/']:
              while toan_tu_stack and self.UuTien(toan_tu_stack[-1]) >= self.UuTien(bt[i]):
                  self.ThucHienPhepTinh(toan_hang_stack, toan_tu_stack)
              toan_tu_stack.append(bt[i])
          i += 1

      while toan_tu_stack:
          self.ThucHienPhepTinh(toan_hang_stack, toan_tu_stack)

      return toan_hang_stack[-1]

  def UuTien(self, toan_tu):
      if toan_tu in ['+', '-']:
          return 1
      elif toan_tu in ['*', '/']:
          return 2
      return 0

  def ThucHienPhepTinh(self, toan_hang_stack, toan_tu_stack):
      if len(toan_hang_stack) < 2 or len(toan_tu_stack) < 1:
          return
      operand2 = toan_hang_stack.pop()
      operand1 = toan_hang_stack.pop()
      operator = toan_tu_stack.pop()
      if operator == '+':
          toan_hang_stack.append(operand1 + operand2)
      elif operator == '-':
          toan_hang_stack.append(operand1 - operand2)
      elif operator == '*':
          toan_hang_stack.append(operand1 * operand2)
      elif operator == '/':
          toan_hang_stack.append(operand1 / operand2)

# Test
bt = "31+5*2-6/3"
bieu_thuc = BieuThuc()
print("Gia tri cua bieu thuc la:", bieu_thuc.GiaTri(bt))
