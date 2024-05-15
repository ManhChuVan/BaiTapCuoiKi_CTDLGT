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

  def RutGon(self):
      if self.Head is None:
          return

      current = self.Head
      while current is not None:
          temp = current
          while temp is not None and temp.KeTiep is not None:
              if temp.KeTiep.SoMu == current.SoMu:
                  current.HeSo += temp.KeTiep.HeSo
                  temp.KeTiep = temp.KeTiep.KeTiep
              else:
                  temp = temp.KeTiep
          current = current.KeTiep

      # Xóa các số hạng có hệ số bằng 0
      previous = None
      current = self.Head
      while current is not None:
          if current.HeSo == 0:
              if previous is None:
                  self.Head = current.KeTiep
              else:
                  previous.KeTiep = current.KeTiep
          else:
              previous = current
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
da_thuc.Them(4, 1)
da_thuc.Them(5, 0)
print("Đa thức ban đầu:")
da_thuc.InDaThuc()
da_thuc.Them(-2, 2)  
da_thuc.RutGon()
print("\nĐa thức sau khi rút gọn:")
da_thuc.InDaThuc()
