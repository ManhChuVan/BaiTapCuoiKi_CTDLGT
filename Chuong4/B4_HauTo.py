class BieuThuc:
  def HauTo(self, bt):
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
              toan_hang_stack.append(operand)
              i -= 1
          elif bt[i] in ['+', '-', '*', '/']:
              while toan_tu_stack and self.UuTien(toan_tu_stack[-1]) >= self.UuTien(bt[i]):
                  toan_hang_stack.append(toan_tu_stack.pop())
              toan_tu_stack.append(bt[i])
          i += 1

      while toan_tu_stack:
          toan_hang_stack.append(toan_tu_stack.pop())

      return ' '.join(toan_hang_stack)

  def UuTien(self, toan_tu):
      if toan_tu in ['+', '-']:
          return 1
      elif toan_tu in ['*', '/']:
          return 2
      return 0

# Test
bt = "25 + 6 + 8 / 2 - 4 * 5"
bieu_thuc = BieuThuc()
print("Bieu thuc hau to:", bieu_thuc.HauTo(bt))
