
def Day6(mylist):
    #iterate for 80 days
    
    '''
    PartOne
    days = 80
    while days:
        #first check, if 0 reset 6 and add 8
        for i in range(len(mylist)):
            if mylist[i]==0:
                mylist[i] = 6
                mylist.append(8)
            else:
                mylist[i]-=1
        days-=1
    print(len(mylist))
    
    '''
    lanternfish_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for i in mylist:
        lanternfish_dict[i]+=1

    print(lanternfish_dict)

    for _ in range(256):
        new_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for key in lanternfish_dict.keys():
            new_dict[key-1] = lanternfish_dict[key]
        
        for key in new_dict.keys():
            if key == -1:
                new_dict[8]=new_dict[-1]
                new_dict[6]+=new_dict[-1]
        lanternfish_dict = new_dict
        del lanternfish_dict[-1]
    
    print(sum(lanternfish_dict.values()))

if __name__=="__main__":
    mylist = []
    with open('input','r') as f:
        for line in f:
            mylist+=list(map(int,line.rstrip().split(',')))
    Day6(mylist)

