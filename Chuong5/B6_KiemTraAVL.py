class Node:
  def __init__(self, data):
      self.Info = data
      self.Left = None
      self.Right = None

class Cay:
  def __init__(self):
      self.Root = None

  def ChieuCao(self, node):
      if node is None:
          return 0
      return max(self.ChieuCao(node.Left), self.ChieuCao(node.Right)) + 1

  def KiemTraAVL(self, root):
      if root is None:
          return True

      # Kiểm tra chênh lệch chiều cao của cây con bên trái và bên phải của nút hiện tại
      left_height = self.ChieuCao(root.Left)
      right_height = self.ChieuCao(root.Right)
      if abs(left_height - right_height) > 1:
          return False

      # Đệ qui kiểm tra cho cây con bên trái và cây con bên phải
      return self.KiemTraAVL(root.Left) and self.KiemTraAVL(root.Right)

# Test
cay = Cay()
cay.Root = Node(1)
cay.Root.Left = Node(2)
cay.Root.Right = Node(3)
cay.Root.Left.Left = Node(4)
cay.Root.Right.Right = Node(5)
cay.Root.Right.Right.Right = Node(6)
# cay.Root.Right.Right.Right.Left = Node(7)


if cay.KiemTraAVL(cay.Root):
  print("Cay la mot cay AVL")
else:
  print("Cay khong phai la mot cay AVL")
