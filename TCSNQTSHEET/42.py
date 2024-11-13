class Solution:
    def countTriplets(self, arr, n, sum):
        # Sort the array
        arr.sort()
        cnt = 0
        for i in range(n-2):
            left = i + 1
            right = n - 1
            while left < right:
                curr_sum = arr[i] + arr[left] + arr[right]
                
                if curr_sum >= sum:
                    right -= 1
                else:
                    # All triplets between left and right are valid
                    cnt += (right - left)
                    left += 1
        return cnt

# Input reading and processing
t = int(input())
for _ in range(t):
    l = list(map(int, input().split()))
    n = l[0]
    k = l[1]
    arr = list(map(int, input().split()))
    ob = Solution()
    ans = ob.countTriplets(arr, n, k)
    print(ans)
