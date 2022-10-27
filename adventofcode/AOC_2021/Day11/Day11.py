
def Day11(mylist):
    print(mylist)
    pass







if __name__=="__main__":
    mylist = []
    with open('input','r') as f:
        for line in f:
            mylist.append(line.rstrip()) 
    Day11(mylist)
