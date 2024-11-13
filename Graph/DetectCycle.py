def is_cyclic(v,adj):
    #mark all the vertices as not visisted
    visited=[False]*v
    #call the recursive helper function
    #to detect cycle in differnet dfs trees
    for u in range(v):
        if not visited[u]:
            if is_cyclicUtil(u,adj,visited,-1):
                return True
        return False
def is_cyclicUtil(v,adj,visited,parent):
    visited[v]=True
    for i in adj[v]:
        if not visited[i]:
            if is_cyclicUtil(i,adj,visited,v):
                return True
            elif i!=parent:
                return True
    return False
if __name__ =="__main__":
    v=3
    adj=[[] for _ in range(v)]
    adj[1].append(0)
    adj[0].append(1)
    adj[0].append(2)
    adj[2].append(0)
    adj[1].append(2)
    adj[2].append(1)

    print("Contains cycle" if is_cyclic(v, adj) else "No Cycle")
    