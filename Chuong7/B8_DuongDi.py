class Graph:
  def __init__(self):
      self.graph = {}

  def add_edge(self, u, v):
      self.graph.setdefault(u, []).append(v)

  def is_reachable(self, v1, v2):
      visited = set()

      def dfs(node):
          if node == v2:
              return True
          visited.add(node)
          for neighbor in self.graph.get(node, []):
              if neighbor not in visited:
                  if dfs(neighbor):
                      return True
          return False

      return dfs(v1)

# Test
g = Graph()
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(1, 4)

print("Có đường đi từ 1 đến 3:", g.is_reachable(1, 3))  # Kết quả: True
print("Có đường đi từ 4 đến 2:", g.is_reachable(4, 2))  # Kết quả: False
print("Có đường đi từ 2 đến 5:", g.is_reachable(2, 5))  # Kết quả: False
