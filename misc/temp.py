
'''
First:    
Write a program that finds the largest of given numbers?
1, 3, 5, 7, 9, 11, 2, 4, 6, 13, 8

Second:
Consider two strings:
s1 = "abc"
s2 = "aacbabcabdefabcaac"
Can you find number of occurrences of permutations of s1 in s2?
'''

from collections import Counter

def second(s1,s2):
    left = 0
    right = len(s1) - 1

    result = []
    while right < len(s2):
        if Counter(s1) == Counter(s2[left:right+1]):
            result.append(left)
        left+=1
        right+=1

    return result


def solution(score):
    sorted_scores = sorted(score,reverse=True)
    mydict = {num:idx for idx,num in enumerate(sorted_scores,start=1)}
    medals = {1:"Gold",2:"Silver",3:"Bronze"}

    result = []
    for nums in score:
        result.append(medals.get(mydict[nums],str(mydict[nums])))
    return result

solution([10,3,8,9,4])

import heapq

def first(nums):
    heapq.heapify(nums)

    print(heapq.nlargest(3,nums))


if __name__ == "__main__":
    first([1, 3, 5, 7, 9, 11, 2, 4, 6, 13, 8])


