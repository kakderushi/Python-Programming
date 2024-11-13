'''
A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

Example 1
Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 uni
'''

from typing import List

class Solution:
    def canCross(self, stones:List[int])->bool:
        destination=stones[-1]
        hashMap=dict()
        # initialize the hashmap with stone positions as keys and sets as values
        for stone in stones:
            hashMap[stone]=set()
        # The first stone has an initial jump of 1  
        hashMap[stones[0]].add(1)
        
        for i in range(len(stones)):
            curr_stone_position=stones[i]
            for jump in hashMap[curr_stone_position]:
                next_position=curr_stone_position+jump
                if next_position==destination:
                    return True
                if next_position in hashMap:
                    if jump -1 >0:
                        hashMap[next_position].add(jump-1)
                    hashMap[next_position].add(jump)
                    hashMap[next_position].add(jump+1)

        return False

def main():
    stones=[0,1,3,5,6,8,12,17]
    obj=Solution()
    result=obj.canCross(stones)
    print("Can cross",result)
if __name__ =="__main__":
    main()
    