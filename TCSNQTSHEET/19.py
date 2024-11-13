class Solution:
    def replacByRank(self, arr):
        # Create a sorted list of unique elements
        sorted_unique = sorted(set(arr))
        
        # Create a dictionary to map each element to its rank
        rank_map = {value: rank + 1 for rank, value in enumerate(sorted_unique)}
        
        # Replace elements in the original array with their ranks
        ranked_arr = [rank_map[value] for value in arr]
        
        return ranked_arr
   
    
def main():
    
    T=int(input("Enter the test case").strip())
    
    while T>0:
        
        arr=[int (x) for x in input("Enter the elements of the array").strip().split()]
        ob=Solution()
        res=ob.replacByRank(arr)
        print(res)
        T=T-1
        
        
if __name__ =="__main__":
    main()