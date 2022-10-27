from collections import defaultdict
import re

a = open('input').read()[:-1].split('\n')
start = a[0]
a = a[2:]

def printpop(h):
    pop = defaultdict(int)
    for k, v in h.items():
        pop[k[0]] += v
        pop[k[1]] += v
    wot = sorted(v for k, v in pop.items())
    aa = wot[1] // 2
    bb = wot[-1] // 2
    print(bb - aa)

hist = defaultdict(int)
for i in range(len(start) - 1):
    hist[start[i] + start[i + 1]] += 1
hist['Z' + start[0]] = 1
hist[start[-1] + 'Z'] = 1

for step in range(40):
    for line in a:
        x, y = line.split(' -> ')
        if x in hist:
            z1 = x[0] + y.lower()
            z2 = y.lower() + x[1]
            n = hist[x]
            hist[z1] += n
            hist[z2] += n
            hist[x] = 0
    hist2 = defaultdict(int)
    for k, v in hist.items():
        hist2[k.upper()] += v
    hist = hist2

printpop(hist)