import atexit
import io
import sys
class Solution:
    def minimumPlatform(self,arr,dep):
        arr.sort()
        dep.sort()
        i,j,maxi,cnt=0,0,0,0
        while i <len(arr):
            if arr[i] <= dep[j]:
                cnt+=1
                i+=1
            else:
                j+=1
                cnt-=1
            maxi=max(maxi,cnt)
        return maxi
             
if __name__ == "__main__":
    # these are useful for taking  input from user
    arrival=list(map(int,input().strip().split()))
    departure=list(map(int,input().strip().split()))
    ob=Solution()
    print(ob.minimumPlatform(arrival,departure))
    