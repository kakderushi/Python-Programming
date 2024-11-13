class Solution:
    
    def average(self,array,n):
        res=sum(array)//n
        
        return res 






def main():
    # test case
    T=int(input("Enter the number of test cases"))
    
    while T>0:
        # read N and K
        nd=[int (x) for x in input("Enter N size of the array").strip().split()]
        N=nd[0]
        
        #read array Examples
        
        array=[int(x) for x in input("Enter the elements of the array").strip().split()]
        
        ob=Solution()
        #calcualte the avg 
        avg=ob.average(array,N)
        
        #print the output
        print(avg)
        
    
        
        T=T-1
        
if __name__=="__main__":
    main()
        
        
    
    
    