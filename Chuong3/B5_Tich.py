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

  def Tich(self, dathuc2):
      result = DaThuc()
      current1 = self.Head
      while current1 is not None:
          current2 = dathuc2.Head
          while current2 is not None:
              result.Them(current1.HeSo * current2.HeSo, current1.SoMu + current2.SoMu)
              current2 = current2.KeTiep
          current1 = current1.KeTiep
      result.RutGon()
      return result

  def InDaThuc(self):
      if self.Head is None:
          print("Da thuc rong")
          return
      current = self.Head
      while current is not None:
          print(f"{current.HeSo}x^{current.SoMu}", end=" ")
          current = current.KeTiep

# Test
da_thuc1 = DaThuc()
da_thuc1.Them(3, 2)
da_thuc1.Them(4, 1)
da_thuc1.Them(5, 0)

da_thuc2 = DaThuc()
da_thuc2.Them(2, 2)
da_thuc2.Them(1, 1)
da_thuc2.Them(3, 0)

result = da_thuc1.Tich(da_thuc2)
print("Da thuc tich:")
result.InDaThuc()
