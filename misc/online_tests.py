from collections import defaultdict
'''
mylist = [1,2,3,4,4,5,3,6,2,1]

mydict = defaultdict(int)

for i in range(len(mylist)):
    if mydict[mylist[i]] == 0:
        mydict[mylist[i]]+=1
        print(mylist[i])

from itertools import combinations

mylist = [12, 3, 1, 2, -6, 5, -8, 6]
target = 0
result = []
for comb in combinations(mylist,3):
    if comb[0] + comb[1] + comb[2] == target:
        result.append(comb)
        
print(result)

sort = [1,4,5,2,1,4,5,3,6,4,4]

print(list((set(sort))))

num2words1 = {0:'Zero',1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',6:'Six',7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 
                11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 
                15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 
                19: 'Nineteen'}
                
num2words2 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']


def words(num):
    if 0<=num<=19:
        print(num2words1[num])
    elif 20<=num<=99:
        units = num%10
        tens = num//10
        print(tens,units)
        print(num2words2[tens-2]+"-"+num2words1[units] if units else num2words2[tens-2])
        
    elif 100<=num<=999:
        units = num%10
        num = num//10
        tens = num%10
        num = num//10
        hun = num%10
        print(hun,tens,units)
        print(num2words1[hun]+'HundredAnd'+num2words2[tens-2]+num2words1[units] if tens and units else num2words1[hun]+'Hundred' )
    elif 1000<=num<=9999:
        units = num%10
        num = num//10
        tens = num%10
        num = num//10
        hun = num%10
        num = num//10
        tho = num%10
        print(tho,hun,tens,units)
        print(num2words1[tho]+'Thousand'+num2words1[hun]+'HundredAnd'+num2words2[tens-2]+num2words1[units] if hun and tens and units else num2words1[tho]+'Thousand')
        
    else:
        print("Out of range")
            
        
words(112)


def countSetBits(n):
    count = 0

    while(n):
        n &= (n-1)
        count+=1

    print(count)

countSetBits(15)

#Sieve Of Eratosthenes 

def findPrimes(n):

    prime = [True for i in range(n+1)]
    p = 2

    while(p * p <= n):

        #check if prime
        if (prime[p] == True):
            for i in range(p*p,n+1,p):
                prime[i] = False
        p+=1

    total = 0
    for i in range(2,n+1):
        if prime[i]:
            if n % i == 0:
                total+=i
    print(total)

findPrimes(39)


def findTotal(n):

    temp = [0] * (n+1)

    for i in range(2,n+1):

        #check if prime
        if temp[i] == 0:
            #add this prime number to all its multiples
            for j in range(i,n+1,i):
                temp[j]+=i

    return temp[n]


print(findTotal(39))

string = "AjaY"
result = " "
for i in range(len(string)):
    #for lowercase to uppercase
    if string[i] in "abcdefghijklmnopqrstuvwxyz":
        result+=chr((ord(string[i])-32))
    else:
        result+=chr((ord(string[i])+32))

print(result)

#Profit maximization Apisero.

def solve(n,a):
    dp=[0]*n

    for i in range(0,n):
        sumvalue = 0
        for j in range(0,i):
            if(a[i]%a[j]==0):
                sumvalue = max(sumvalue,dp[j])
        dp[i] = sumvalue+a[i]

    return max(dp)


n = int(input())
p = list(map(int,input().split()))

print(solve(n,p))
'''

def solution(string):
    result,curr,num = [],None,1
    
    curr,num = string[0],1
    for i in range(1,len(string)):
        if curr!=string[i]:
            result.append((curr,num))
            curr,num = string[i],1
        else:
            num+=1
        
        if i==len(string)-1:
            result.append((curr,num))

    print(result)

solution('aaaabbbccdaa')


