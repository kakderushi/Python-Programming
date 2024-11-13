# split array in three equal sum subarrays
'''
Given an array arr[], determine if arr can be split into three consecutive parts such that the sum of each part is equal. If yes return any index pair(i, j) in an array such that sum(arr[0..i]) = sum(arr[i+1..j]) = sum(arr[j+1..n-1]), otherwise return an array {-1,-1}.

Note: Driver code will print true if arr can be split into three equal sum subarrays, otherwise, it is false.

Examples :

Input:  arr[] = [1, 3, 4, 0, 4]
Output: true
Explanation: [1, 2] is valid pair as sum of subarray arr[0..1] is equal to sum of subarray arr[2..3] and also to sum of subarray arr[4..4]. The sum is 4. 
Input: arr[] = [2, 3, 4]
Output: false
Explanation: No three subarrays exist which have equal sum.
'''
class Solution:
    def findSplit(self,arr):
        pass
    
if __name__ =="__main__":
    t=int(input())
    while t:
        t-=1
        arr=[int(x) for x in input().split().strip()]
        ob=Solution()
        res=ob.findSplit(arr)
        if res==[-1,-1]:
            print("false")
        else:
            print('true')
        print('~')
            