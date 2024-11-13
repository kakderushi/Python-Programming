
class Solution:
    def median(self,arr,n):
        # sort the array
        arr.sort()
        if n%2!=0:
            mid1=n//2
            res=arr[mid1]
            
            return res
        else:
            mid2=n//2-1
            mid3=n//2
            median_value=(arr[mid2]+arr[mid3])/2.0
            
            return median_value


def main():
    T=int(input("Enter the test cases").strip())
    
    while T>0:
        
        # size of the aaray
        
        N=int(input("Enter the size of the array").strip())
        
        # read elements of the array
        
        array=[int(x) for x in input("Enter the elements of the array").strip().split()]
        
        ob=Solution()
        med=ob.median(array,N)
        print(med)
        T=T-1
        
        
        
        
if __name__ =="__main__":
    main()
        
        
    