dots, insts = open('input').read()[:-1].split('\n\n')
dots = [(int(x), int(y))
        for x, y in [dot.split(',') for dot in dots.split('\n')]]
part1done = False
for inst in insts.split('\n'):
    a, b, c = inst.split(' ')
    xy, d = c.split('=')
    d = int(d)

    for i, (x, y) in enumerate(dots):
        if xy == 'x':
            if x > d:
                dots[i] = (d - (x - d), y)
        else:
            if y > d:
                dots[i] = (x, d - (y - d))
    if not part1done:
        print('part1', len(set(dots)))
        part1done = True

grid = [[' '] * max(x + 1 for x, y in dots)
        for i in range(max(y + 1 for x, y in dots))]
for x, y in dots:
    grid[y][x] = '#'
print('\n'.join(' '.join(g) for g in grid))