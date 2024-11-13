'''
Given an array arr of integers which may or may not contain duplicate elements. Your task is to remove duplicate elements.

Examples:

Input: arr[] = [1, 2, 3, 1, 4, 2]
Output: [1, 2, 3, 4]
Explanation: 2 and 1 have more than 1 occurence.
'''


class Solution:
    def removeDuplicate(self, arr):
        arr2=[]
        s=set()
        for i in arr:
            if i not in s:
                s.add(i)
                arr2.append(i)
        return arr2
    
if __name__ == "__main__":
    t=int(input())
    while t>0:
        arr=list(map(int, input().split()))
        ob=Solution()
        ans=ob.removeDuplicates(arr)
        print(*ans)
        t-=1
        