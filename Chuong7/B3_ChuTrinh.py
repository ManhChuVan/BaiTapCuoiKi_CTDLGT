class Graph:
  def __init__(self):
      self.graph = {}

  def add_edge(self, u, v):
      if u not in self.graph:
          self.graph[u] = []
      self.graph[u].append(v)

  def is_cyclic_util(self, v, visited, parent):
      visited.add(v)
      if v in self.graph:
          for neighbor in self.graph[v]:
              if neighbor not in visited:
                  if self.is_cyclic_util(neighbor, visited, v):
                      return True
              elif parent != neighbor:
                  return True
      return False

  def has_cycle(self):
      visited = set()
      for v in self.graph:
          if v not in visited:
              if self.is_cyclic_util(v, visited, None):
                  return True
      return False

# Test
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Có chu trình trong đồ thị:", g.has_cycle())  # True

g = Graph()
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
print("Có chu trình trong đồ thị:", g.has_cycle())  # False
