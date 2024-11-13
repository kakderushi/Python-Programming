# Dijkstra's algo is used to find the shortest path between nodes in a graph
# especially  when the graph has non negative edge weights

# start with the source node and assign it a tentaive distance of 0
#assign all other nodes a tentative distance of infinity
#explore all neighbours of the current node and update their tentative distance
#select the node with the smallest tentative distance and repeat the proceses until all nodes are processed
def dijkstra(graph,start):
    #number of vertices in the graph
    v=len(graph)
    
    
if __name__ == "__main__":
    # Graph representation: adjacency list
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }

    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)

    # Print shortest distances from start_node to all other nodes
    print(f"Shortest distances from {start_node}:")
    for node, distance in shortest_distances.items():
        print(f"Node {node}: {distance}")