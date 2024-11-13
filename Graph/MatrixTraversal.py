from collections import deque

def bfs(matrix, start_node):
    visited = [False] * len(matrix)
    queue = deque([start_node])
    visited[start_node] = True
    
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        
        for neighbor, isConnected in enumerate(matrix[node]):
            if isConnected and not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

# Example graph represented by a matrix (adjacency matrix)
graph = [
    [0, 1, 0, 0, 1],  # Node 0 is connected to node 1 and node 4
    [1, 0, 1, 0, 0],  # Node 1 is connected to node 0 and node 2
    [0, 1, 0, 1, 0],  # Node 2 is connected to node 1 and node 3
    [0, 0, 1, 0, 1],  # Node 3 is connected to node 2 and node 4
    [1, 0, 0, 1, 0]   # Node 4 is connected to node 0 and node 3
]

# Starting BFS from node 0
print("BFS Traversal starting from node 0:")
bfs(graph, 0)
