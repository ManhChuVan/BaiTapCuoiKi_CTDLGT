class Node:
  def __init__(self, data):
      self.Info = data
      self.Left = None
      self.Right = None

class Cay:
  def __init__(self):
      self.Root = None

  def ChieuCao(self, root):
      if root is None:
          return 0
      return max(self.ChieuCao(root.Left), self.ChieuCao(root.Right)) + 1


# Test
cay = Cay()
cay.Root = Node(1)
cay.Root.Left = Node(2)
cay.Root.Right = Node(3)
cay.Root.Left.Left = Node(4)
cay.Root.Right.Right = Node(5)
cay.Root.Right.Right.Right = Node(6)

print("Chieu cao cua cay:", cay.ChieuCao(cay.Root))
