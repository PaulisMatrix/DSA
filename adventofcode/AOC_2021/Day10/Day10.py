

def Day10():
    points = {')': 3, ']': 57, '}': 1197, '>': 25137}
    match = {'(': ')', '{': '}', '[': ']', '<': '>'}
    result = 0
    
    '''
    with open('input','r') as f:
        for line in f:
            count = 0
            stack = []
            for char in line.rstrip():
                if char in '([{<':
                    stack.append(char)
                else:
                    shar = match[stack.pop()]
                    if char!=shar:
                        count+=points[char]
                        break
            result+=count
    print(result)
    '''
    result_part2 = []
    points_part2 = {')': 1, ']': 2, '}': 3, '>': 4}
    with open('input','r') as f:
        for line in f:
            stack = []
            count_part2 = 0
            exclude = True
            for char in line.rstrip():
                if char in '([{<':
                    stack.append(char)
                else:
                    shar = match[stack.pop()]
                    if char!=shar:
                        exclude = False
                        break
            if exclude and stack!=None:
                r_stack = stack[::-1]
                for chr in r_stack:
                    bracket = match[chr]
                    val = points_part2[bracket]
                    count_part2 = (count_part2*5) + val
                result_part2.append(count_part2)
    result_part2.sort()
    print(result_part2[len(result_part2)//2])


if __name__=="__main__":
    Day10()
            
