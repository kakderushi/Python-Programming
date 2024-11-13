# 5 th october questions
# write a code you are given an interger return true if sum 
# of the digits is multiple of 3 else return false

def isSumMultipleOfThree(num):
    total_sum=0
    while num!=0:
        total_sum+=num%10
        num//10
    return total_sum%3==0

number=int(input("Enter an integer"))
if isSumMultipleOfThree(number):
    print("true")
else:
    print("false")


