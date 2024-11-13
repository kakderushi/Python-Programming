class Solution:
    def findFloor(self,A,N,X):
        low, high=0,N-1
        floor_index=-1
        
        while low <=high:
            mid=(low+high)//2
            
            if A[mid]==X:
                return mid
                
            elif A[mid] <X:
                floor_index=mid
                low=mid+1 
            else:
                high=mid-1
                
        return floor_index

import math

def main():
    t=int(input())
    while t>0:
        nx=[int (x) for x in input().strip().split()]
        n=nx[0]
        x=nx[1]
        
        A=[int (x) for x in input().strip().split()]
        obj=Solution()
        print(obj.findFloor(A,n,x))
        t=t-1