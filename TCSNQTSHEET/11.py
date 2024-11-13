# Remove duplicates values form the array
class Solution:
    def removeDuplicates(self,arr,n):
    # this is the test case 
        if n==0 or n==1:
            return 
    
        temp=[]

        for i in range(n-1):
            if arr[i]!=arr[i+1]:
                temp.append(arr[i])

    #add last item those who wont to addedd
        temp.append(arr[-1])

    # copy all the elements in original array
        for i in range(len(temp)):
            arr[i]=temp[i]

        return len(temp)
    
    
def main():
    # get input for test cases
    T=int(input("Enter the test cases").strip())
    while T>0:
        #for size of the array
        N=int(input("Enter the size of the array").strip())
        
        # for elements of the array
        array=[int(x) for x in input("Enter the elements inside the array").strip().split() ]
        
        ob=Solution()
        res=ob.removeDuplicates(array,N)
        print(res)
        T=T-1
        
        
if __name__ =="__main__":
    main()
