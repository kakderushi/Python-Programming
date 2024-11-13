
def isSubset(arr1,arr2,n,m):
    arr1.sort()
    arr2.sort()
    
    i,j=0,0
    n,m=len(arr1), len(arr2)
    
    while i< n and j<m:
        if arr1[i]<arr2[i]:
            i+=1
            
        elif arr1[i]==arr2[j]:
            i+=1
            j+=1
        else:
            return "No"
    if j==m:
        return 'Yes'
    else:
        return 'No'
        

def main():
    t=int(input())
    for _ in range(t):
        sz=[int (x) for x in input().strip().split()]
        n,m=sz[0],sz[1]
        
        a1=[int (x) for x in input().strip().split()]
        a2=[int (x) for x in input().strip().split()]
        print(isSubset(a1,a2,n,m))
        
        
        
if __name__ == '__main__':
    main()