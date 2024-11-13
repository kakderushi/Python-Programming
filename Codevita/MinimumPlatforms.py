# Minimum platforms of train

# number of trains N
# Each train's arrival and departure time

def find_platforms(arrivals,departures):
    arrivals.sort()
    departures.sort()
    platforms_needed=1
    res=1
    i,j=1,0
    while i< len(arrivals) and j< len(departures):
        if arrivals[i] <= departures[j]:
            platforms_needed+=1
            i+=1
        else:
            platforms_needed-=1
            j+=1
        result=max(result,platforms_needed)
    return result

n=int(input())
arrivals=list(map(int, input().split()))
departures=list(map(int,input().split()))
print(find_platforms(arrivals,departures))