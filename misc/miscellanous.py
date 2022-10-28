#permutations and combinations of a given string

'''
from itertools import combinations,combinations_with_replacement,permutations

#combs = [c for c in combinations_with_replacement(list(range(1,9)),3)]
#print(combs)

#perms = [p for p in permutations('ABC')]
#print(perms)


#Find out permutations of string 'ABC'

def permute(data,i,length):
    if i==length:
        print(''.join(data))
    else:

        for j in range(i,length):
            data[i], data[j] = data[j], data[i]  #backtrack
            permute(data,i+1,length)
            data[i], data[j] = data[j], data[i]


if __name__ == "__main__":
   data = "ABC"
   n = len(data)
   permute(list(data),0,n)

def isSafe(matrix,x,y):

    if x>=0 and x<len(matrix) and y>=0 and y<len(matrix[0]) and matrix[x][y] == '.':
        return True
    else:
        return False


def solve(matrix):

    sol = [[0 for j in range(len(matrix[0]))] for i in range(len(matrix))]
    

    if solution(matrix,0,0,sol) == False:
        print("Solution Dosent exists")

    
    countone = 0
    for i in range(len(sol)):
        countone+=sol[i].count(1)

    print((countone-1)*5)

def solution(matrix,x,y,sol):
    #if x,y is goal,return True
    if x==len(matrix)-1 and y==len(matrix[0])-1 and matrix[x][y]=='.':
        sol[x][y] = 1 
        return True


    if isSafe(matrix,x,y)==True:

        sol[x][y] = 1

        #count = 0
        #move forward in x direction
        if solution(matrix,x+1,y,sol) == True:
            return True
          
        #move downward in y direction
        if solution(matrix,x,y+1,sol) == True:
            return True
        

        #if none of movements work,backtrack
        sol[x][y] = 0
        return False


if __name__=="__main__":
    mylist = ['..##','#.##','#...']

    matrix = []

    for i in range(len(mylist)):
        result = []
        for j in range(len(mylist[0])):
            result.append(mylist[i][j])

        matrix.append(result)

    solve(matrix)
    #solution(matrix,x,y)

from collections import Counter

string = input("Enter your string")

freq = Counter(string)

#print(freq)
sorted_freq = {k:v for k,v in sorted(freq.items(),key=lambda v:v[1],reverse=True)}
#sorted(freq.items(),key=lambda v:v[1],reverse=True)
print(sorted_freq)


for key in sorted_freq.keys():
    #print(sorted_freq[i][0],end=" ")
    print(key,end="")


def solution(num):
    count = num

    while(num != 1):

        if(num%2 == 0):
            count+= num//2
            num = num//2 
        else:
            count += (num//2 + 1)
            num = num//2 + 1


if __name__ == "__main__":
    num = int(input("Enter the number of candles"))
    print(solution(num))

#generate all possible sublists or contiguous subarrays
def solution(nums):
    for w in range(1,len(nums)+1):
        for i in range(len(nums)-w+1):
            print(nums[i:w+i])

'''
from itertools import permutations

def isPrime(num):
    if num > 1:
        for i in range(2,int(num/2)+1):
            if(num%i) == 0:
                return False
                
        else:
            return True
    else:
        return False

def solution(nums):
    count = 0
    for i in range(len(str(nums))):
        unique = set()
        perms = [p for p in permutations(str(nums),i+1)]
        for j in range(len(perms)):
            unique.add(int(''.join(perms[j])))

        print(unique)

        for x in unique:
            if isPrime(x):
                count+=1
    return count


if __name__ == "__main__":
    numberValue = int(input())
    result = solution(numberValue)
    print(result)


