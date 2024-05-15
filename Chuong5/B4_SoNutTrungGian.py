class Node:
  def __init__(self, data):
      self.Info = data
      self.Left = None
      self.Right = None

class Cay:
  def __init__(self):
      self.Root = None
  def SoNutTrungGian(self, root):
      if root is None:
          return 0
      if ((root.Left is None and root.Right is not None) or 
          (root.Left is not None and root.Right is None)) and root != self.Root:
          return 1 + self.SoNutTrungGian(root.Left) + self.SoNutTrungGian(root.Right)
      return self.SoNutTrungGian(root.Left) + self.SoNutTrungGian(root.Right)

# Test
cay = Cay()
cay.Root = Node(1)
cay.Root.Left = Node(2)
cay.Root.Left.Left = Node(3)
cay.Root.Left.Right = Node(4)
cay.Root.Right = Node(5)
cay.Root.Right.Right = Node(6)
cay.Root.Right.Right.Right = Node(7)

print("So nut trung gian cua cay:", cay.SoNutTrungGian(cay.Root))
