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
          new_node.KeTiep = self.Head  # Node đầu tiên trỏ đến chính nó
      else:
          current = self.Head
          while current.KeTiep != self.Head:  # Duyệt tới node cuối cùng
              current = current.KeTiep
          current.KeTiep = new_node
          new_node.KeTiep = self.Head  # Node mới trỏ đến node đầu tiên, tạo thành vòng

  def InDaThuc(self):
      if self.Head is None:
          print("Da thuc rong")
          return
      current = self.Head
      while True:
          print(f"{current.HeSo}x^{current.SoMu}", end=" ")
          current = current.KeTiep
          if current == self.Head:  # Kết thúc vòng
              break

# Test
da_thuc = DaThuc()
da_thuc.Them(3, 2)
da_thuc.Them(4, 1)
da_thuc.Them(5, 0)
da_thuc.InDaThuc()
