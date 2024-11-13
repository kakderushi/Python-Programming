# Remove duplicate elements from sorted array
class Solution:
    
    def remove_duplicate(self,arr):
        if not arr:
            return 
        #pointer for the position of the next unique element
        i=0 
        for j in range(1,len(arr)):
            if arr[j]!=arr[i]:
                i=i+1
                arr[i]=arr[j]
            #The number of unique elements  
        return i+1
    
if __name__ =="__main__":
    import sys
    input=sys.stdin.read
    data=input().strip().split('\n')
    
    t=int(data[0])
    line=1
    
    solution=Solution()
    for _  in  range(t):
        if line<len(data):
            arr=list(map(int,data[line].split()))
            line=line+1
            ans=solution.remove_duplicate(arr)
            for i in range(ans):
                print(arr[i],end="")
            print()
        