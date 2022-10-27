mat = []

with open('input', 'r') as f:
    for line in f.read().splitlines():
        mat.append([int(x) for x in line])

N = len(mat)
M = len(mat[0])

adj = [[] for i in range(N * M + 1)]
values = [0 for i in range(N * M + 1)]


for r in range(N):
    for c in range(M):
        values[c + r * N] = mat[r][c]

        for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            R = dr + r
            C = dc + c

            if R >= N or C >= M or C < 0 or R < 0:
                continue

            adj[c + r * N].append(C + R * N)

            

count = 0
basins = []

for cell in range(N * M):

    higher = 0

    for other in adj[cell]:

        if values[cell] < values[other]:
            higher += 1

        if higher == len(adj[cell]):
            basins.append(cell)

from collections import deque

scores = []

for base_cell in basins:

    seen = set()
    Q = deque((base_cell,))

    while Q:
        cell = Q.popleft()

        if cell in seen:
            continue

        seen.add(cell)
        
        for other in adj[cell]:

            if values[other] == 9:
                continue
            
            Q.append(other)
            
    scores.append(len(seen))

scores.sort(reverse=True)

print(scores[0] * scores[1] * scores[2])