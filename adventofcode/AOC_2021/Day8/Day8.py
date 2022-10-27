def Day8(mylist):
    count = 0
    myset = (2,4,3,7)
    #distinct length wale are 1:2,4:4,7:3,8:7
    
    for pattern in mylist:
       if len(pattern) in myset:
            count+=1

    


    print(count)

if __name__=="__main__":
    mylist = []
    with open('input','r') as f:
        for line in f:
            f,s = line.split('|')
            mylist.append((f.rstrip(),s.rstrip()))
            break
    print(mylist)
    #Day8(mylist)













