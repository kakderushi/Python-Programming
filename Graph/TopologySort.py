
def topologicalSortUtil(v,adj,visited,stack):
    visited[v]=True
    #recur for all adjacent vertices
    for i in adj[v]:
        if not visited[i]:
            topologicalSortUtil(i,adj,visited,stack)
        #push current vertex to stack which stores the result 
        stack.append(v)
def topologicalSort(adj,v):
    stack=[]
    visited=[False]*v
    
    for i in range(v):
        if not visited[i]:
            topologicalSortUtil(i,adj,visited,stack)
    print("topological sorting of the graph",end=" ")
    while stack:
        print(stack.pop(),end=" ")
        


if __name__ =="__main__":
    v=4
    edges=[[0,1],[1,2],[3,1],[3,2]]
    adj = [[] for _ in range(V)]

    for i in edges:
        adj[i[0]].append(i[1])

    topologicalSort(adj, V)