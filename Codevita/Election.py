##Election outcome 

def election_result(voter_queue):
    a_supporters=0
    b_supporters=0
    for voter in voter_queue:
        if voter == 'A':
            a_supporters+=1
        elif voter=='B':
            b_supporters+=1
    if a_supporters > b_supporters:
        return 'A'
    elif b_supporters>a_supporters:
        return 'B'
    else:
        return 'coalition goverment'

n=int(input())
voter_queue=input().strip()
print(election_result(voter_queue))