class Solution:
    def getDigitDiff(self,arr,k):
        lst=[]
        for i in arr:
            if i< k:
                s=str(i)
                temp=True
                if len(s)>1:
                    for j in range(1,len(s)):
                        if( abs(int(s[j])-int[j-1]))==1 and temp=True:
                            temp=True
                        else:
                            temp=False
                        if temp:
                            lst.append(i)
        return lst
if __name__ =="__main__":
    t=int(input())
    while t>0:
        k=int(input())
        arr=list(map(int, input().split()))
        ob=Solution()
        ans=ob.getDigitDiff(arr,k)
        print(ans)
        t-=1
        