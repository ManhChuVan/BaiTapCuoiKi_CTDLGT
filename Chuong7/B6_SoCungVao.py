class DirectedGraph:
  def __init__(self):
      self.graph = {}

  def add_edge(self, u, v):
      self.graph.setdefault(u, []).append(v)

  def in_degree_of_vertex(self, v):
      in_degree = 0
      for vertices in self.graph.values():
          if v in vertices:
              in_degree += 1
      return in_degree

# Test
dg = DirectedGraph()
dg.add_edge(1, 2)
dg.add_edge(2, 3)
dg.add_edge(2, 4)
dg.add_edge(3, 4)
dg.add_edge(4, 1)

print("Số cung vào của đỉnh 1 là:", dg.in_degree_of_vertex(1))  # Kết quả: 1
print("Số cung vào của đỉnh 2 là:", dg.in_degree_of_vertex(2))  # Kết quả: 1
print("Số cung vào của đỉnh 3 là:", dg.in_degree_of_vertex(3))  # Kết quả: 1
print("Số cung vào của đỉnh 4 là:", dg.in_degree_of_vertex(4))  # Kết quả: 2
