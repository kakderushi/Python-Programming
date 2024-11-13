class Solution:
    # insert at the beginning
    def insert_beginning(self,arr,element):
        arr.insert(0,element)
        return arr
    
    #insert at the end
    def insert_end(self,arr,element):
        arr.append(element)
        return arr
    
    # insert at the specific position
    def insert_at(self,arr,element,pos):
        if pos<0 or pos>len(arr):
            return arr
        arr.insert_at(pos,element)
        return arr
         
    
def main():
    T=int(input("Enter the test casese").strip())
    while T>0:
        #Taking input for the array size and elements 
        N=int(input("Enter the number of elements in the array"))
        array=[int (x) for x in input("Enter the elements of the array").strip().split()]
        
        ob=Solution()
        
        # insert the beginning of the array
        element=int(input("Enter the elements to insert at the beginning").strip())
        res1=ob.insert_beginning(array,element)
        print(res1)
        
        # insert at the end of the array
        element=int(input("Enter the end of array").strip())
        res2=ob.insert_end(array,element)
        print(res2)
        
        #insert at the specific location
        element=int(input("Enter the elements at the specific location"))
        pos=int(input("Enter the position"))
        res3=ob.insert_at(array,element,pos)
        print(res3)
        
        T=T-1
        
    
if __name__ =="__main__":
    main()