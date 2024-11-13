class Solution:
    def merge(self, S1, S2):
        res = ''
        i = 0
        j = 0
        # merging both till one exhausts
        while i < len(S1) and j < len(S2):
            res += S1[i]
            res += S2[j]
            i+=1
            j+=1
        # merging the left over part of the larger string
        while i < len(S1):
            res += S1[i]
            i+=1
        while j < len(S2):
            res += S2[j]
            j+=1
        return res
        
if __name__ =="__main__":
    t=int(input())
    for _ in range(t):
        # This for in order to get input in string format then here we used str 
        s1,s2=map(str, input().strip().split())
        ob=Solution()
        print(ob.merge(s1,s2))
    