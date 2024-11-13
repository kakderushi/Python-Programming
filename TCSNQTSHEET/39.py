class Solution:
    def countZeros(self,arr,n):
        cnt=0
        row=0
        col=n-1
        
        while row <n and col>=0:
            if arr[row][col]==0:
                cnt+=(col+1)
                row+=1
                
            else:
                col-=1
                
        return cnt
        
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        
        arr=list(map(int,input().strip().split()))
        matrix=[[0 for i in range (n)] for j in range(n)]
        k=0
        for i in range(n):
            for j in range(n):
                matrix[i][j]=arr[k]
                k+=1
        ob=Solution()
        print(ob.countZeros(matrix, n))