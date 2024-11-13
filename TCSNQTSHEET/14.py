
class Solution:
    def find_non_repeating_elements(self,arr,n):
        freq={}
        for num in arr:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
                
        non_rep=[num for num in freq if freq[num]==1]
        return non_rep
    
def main():
    T=int(input("Enter the test cases").strip())
    
    while T>0:
        
        # size of the aaray
        
        N=int(input("Enter the size of the array").strip())
        
        # read elements of the array
        
        array=[int(x) for x in input("Enter the elements of the array").strip().split()]
        
        ob=Solution()
        med=ob.find_non_repeating_elements(array,N)
        print(med)
        T=T-1
        
        
        
        
if __name__ =="__main__":
    main()
        