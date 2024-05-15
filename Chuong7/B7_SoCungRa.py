class DirectedGraph:
  def __init__(self):
      self.graph = {}

  def add_edge(self, u, v):
      self.graph.setdefault(u, []).append(v)

  def out_degree_of_vertex(self, v):
      if v not in self.graph:
          return 0
      return len(self.graph[v])

# Test
dg = DirectedGraph()
dg.add_edge(1, 2)
dg.add_edge(2, 3)
dg.add_edge(2, 4)
dg.add_edge(3, 4)
dg.add_edge(4, 1)

print("Số cung ra của đỉnh 1 là:", dg.out_degree_of_vertex(1))  # Kết quả: 1
print("Số cung ra của đỉnh 2 là:", dg.out_degree_of_vertex(2))  # Kết quả: 2
print("Số cung ra của đỉnh 3 là:", dg.out_degree_of_vertex(3))  # Kết quả: 1
print("Số cung ra của đỉnh 4 là:", dg.out_degree_of_vertex(4))  # Kết quả: 1
