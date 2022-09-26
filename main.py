class Node:
    def __init__(self, id):
        self.id = id
        self.neighbours = []

class Graph:
    def __init__(self):
        self.nodes = None


    def load(self):
        print("Please input graph data:")
        n, p = map(int, input().split(' '))
        self.nodes=[None]*n
        for i in range(n):
            self.nodes[i] = Node(i)

        for i in range(p):
            start, end = map(int, input().split(' '))
            self.nodes[start].neighbours.append(end)
            self.nodes[end].neighbours.append(start)

    def is_connected_bfs(self, node1, node2):
        if node1 == node2:
            return True
        current = [node1]
        next = []
        visited = [False] * len(self.nodes)
        visited[node1] = True

        while current:
            for node in current:
                neighbours = self.get_neighbours(node)
                for neighbour in neighbours:
                    if neighbour == node2:
                        return True
                    if not visited[neighbour]:
                        next.append(neighbour)
                        visited[neighbour] = True
            current = next
            next = []
        return False

    def get_neighbours(self, node):
        return self.nodes[node].neighbours


    def is_connected_dfs(self,node1, node2):
        visited = [False] * len(self.nodes)
        return self.is_connected_dfs_recursive(node1, node2, visited)

    def is_connected_dfs_recursive(self, node1, node2, visited):
        if node1 == node2:
            return True
        visited[node1] = True
        neighbours = self.get_neighbours(node1)
        for neighbour in neighbours:
            if visited[neighbour]:
                continue
            if self.is_connected_dfs_recursive(neighbour, node2, visited):
                return True
        return False


g = Graph()
g.load()
print("Please input node1 node2:")
node1, node2 = map(int, input().split(' '))
if g.is_connected_bfs(node1, node2):
    print("%d and %d are connected" % (node1, node2))
else:
    print("%d and %d are not connected" % (node1, node2))

if g.is_connected_dfs(node1, node2):
    print("%d and %d are connected" % (node1, node2))
else:
    print("%d and %d are not connected" % (node1, node2))

