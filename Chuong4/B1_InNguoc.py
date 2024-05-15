class Node:
  def __init__(self, data):
      self.Info = data
      self.Next = None

class DSLK:
  def __init__(self):
      self.Head = None

  def Them(self, data):
      new_node = Node(data)
      if self.Head is None:
          self.Head = new_node
      else:
          current = self.Head
          while current.Next is not None:
              current = current.Next
          current.Next = new_node

  def InNguocDequi(self, node):
      if node is None:
          return
      self.InNguocDequi(node.Next)
      print(node.Info, end=" ")

  def InNguocKhongDequi(self):
      if self.Head is None:
          print("Danh sach rong")
          return
      stack = []
      current = self.Head
      while current is not None:
          stack.append(current.Info)
          current = current.Next
      while stack:
          print(stack.pop(), end=" ")

# Test
dslk = DSLK()
dslk.Them(1)
dslk.Them(2)
dslk.Them(3)
dslk.Them(4)

print("In nguoc bang de qui:")
dslk.InNguocDequi(dslk.Head)
print("\nIn nguoc khong de qui:")
dslk.InNguocKhongDequi()
