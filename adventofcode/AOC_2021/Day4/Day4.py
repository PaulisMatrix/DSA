

from itertools import combinations
import math

def isPrime(num):
    if num<=1:
        return False
    
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True


def solution(s):
    res = 0
    n = len(s)
    for i in range(1,n+1):
        comb = combinations(s,i)
        for j in comb:
            num = int(''.join(j),2)
            if isPrime(num):
                #print(num)
                res = max(num,res)
    print(res)

if __name__=="__main__":
    solution('10101000110000')



def get_nums():
    nums = []
    with open('input','r') as f:
        for line in f:
            try:
                nums+=list((map(int,line.split(','))))
            except:
                break

    return nums

def partOne():
    pass





if __name__=="__main__":
    nums = []
    nums = get_nums()
    print(nums)
    partOne()













