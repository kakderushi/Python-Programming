class CountComponents:
    def build_graph(n,edges):
        graph=[]
        for i in range(n):
            graph.append(list())
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        return graph
    
    def solve(self,node,graph,visited):
        visited[node]=True
        for nbr in graph[node]:
            if not visited[nbr]:
                self.solve(nbr,graph,visited)
            
    def countComponents(self,n,edges):
        graph=self.build_graph(edges,n)
        visited=[False]*n
        cnt=0
        for src in range(n):
            if visited[src] is not True:
                self.solve(src,graph,visited)
                cnt+=1
        return cnt


if __name__ == "__main__":
    edges = [[0, 1], [0, 2], [1, 2], [1, 3], [1, 4], [2, 5], [3, 4], [3, 5], [6, 7], [7, 8],[12,14]]
    n = 9
    obj=CountComponents()
    cnt=obj.countComponents(edges,n)
    print(cnt)
    
    
    