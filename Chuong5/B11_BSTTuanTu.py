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

  def isSequentialBSTUtil(self, node, isLeft):
      # Trường hợp cơ bản: nút là None
      if node is None:
          return True

      # Nếu nút gốc có 2 nút con, trả về False
      if node.Left is not None and node.Right is not None:
          return False

      # Nếu nút con là bên trái, kiểm tra tất cả các nút con có phải là bên trái không
      if isLeft:
          if node.Left is not None:
              return self.isSequentialBSTUtil(node.Left, isLeft)
          elif node.Right is not None:
              return False
      # Nếu nút con là bên phải, kiểm tra tất cả các nút con có phải là bên phải không
      else:
          if node.Right is not None:
              return self.isSequentialBSTUtil(node.Right, isLeft)
          elif node.Left is not None:
              return False

      return True


  def KiemTraSequentialBST(self):
      if not self.KiemTraBST():
          return False

      if self.Root is None:
          return True

      # Nếu nút gốc có cả hai nút con, trả về False
      if self.Root.Left is not None and self.Root.Right is not None:
          return False

      # Kiểm tra nút con của nút gốc
      if self.Root.Left is not None:
          return self.isSequentialBSTUtil(self.Root.Left, True)
      elif self.Root.Right is not None:
          return self.isSequentialBSTUtil(self.Root.Right, False)

      return True


# Test
cay = Cay()
cay.Root = Node(7)
cay.Root.Left = Node(3)
# cay.Root.Right = Node(6)
# cay.Root.Right.Right = Node(5)
# cay.Root.Left.Right = Node(6)
cay.Root.Left.Left = Node(4)
# cay.Root.Left.Right.Left = Node(5)

if cay.KiemTraSequentialBST():
  print("Cây là một cây BST tuần tự")
else:
  print("Cây không phải là một cây BST tuần tự")
