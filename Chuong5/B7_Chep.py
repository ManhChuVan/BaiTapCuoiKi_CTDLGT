class Node:
  def __init__(self, data):
      self.Info = data
      self.Left = None
      self.Right = None

class Cay:
  def __init__(self):
      self.Root = None

  def Chep(self, root):
      if root is None:
          return None

      # Tạo một nút mới với thông tin từ nút gốc
      new_node = Node(root.Info)

      # Đệ qui sao chép cây con bên trái và bên phải của nút gốc
      new_node.Left = self.Chep(root.Left)
      new_node.Right = self.Chep(root.Right)

      return new_node

# Test
cay = Cay()
cay.Root = Node(1)
cay.Root.Left = Node(2)
cay.Root.Right = Node(3)
cay.Root.Left.Left = Node(4)
cay.Root.Left.Right = Node(8)
cay.Root.Left.Right.Right = Node(10)
cay.Root.Right.Right = Node(5)
cay.Root.Right.Left = Node(9)


new_cay = Cay()
new_cay.Root = cay.Chep(cay.Root)

def in_order_traversal(root):
  if root:
      in_order_traversal(root.Left)
      print(root.Info, end=" ")
      in_order_traversal(root.Right)

print("Cay ban dau:")
in_order_traversal(cay.Root)
print("\nCay sau khi sao chep:")
in_order_traversal(new_cay.Root)
