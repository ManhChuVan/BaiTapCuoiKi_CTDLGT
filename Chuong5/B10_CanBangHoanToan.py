class Node:
  def __init__(self, data):
      self.Info = data
      self.Left = None
      self.Right = None

class Cay:
  def __init__(self):
      self.Root = None

  def CanBangHoanToan(self):
      def dem_nut(node):
          if node is None:
              return 0
          return 1 + dem_nut(node.Left) + dem_nut(node.Right)

      def kiem_tra_can_bang(node):
          if node is None:
              return True

          # Đệ qui kiểm tra số lượng nút của cây con bên trái và bên phải
          left_count = dem_nut(node.Left)
          right_count = dem_nut(node.Right)
          print("left_count:" , left_count)
          print("right_count:" , right_count)
  
          # Kiểm tra xem chênh lệch số lượng nút có lớn hơn 1 không
          if abs(left_count - right_count) > 1:
              return False

          # Đệ qui kiểm tra từng nút của cây
          return kiem_tra_can_bang(node.Left) and kiem_tra_can_bang(node.Right)

      return kiem_tra_can_bang(self.Root)

# Test
cay = Cay()
cay.Root = Node(1)
cay.Root.Left = Node(2)
cay.Root.Right = Node(3)
cay.Root.Left.Left = Node(4)
cay.Root.Left.Right = Node(4)
cay.Root.Left.Left.Left = Node(5)
# cay.Root.Left.Left.Right = Node(4)

cay.Root.Right.Right = Node(5)
cay.Root.Right.Right.Left = Node(6)
cay.Root.Right.Left = Node(7)


if cay.CanBangHoanToan():
  print("Cay la mot cay can bang hoan toan")
else:
  print("Cay khong phai la mot cay can bang hoan toan")
