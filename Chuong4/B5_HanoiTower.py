class HanoiTower:
  def __init__(self, n):
      self.n = n
      self.tower1 = list(range(n, 0, -1))  # Tháp ban đầu ở vị trí 1
      self.tower2 = []  # Tháp trung gian ở vị trí 2
      self.tower3 = []  # Tháp đích ở vị trí 3

  def move(self, n, source, target, auxiliary):
      if n > 0:
          # Di chuyển (n-1) tầng từ nguồn đến trung gian
          self.move(n - 1, source, auxiliary, target)
          # Di chuyển tầng còn lại từ nguồn đến đích 
          target.append(source.pop())
          print(f"Di chuyển tầng {n} từ tháp {source} đến tháp {target}")
          # Di chuyển (n-1) tầng từ trung gian đến đích
          self.move(n - 1, auxiliary, target, source)

  def solve(self):
      self.move(self.n, self.tower1, self.tower3, self.tower2)


# Test
n = 4  # Số tầng của tháp
hanoi = HanoiTower(n)
print("Tháp ban đầu:")
print("Tháp 1:", hanoi.tower1)
print("Tháp 2:", hanoi.tower2)
print("Tháp 3:", hanoi.tower3)

print("\nBắt đầu giải quyết:")
hanoi.solve()

print("\nTháp sau khi di chuyển:")
print("Tháp 1:", hanoi.tower1)
print("Tháp 2:", hanoi.tower2)
print("Tháp 3:", hanoi.tower3)
