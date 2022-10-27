

def sumOfN(N):
    N = abs(N)
    return (N*N+N) // 2


def Day7(mylist):
   
    '''
    min_fuel = float('inf')

    #ar = numpy.array(mylist)
    #print(numpy.mean(ar))
    
    #PartOne
    for i in range(len(mylist)):
        cost = 0
        for j in range(0,len(mylist)):
            step = abs(mylist[i]-mylist[j])
            #print(cost)
        
        if cost < min_fuel:
            min_fuel = cost

    print(min_fuel)
    
    #PartTwo
    '''
    x = min(mylist)
    y = max(mylist)
    scores = []
    #print(x,y)
    for i in range(x,y+1):
        val = sum(sumOfN(i-j) for j in mylist)
        scores.append(val)
    print(min(scores))


if __name__=="__main__":
    mylist = []
    
    with open('input','r') as f:
        for line in f:
            mylist+=list(map(int,line.rstrip().split(',')))
    
    Day7(mylist)
