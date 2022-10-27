def solution():
    depth = 0
    hori = 0
    with open('input','r') as f:
        for line in f:
            command,value = line.split()
            if command == 'forward':
                hori+=int(value)
            elif command == 'down':
                depth+=int(value)
            else:
                depth-=int(value)

    print(hori*depth)

if __name__=="__main__":
    solution()