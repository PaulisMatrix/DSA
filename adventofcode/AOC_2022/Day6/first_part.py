
def solution(file):
    result = 0
    with open(file) as file:
        for line in file:
            line = line.strip()
            for idx in range(0,len(line)):
                chunk = line[idx+0:idx+4]
                if len(set(chunk)) == len(chunk):
                    print(idx+4)
                    break

    
if __name__ == "__main__":
    file = "sample.txt"
    solution(file)