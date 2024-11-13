class Solution:
    def repeatingElement(self,arr,n):
        if n==0 or n==1:
            return 
        
        temp=[]
        
        for i in range(n-1):
            for j in range(i+1,n):
                if arr[i]==arr[j]:
                    temp.append(arr[i])
        return temp



def main():
    T=int(input("Enter the test cases").strip())
    
    while T>0:
        
        # size of the aaray
        
        N=int(input("Enter the size of the array").strip())
        
        # read elements of the array
        
        array=[int(x) for x in input("Enter the elements of the array").strip().split()]
        
        ob=Solution()
        med=ob.repeatingElement(array,N)
        print(med)
        T=T-1
        
        
        
        
if __name__ =="__main__":
    main()
        