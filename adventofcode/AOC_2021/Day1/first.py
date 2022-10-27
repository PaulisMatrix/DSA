def solution():
    count = 0
    number = 0
    with open("input.txt") as f:
        for line in f:
            if int(line) > number:
                count+=1
            number = int(line)
    print(count)



if __name__ == "__main__":
    solution()

