
# print the sum of elements which consists of multiplication


class Solution:
    def mulWithAdd(self,n):
        res=n*(n+1)//2
        
        return res*10
    


def main():
    t=int(input("Enter the test case"))
    
    while t>0:
        n=int(input("Enter the number "))
        ob=Solution()
        res=ob.mulWithAdd(n)
        print(res)
        t=t-1

if __name__ =="__main__":
    main()