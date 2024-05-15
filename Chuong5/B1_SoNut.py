class Node:
  def __init__(self, data):
      self.Info = data
      self.Left = None
      self.Right = None

class Cay:
  def __init__(self):
      self.Root = None

  def SoNut(self, root):
      if root is None:
          return 0
      return self.SoNut(root.Left) + self.SoNut(root.Right) + 1

# Test
cay = Cay()
cay.Root = Node(1)
cay.Root.Left = Node(2)
cay.Root.Right = Node(3)
cay.Root.Left.Left = Node(4)
cay.Root.Left.Right = Node(5)

print("So nut cua cay:", cay.SoNut(cay.Root))
