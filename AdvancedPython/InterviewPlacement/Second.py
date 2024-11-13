'''
Write a python program to sort characters and numbers so that 
first alphabets and then numbers are printed

input: A7B1R3

output: ABR137
'''


str1=input("Enter the input")
alphabets=[]
numbers=[]

for ch in str1:
    if ch.isalpha():
        alphabets.append(ch)
    else:
        numbers.append(ch)

finalList=(sorted(alphabets)+sorted(numbers))
output="".join(finalList)
print(output)