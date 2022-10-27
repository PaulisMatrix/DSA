import heapq
#DAY = 15
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def in_matrix(matrix, i, j):
    n = len(matrix)
    m = len(matrix[0])
    return 0 <= i < n and 0 <= j < m


def extend(matrix, k):
    n = len(matrix)
    m = len(matrix[0])
    return [
        [((matrix[i % n][j % m] - 1) + (i // n) + (j // m)) % 9 + 1 for j in range(m * k)] for i in range(n * k)
    ]


def shortest_path(matrix):
    n = len(matrix)
    m = len(matrix[0])

    INF = 10 * m * n

    d = [[INF] * m for _ in range(n)]
    d[0][0] = 0
    q = [(d[0][0], (0, 0))]

    while q:
        _, (i, j) = heapq.heappop(q)
        for di, dj in moves:
            i2 = i + di
            j2 = j + dj
            if not in_matrix(matrix, i2, j2):
                continue
            if d[i2][j2] > d[i][j] + matrix[i2][j2]:
                heapq.heappush(q, (d[i][j] + matrix[i2][j2], (i2, j2)))
                d[i2][j2] = d[i][j] + matrix[i2][j2]
    return d[-1][-1]


def main():
    with open(f"input") as f:
        matrix = [list(map(int, line.strip())) for line in f.readlines() if line]
    print(f'ans part 1: {shortest_path(matrix)}')
    print(f'ans part 2: {shortest_path(extend(matrix, 5))}')


if __name__ == '__main__':
    main()