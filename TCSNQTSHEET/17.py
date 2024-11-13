# find all the numbers in the range

class Solution:
    def palindrome_range(self,min,maxVal):
        palindrome=[]
        
        for i in range(min,maxVal):
             # check if the number is a palindrome
            if str(i)==str(i)[::-1]:
                palindrome.append(i)
                
        return palindrome
               
            
    
def main():
    
    T =int(input("Enter the test case").strip())
    while T>0:
        min=int(input("Enter the minimum number").strip())
        maxVal=int(input("Enter the max number"))
        sol=Solution()
        res=sol.palindrome_range(min,maxVal)
        print(res)
        T=T-1
        
if __name__ =="__main__":
    main()
    