import numpy as np


def Day5(grid1,grid2):
    with open('input','r') as f:
        for line in f:
            first,second = line.split('->')
            x1,y1 = list(map(int,first.split(',')))
            x2,y2 = list(map(int,second.split(',')))
            x1,x2 = sorted((x1,x2))
            y1,y2 = sorted((y1,y2))
            if x1==x2 or y1==y2:
                grid1[x1:x2+1,y1:y2+1]+=1
                grid2[x1:x2+1,y1:y2+1]+=1
            else:
                if abs(x1-x2) == abs(y1-y2):
                    slope = abs(y2-y1)
                    for x in range(x1,x2+1):
                        pass
                    '''
                    ((x1, y1), (x2, y2)) = sorted(((x1, y1), (x2, y2)))
                    for i, x in enumerate(range(x1, x2+1)):
                        y = y1 + (y2 - y1) * i // abs(y2 - y1)
                        grid2[x, y] += 1    
                    '''

    print(np.count_nonzero(grid1 > 1))
    print(np.count_nonzero(grid2 > 1))
    

if __name__=="__main__":
    n = 1024
    grid1 = np.zeros((n,n))
    grid2 = np.zeros((n,n)) 
    Day5(grid1,grid2)