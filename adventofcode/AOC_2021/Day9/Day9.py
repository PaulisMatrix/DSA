def Day9(mylist):
    result = []
    for i in range(len(mylist)-1):
        l = len(mylist[i])
        #if its the first line, i-1 is not present
        if i==0:
            for j in range(l):
                #left j-1
                if j==0:
                    #down,right
                    if mylist[i][j] < mylist[i+1][j] and mylist[i][j] < mylist[i][j+1]:
                        result.append(mylist[i][j])
                elif j==l-1:
                    #left down
                    if mylist[i][j] < mylist[i][j-1] and mylist[i][j] < mylist[i+1][j]:
                        result.append(mylist[i][j])
                    #left,down,right
                else:
                    if mylist[i][j] < mylist[i][j-1] and mylist[i][j] < mylist[i+1][j] and mylist[i][j] < mylist[i][j+1]:
                        result.append(mylist[i][j])
        else:
            for j in range(l):
                #left j-1
                if j==0:
                    #down,right,up
                    if mylist[i][j] < mylist[i+1][j] and mylist[i][j] < mylist[i][j+1] and mylist[i][j] < mylist[i-1][j]:
                        result.append(mylist[i][j])
                    
                elif j==l-1:
                    #left, up ,down
                    if mylist[i][j] < mylist[i][j-1] and mylist[i][j] < mylist[i+1][j] and mylist[i][j] < mylist[i-1][j]:
                        result.append(mylist[i][j])

                    #left,down,right,up
                else:
                    if mylist[i][j] < mylist[i][j-1] and mylist[i][j] < mylist[i+1][j] and mylist[i][j] < mylist[i][j+1] and mylist[i][j] < mylist[i-1][j]:
                        result.append(mylist[i][j])
    #process i+1
    #up,left
    s = len(mylist[i+1])
    for j in range(s):          
        #up,right
        if j==0:
            if mylist[i+1][j] < mylist[i][j] and mylist[i+1][j] < mylist[i+1][j+1]:
                result.append(mylist[i+1][j])
        elif j==s-1:
            #left,up
            if mylist[i+1][j] < mylist[i+1][j-1] and mylist[i+1][j] < mylist[i][j]:
                result.append(mylist[i+1][j])

        else:
            #up,left,right
            if mylist[i+1][j] < mylist[i][j] and mylist[i+1][j] < mylist[i+1][j-1] and mylist[i+1][j] < mylist[i+1][j+1]:
                result.append(mylist[i+1][j])
        
    print(sum(result)+len(result))
if __name__=="__main__":
    mylist = [[2,1,9,9,9,4,3,2,1,0],
              [3,9,8,7,8,9,4,9,2,1],
              [9,8,5,6,7,8,9,8,9,2],
              [8,7,6,7,8,9,6,7,8,9],
              [9,8,9,9,9,6,5,6,7,8]]
    #Day9(mylist)
    test = []
    with open('input','r') as f:
        for line in f:
            temp = []
            s = str(line.rstrip())
            for i in range(len(s)):
                temp.append(int(s[i]))
            test.append(temp)

    Day9(test)
    #print(test)
    