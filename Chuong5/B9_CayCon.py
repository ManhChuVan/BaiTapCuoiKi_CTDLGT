class Node:
  def __init__(self, data):
    self.Info = data
    self.Left = None
    self.Right = None

class Cay:
  def __init__(self):
    self.Root = None

  def CayCon(self, root1, root2):
    # Trường hợp cơ bản: nếu cây con là None, nó luôn là cây con của cây gốc
    if root2 is None:
      return True

    # Trường hợp cơ bản: nếu cây gốc là None, cây con không thể là cây con của nó
    if root1 is None:
      return False

    # Kiểm tra xem cây2 có là cây con của cây con bên trái hoặc bên phải của nút cây gốc ko
    return (self.CayCon(root1.Left, root2) or self.CayCon(root1.Right, root2) or 
            (root1.Info == root2.Info and self.CayCon(root1.Left, root2.Left) and 
             self.CayCon(root1.Right, root2.Right)))

# Test
cay1 = Cay()
cay1.Root = Node(1)
cay1.Root.Left = Node(2)
cay1.Root.Right = Node(3)
cay1.Root.Left.Left = Node(4)
cay1.Root.Right.Right = Node(5)

cay2 = Cay()
cay2.Root = Node(2)
cay2.Root.Left = Node(4)

if cay1.CayCon(cay1.Root, cay2.Root):
  print("Cay 2 la cay con cua cay 1")
else:
  print("Cay 2 khong la cay con cua cay 1")
