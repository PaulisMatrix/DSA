def solution(file):
    result = 0
    with open(file) as file:
        for line in file:
            x,y = line.strip().split(",")
            x0,x1 = list(map(int,x.split("-")))
            y0,y1 = list(map(int,y.split("-")))

            if x0 <= y0 and x1 >= y1:
                result += 1
            elif x0 >= y0 and x1 <= y1:
                result += 1

    print(result)
if __name__ == "__main__":
    file = "input.txt"
    solution(file)