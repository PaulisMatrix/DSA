def solution(file):
    with open(file) as f:
        grid = [list(map(int, line)) for line in f.read().splitlines()]
        visibles = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                visible = False
                z = grid[x][y]

                # right
                for i in range(y + 1, len(grid[0])):
                    if grid[x][i] >= z:
                        break
                else:
                    visible = True

                # left
                for i in range(y - 1, -1, -1):
                    if grid[x][i] >= z:
                        break
                else:
                    visible = True

                # top
                for i in range(x + 1, len(grid)):
                    if grid[i][y] >= z:
                        break
                else:
                    visible = True

                # bottom
                for i in range(x - 1, -1, -1):
                    if grid[i][y] >= z:
                        break
                else:
                    visible = True
                if visible:
                    visibles += 1

    print("Part 1:", visibles)


if __name__ == "__main__":
    file = "input.txt"
    solution(file=file)
