'''
Write a program to display the words that 
are repeated more than or equal to N times in the
text

input:

first input is a string

second input is integer (count ) representing value of number of times words occur in the text


output:
list of words
text is case sentive 
'''
string=input().split()
N=int(input())

cnt=dict()
for word in string:
    if word in cnt:
        cnt[word]+=1
    else:
        cnt[word]=1
word=[]      
for key in cnt:
    if cnt[key]>=N:
        word.append(key)
        
if len(word)>0:
    print(word)
else:
    print("NA")

        
 
