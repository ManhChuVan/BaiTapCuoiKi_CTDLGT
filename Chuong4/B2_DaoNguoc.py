class Node:
  def __init__(self, data):
      self.Info = data
      self.Next = None

class DSLK:
  def __init__(self):
      self.Head = None

  def Them(self, data):
      new_node = Node(data)
      if self.Head is None:
          self.Head = new_node
      else:
          current_node = self.Head
          while current_node.Next is not None:
              current_node = current_node.Next
          current_node.Next = new_node

  def InDanhSach(self):
      if self.Head is None:
          return

      current_node = self.Head
      while current_node is not None:
          print(current_node.Info, end=" ")
          current_node = current_node.Next

  def DaoNguoc(self):
      if self.Head is None:
          print("Danh sach rong")
          return
      stack = []
      current_node = self.Head
      temp1 = current_node
      self.Head = current_node.Next
      current_node.Next = None
      current_node = self.Head

      while current_node is not None and current_node.Next.Next is not None:
          current_node = current_node.Next

      temp2 = current_node.Next
      current_node.Next = None

      stack.append(temp2)
      current_node = self.Head
      while current_node is not None:
          stack.append(current_node)
          current_node = current_node.Next
      stack.append(temp1)


      self.Head = stack[0]
      current_node = self.Head
      for item in stack:
          current_node.Next = item
          current_node = current_node.Next
      current_node.Next = None


#test
dslk = DSLK()
dslk.Them(1)
dslk.Them(2)
dslk.Them(3)
dslk.Them(4)
dslk.Them(5)


print("Danh sach ban dau: ")
dslk.InDanhSach()


dslk.DaoNguoc()
print("\nDao nguoc:")
dslk.InDanhSach()

#Dao nguoc tat ca dslk 

# class Node:
#   def __init__(self, data):
#       self.Info = data
#       self.Next = None

# class DSLK:
#   def __init__(self):
#       self.Head = None

#   def Them(self, data):
#       new_node = Node(data)
#       if self.Head is None:
#           self.Head = new_node
#       else:
#           current = self.Head
#           while current.Next is not None:
#               current = current.Next
#           current.Next = new_node

#   def DaoNguoc(self):
#       if self.Head is None:
#           print("Danh sach rong")
#           return

#       stack = []
#       current = self.Head
#       while current is not None:
#           stack.append(current)
#           current = current.Next

#       self.Head = stack.pop()
#       current = self.Head
#       while stack:
#           current.Next = stack.pop()
#           current = current.Next
#       current.Next = None

#   def InDS(self):
#       if self.Head is None:
#           print("Danh sach rong")
#           return
#       current = self.Head
#       while current is not None:
#           print(current.Info, end=" ")
#           current = current.Next

# # Test
# dslk = DSLK()
# dslk.Them(1)
# dslk.Them(2)
# dslk.Them(3)
# dslk.Them(4)

# print("Danh sach truoc khi dao nguoc:")
# dslk.InDS()

# dslk.DaoNguoc()
# print("\nDanh sach sau khi dao nguoc:")
# dslk.InDS()