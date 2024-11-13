class Solution:
    def areAnagrams(self,s1,s2):
        if len(s1)!=len(s2):
            return False
        
        countS1=[0]*26
        countS2=[0]*26
        
        for i in range(len(s1)):
            countS1[ord(s1[i])-ord('a')]+=1
            countS2[ord(s1[i])-ord('a')]+=1
            
        return countS1==countS2
# time complexity =0(n)
# space complexity =0(1)
    
    
if __name__ =="__main__":
    t=int(input())
    for i in range(t):
        a=input().strip()
        b=input().strip()
        if Solution().areAnagrams(a,b):
            print('true')
        else:
            print("false")
        print("~")