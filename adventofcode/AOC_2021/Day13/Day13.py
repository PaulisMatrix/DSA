coords = []
dirs = []

#671
with open('input','r') as f:
    max_x,max_y = float('-inf'),float('-inf')
    for line in f:
        try:
            x,y = [int(i) for i in line.rstrip().split(',')]
            max_x=max(max_x,x)
            max_y=max(max_y,y)
            coords.append((x,y))
        except:
            try:
                dir,pos = line.rstrip().split('=')
                dirs.append((dir[-1],int(pos)))
            except:
                pass

dotted = set()

for dir,pos in dirs:
    for x,y in coords:
        if dir=='x':
            if x>pos:
                x = pos - (x-pos)
        else:
            if y>pos:
                y = pos - (y-pos)
        dotted.add((x,y))
    


'''
for x,y in coords:
    for dir,pos in dirs:
        if dir=='x':
            if x>pos:
                x = pos - (x-pos)
        if dir=='y':
            if y>pos:
                y = pos - (y-pos)
    dotted.add((x,y))
'''
print(max_x,max_y)
matrix = [[' ' for _ in range(max_x)] for _ in range(max_y)]

for x,y in dotted:
    matrix[x][y] = '#'

for rows in matrix:
    print('/n'.join(rows))










