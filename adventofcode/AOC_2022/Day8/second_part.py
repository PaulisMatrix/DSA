def solution(file):
    with open(file) as f:
        grid = [list(map(int, line)) for line in f.read().splitlines()]
        max_score = float("-inf")

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                score = 1
                z = grid[x][y]

                # right
                for i in range(y + 1, len(grid[0])):
                    if grid[x][i] >= z:
                        score *= i - y
                        break
                else:
                    score *= len(grid[0]) - 1 - y

                # left
                for i in range(y - 1, -1, -1):
                    if grid[x][i] >= z:
                        score *= y - i
                        break
                else:
                    score *= y

                # top
                for i in range(x + 1, len(grid)):
                    if grid[i][y] >= z:
                        score *= i - x
                        break
                else:
                    score *= len(grid) - 1 - x

                # bottom
                for i in range(x - 1, -1, -1):
                    if grid[i][y] >= z:
                        score *= x - i
                        break
                else:
                    score *= x

                max_score = max(max_score, score)

    print("Part 2:", max_score)


if __name__ == "__main__":
    file = "input.txt"
    solution(file=file)
