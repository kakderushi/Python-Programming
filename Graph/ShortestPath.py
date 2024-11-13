from collections import deque

#function to find the shortest path using bfs
def bfs_shortest_path(graph,start,end):
    #Queue to store node distance from start
    queue=deque([start,0])
    #set to keep track of visited nodes
    visited=set()
    #start bfs loop
    while queue:
        #get the current node and its distance form the queue
        node,distance=queue.popleft()
        
        #if we reached the destination node return distance
        if node==end:
            return distance
        #mark the node visited 
        visited.add(node)
        
        #explore all the neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                #add neigbor to queue with updated distance
                queue.append((neighbor,distance+1))
                # mark neighbor as visited
                visited.add(neighbor)
    return -1
    
#Graph represented as an adjacency list
graph={
    0:[1,2],
    1:[0,2,3],
    2:[0,1,4],
    3:[1,4],
    4:[2,3,5],
    5:[4]
}
startNode=0
endNode=5
#find the shortest path from startNode and to endNode
shortestDistance=bfs_shortest_path(graph,startNode,endNode)
print("Shortest distance: ",shortestDistance)