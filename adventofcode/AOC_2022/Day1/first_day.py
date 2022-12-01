import os

def solution(file,num_elfs):
    max_calories = [0]

    with open(file) as file:
        for line in file:
            if line == os.linesep:
                max_calories.append(0)
            else:
                max_calories[-1]+=int(line)

    max_calories.sort(reverse=True)
    print(sum(max_calories[:num_elfs]))

if __name__ == "__main__":
    #file = "first_part.txt"
    #num_elfs = 1
    
    file = "second_part.txt"
    num_elfs = 3

    solution(file,num_elfs)