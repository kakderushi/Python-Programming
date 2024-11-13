#Rearrange the element
class Solution:
    def rearrange(self,arr,n):
        #create two list to storing elements pos and neg
        pos=[]
        neg=[]
        
        for i in range(n):
            if arr[i]<0:
                neg.append(arr[i])
            else:
                pos.append(arr[[i]])
                
        #Iteration on each elements 
        i ,j,k=0
        
        while i<len(neg) and j< len(pos):
            arr[k]=pos[j]
            j+=1
            k+=1
            arr[k]=neg[i]
            i+=1
            k+=1
            
        #Here we storing remaning positive elements
        while j< len(pos):
            arr[k]=pos[j]
            j+=1
            k+=1
            
        while i<len(neg):
            arr[k]=neg[i]
            i+=1
            k+=1
            

if __name__ =="__mani__":
    tc=int(input())
    while tc>0:
        n=int(input())
        arr=list(map(int,input().strip().split()))
        ob=Solution()
        ob.rearrange(arr,n)
        for x in arr:
            print(x,end=" ")
        print()
        tc=tc-1