# find all symmetric pairs in the array
class Solution:
    def find_symmetric_pairs(self,pairs):
        #Dictonary to store pairs
        pari_dict={}
        #list to store symmetric paris
        symmetirc_pairs=[]
        
        #iterate over each pair
        for (a,b) in pairs:
            if(b,a) in pari_dict:
                symmetirc_pairs.append(a,b)
            else:
                pari_dict[(a,b)]=True
            
        return symmetirc_pairs
        


def main():
    T=int(input("Enter the test cases"))
    while T>0:
        
        pair_input = input("Enter pairs in the format (x,y),(a,b),...: ")
    
    # Removing spaces, then splitting the input by '),' to isolate each pair
        pair_input = pair_input.replace(' ', '').strip()
        pairs = []

        for pair in pair_input.split('),'):
        # Removing any remaining parentheses and splitting by comma
            a, b = map(int, pair.strip('()').split(','))
            pairs.append((a, b))
            
            
        T=T-1
# Run the main method
if __name__ =="__main__":
    main()