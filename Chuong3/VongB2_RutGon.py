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

  def RutGon(self):
    if self.Head is None:
      return

    current = self.Head
    while current is not None and current.KeTiep != self.Head:
      temp = current
      while temp is not None and temp.KeTiep != self.Head:

        if temp.KeTiep.SoMu == current.SoMu:
          current.HeSo += temp.KeTiep.HeSo
          temp.KeTiep = temp.KeTiep.KeTiep
        else:
          temp = temp.KeTiep

      current = current.KeTiep

    # Loại bỏ các node có hệ số bằng 0
    prev = None
    current = self.Head
    while current is not None and current.KeTiep != self.Head:
      if current.HeSo == 0:
        if prev:
          prev.KeTiep = current.KeTiep
        else:
          # Nếu node đầu tiên có hệ số bằng 0, cập nhật lại self.Head
          self.Head = current.KeTiep
      else:
        prev = current
      current = current.KeTiep

    # Kiểm tra node cuối cùng
    if current.HeSo == 0:
      if prev:
        prev.KeTiep = current.KeTiep
      else:
        # Nếu node đầu tiên có hệ số bằng 0, cập nhật lại self.Head
        self.Head = None

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
da_thuc.Them(4, 3)
da_thuc.Them(3, 2)
da_thuc.Them(5, 4)
da_thuc.Them(-4, 1)
da_thuc.Them(-4, 3)
da_thuc.Them(-5, 4)
da_thuc.Them(1, 7)
da_thuc.Them(5, 1)

print("Đa thức ban đầu:")
da_thuc.InDaThuc()
da_thuc.RutGon()
print("\nĐa thức sau khi rút gọn:")
da_thuc.InDaThuc()
