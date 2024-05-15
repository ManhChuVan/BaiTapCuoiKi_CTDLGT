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

  def SoNutLa(self, root):
    if root is None:
      return 0
    # if self.SoNut(self.Root) == 1:
    #   return 0
    if root.Left is None and root.Right is None and root != self.Root:  # Nếu là nút lá
      return 1
    return self.SoNutLa(root.Left) + self.SoNutLa(root.Right)


# Test
cay = Cay()
cay.Root = Node(1)
# cay.Root.Left = Node(2)
# cay.Root.Right = Node(3)
# cay.Root.Left.Left = Node(4)
# cay.Root.Right.Right = Node(5)
# cay.Root.Right.Right.Right = Node(6)

print("So nut la cua cay:", cay.SoNutLa(cay.Root))
