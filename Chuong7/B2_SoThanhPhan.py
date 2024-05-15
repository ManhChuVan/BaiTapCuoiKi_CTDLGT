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

  def count_connected_components(self):
      visited = set()

      def dfs(node):
          visited.add(node)
          if node in self.graph:
              for neighbor in self.graph[node]:
                  if neighbor not in visited:
                      dfs(neighbor)

      num_components = 0
      for node in self.graph:
          if node not in visited:
              dfs(node)
              num_components += 1

      return num_components

# Test
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(3, 4)
print("Số thành phần liên thông:", g.count_connected_components())  # 2

g.add_edge(2, 3)
print("Số thành phần liên thông:", g.count_connected_components())  # 1
