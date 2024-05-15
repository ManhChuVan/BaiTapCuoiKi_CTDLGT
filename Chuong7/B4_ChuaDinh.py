class Graph:
  def __init__(self):
      self.graph = {}

  def add_edge(self, u, v):
      if u not in self.graph:
          self.graph[u] = []
      self.graph[u].append(v)

  def contains_vertex(self, v):
      return v in self.graph

# Test
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)

print("Đỉnh 2 có tồn tại trong đồ thị:", g.contains_vertex(2))  # True
print("Đỉnh 4 có tồn tại trong đồ thị:", g.contains_vertex(4))  # False
