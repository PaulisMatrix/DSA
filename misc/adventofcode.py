import itertools

required = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
'''
count = 0
with open("input.txt") as f:
    for line in f:
        print(line.strip().split(" ")[2].split(":")[0])
        break



Day One:
for a,b,c in itertools.combinations(numbers,3):
    if (a+b+c) == 2020:
        print(a*b*c)

Day Two:
for line in f:
        number,char,text = line.strip().split()
        first,second = number.split("-")
        #if int(first) <= text.count(char[0]) <= int(second):
            #count+=1 #First Part
        if ((text[int(first)-1] == char[0]) != (text[int(second)-1] == char[0])):
            count+=1  #Second Part
'''

line = 'eyr:2029 pid:157374862 byr:1991 ecl:amb hcl:#a97842 hgt:178cm'
count = 0
flag = 0
for i in range(len(line.strip().split(" "))):
    if line.strip().split(" ")[i].split(":")[0] in required:
        count+=1
    else:
        break


print(count)
