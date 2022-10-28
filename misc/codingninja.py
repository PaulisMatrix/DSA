import math

# Write your code here
def solution(a,num,mylist):
    b  = int("".join(map(str,mylist)))

    print(pow(a,b) % 1337)


if __name__=="__main__":
    a = int(input())
    num = int(input())
    mylist = list(map(int,input().strip().split()))
    
    solution(a,num,mylist)