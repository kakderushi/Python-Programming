from enum import Enum

class Color(Enum):
    white=0
    gray=1
    black=2
    
class Solution:
    def buildGraph(self, edges, n):
        graph = [[] for _ in range(n)]

        for edge in edges:
            graph[edge[0]].append(edge[1])

        return graph  
    def dfs(self,node,dest,graph,state):
        if state[node]!=Color.white:
            return state[node]==Color.black
        if not graph[node]:
            return node==dest
        state[node]=Color.gray
        
        for nbr in graph[node]:
            if not self.dfs(nbr,dest,graph,state):
                return False
            
            state[node]=Color.black
            return False
        
    def leadsToDestination(self,n,edges,source,destination):
        graph=self.buildGraph(edges,n)
        state=[Color.white]*n
        return self.dfs(source,destination,graph,state)
    