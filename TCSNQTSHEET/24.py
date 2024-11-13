#Equlibrium point
class Solution:
    def equlibriumPoint(self,arr):
        #first test case
        if len(arr)==1:
            return 1
        
        total_sum=sum(arr)
        left_sum=0
        for i in range(len(arr)):
            #total sum is now right_sum for inde i
            total_sum=total_sum - arr[i]
            
            if left_sum==total_sum:
                return i+1
            
            left_sum=left_sum + arr[i]
            
        return -1
    
import math
def main():
    T=int(input())
    while T>0:
        arr=[int (x) for x in input().strip().split()]
        ob=Solution()
        print(ob.equlibriumPoint(arr))
        T=T-1
        
        
        
if __name__ =="__main__":
    main()