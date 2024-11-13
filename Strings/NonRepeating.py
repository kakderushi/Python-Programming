class Solution:
    def nonRepeatingChar(self,s):
        charSpace=[0]*26
        for i in s:
            charSpace[ord(s[i]-97)]+=1
            
        for i in s:
            if charSpace[ord(i)-97]==1:
                return i
        return '$'
    
    
if __name__ =="__main__":
    t=int(input())
    for i in range(t):
        s=str(input())
        obj=Solution()
        ans=obj.nonRepeatingChar(s)
        if ans!='$':
            print(ans)
        else:
            print(-1)
        print("~")
        
'''

apporach:

creating an array of characters
then make count of each characters
then check whatever we want to check form this array regarding it make some changes on array
'''
         
    