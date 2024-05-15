class Node:
  def __init__(self, data):
      self.Info = data
      self.Left = None
      self.Right = None

class Cay:
  def __init__(self):
      self.Root = None

  def SoSanh(self, root1, root2):
      # Trường hợp cơ bản: cả hai cây đều là None, chúng giống nhau
      if root1 is None and root2 is None:
          return True

      # Kiểm tra xem cả hai cây đều không phải None
      if root1 is not None and root2 is not None:
          # So sánh giá trị của hai nút
          if root1.Info == root2.Info:
              # Đệ qui so sánh cây con bên trái và bên phải của từng cây
              return (self.SoSanh(root1.Left, root2.Left) and
                      self.SoSanh(root1.Right, root2.Right))

      # Trường hợp còn lại: một trong hai cây là None hoặc giá trị của hai nút khác nhau
      return False

# Test
cay1 = Cay()
cay1.Root = Node(1)
cay1.Root.Left = Node(2)
cay1.Root.Right = Node(3)
cay1.Root.Left.Left = Node(4)
cay1.Root.Right.Right = Node(5)

cay2 = Cay()
cay2.Root = Node(1)
cay2.Root.Left = Node(2)
cay2.Root.Right = Node(3)
cay2.Root.Left.Left = Node(4)
cay2.Root.Right.Right = Node(5)

if cay1.SoSanh(cay1.Root, cay2.Root):
  print("Hai cay giong nhau")
else:
  print("Hai cay khong giong nhau")
