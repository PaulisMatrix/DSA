
def partOne():
    gamma = 1
    epsilon = 1
    mydict = {}
    with open("input","r") as f:
        for line in f:
            bin_ = line.split()[0]
            #print(len(bin_))
            for idx,item in enumerate(bin_,1):
                #print(idx,item)
                if idx not in mydict:
                    mydict[idx] = [0,0]
                    #print(mydict)
                    if item == '0':
                        mydict[idx][0] = 1
                    else:
                        mydict[idx][1] = 1
                else:
                    if item == '0':
                        mydict[idx][0]+=1
                    else:
                        mydict[idx][1]+=1
    #print(mydict)
    
def get_lines():
    mylist=  []
    with open('input','r') as f:
        for line in f:
            lin = line.split()[0]
            mylist.append(lin)    
    return mylist


def partTwo(data,oxygen,i):

    if len(data) == 1:
        return int(data[0],2)

    count1 = 0
    count0 = 0

    for line in data:
        if line[i] == '1':
            count1+=1
        else:
            count0+=1
    
    if oxygen:
        temp = '1' if count1>=count0 else '0'
    else:
        temp = '0' if count0<=count1 else '1' 
    
    data = [x for x in data if x[i]==temp]

    return partTwo(data,oxygen,i+1)

if __name__ == "__main__":
    #partOne()
    mylist = []
    mylist = get_lines()
    o2 = partTwo(mylist,True,0)
    co2 = partTwo(mylist,False,0)
    print(o2*co2)



