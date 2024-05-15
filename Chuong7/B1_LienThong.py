class Graph:
  def __init__(self):
      self.graph = {}

  def add_edge(self, u, v):
      if u not in self.graph:
          self.graph[u] = []
      self.graph[u].append(v)
      if v not in self.graph:
          self.graph[v] = []
      self.graph[v].append(u)

  def is_connected(self):
      visited = set()

      def dfs(node):
          visited.add(node)
          if node in self.graph:
              for neighbor in self.graph[node]:
                  if neighbor not in visited:
                      dfs(neighbor)

      start_node = next(iter(self.graph.keys()))  # Lấy một đỉnh bất kỳ để bắt đầu DFS
      dfs(start_node)

      # Kiểm tra xem tất cả các đỉnh đã được duyệt qua
      return len(visited) == len(self.graph)

# Test
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(3, 4)
print("Đồ thị liên thông?" , g.is_connected())  # False

g.add_edge(2, 3)
print("Đồ thị liên thông?" , g.is_connected())  # True
