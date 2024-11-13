
def changeads(num):
    b=bin(num)
    b=b[2:len(b)]
    b1=""
    for bit in b:
        if bit =='1':
            b1=b1+'0' 
        else:
            b1=b1+'1'        
    sum1=0
    for i in range(len(b1)):
        sum1=sum1+(int(b1[i])*(2**(len(b1)-(i+1))))
    return sum1

print(changeads(50))