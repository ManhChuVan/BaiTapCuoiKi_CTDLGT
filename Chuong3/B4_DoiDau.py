class Node:
  def __init__(self, heso, somu):
      self.HeSo = heso
      self.SoMu = somu
      self.KeTiep = None

class DaThuc:
  def __init__(self):
      self.Head = None

  def Them(self, heso, somu):
      new_node = Node(heso, somu)
      if self.Head is None:
          self.Head = new_node
      else:
          current = self.Head
          while current.KeTiep is not None:
              current = current.KeTiep
          current.KeTiep = new_node

  def DoiDau(self):
      current = self.Head
      while current is not None:
          current.HeSo = -current.HeSo  # Đổi dấu hệ số
          current = current.KeTiep

  def InDaThuc(self):
      if self.Head is None:
          print("Da thuc rong")
          return
      current = self.Head
      while current is not None:
          print(f"{current.HeSo}x^{current.SoMu}", end=" ")
          current = current.KeTiep

# Test
da_thuc = DaThuc()
da_thuc.Them(3, 2)
da_thuc.Them(-4, 1)
da_thuc.Them(5, 0)

print("Da thuc truoc khi doi dau:")
da_thuc.InDaThuc()

da_thuc.DoiDau()
print("\nDa thuc sau khi doi dau:")
da_thuc.InDaThuc()
