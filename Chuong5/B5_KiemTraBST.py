class Node:
  def __init__(self, data):
      self.Info = data
      self.Left = None
      self.Right = None

class Cay:
  def __init__(self):
      self.Root = None

  def isBSTUtil(self, node, min_val, max_val):
      # Trường hợp cơ bản: nút là None
      if node is None:
          return True

      # Kiểm tra xem giá trị của nút có nằm trong khoảng cho phép không
      if node.Info < min_val or node.Info > max_val:
          return False

      # Kiểm tra các cây con bên trái và bên phải của nút hiện tại
      return (self.isBSTUtil(node.Left, min_val, node.Info - 1) and
              self.isBSTUtil(node.Right, node.Info + 1, max_val))

  def KiemTraBST(self):
      return self.isBSTUtil(self.Root, float("-inf"), float("inf"))

# Test
cay = Cay()
cay.Root = Node(4)
cay.Root.Left = Node(2)
cay.Root.Right = Node(5)
cay.Root.Left.Left = Node(1)
cay.Root.Left.Right = Node(3)

if cay.KiemTraBST():
  print("Cay la mot cay BST")
else:
  print("Cay khong phai la mot cay BST")
