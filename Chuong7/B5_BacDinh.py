class Graph:
  def __init__(self):
      self.graph = {}

  def add_edge(self, u, v):
      self.graph.setdefault(u, []).append(v)
      self.graph.setdefault(v, []).append(u)

  def degree_of_vertex(self, v):
      if v in self.graph:
          return len(self.graph[v])
      return 0

# Test
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("Bậc của đỉnh 2 là:", g.degree_of_vertex(2))  # Kết quả: 3
print("Bậc của đỉnh 3 là:", g.degree_of_vertex(3))  # Kết quả: 1
print("Bậc của đỉnh 4 là:", g.degree_of_vertex(4))  # Kết quả: 0 (đỉnh không tồn tại)
