from collections import defaultdict


def solution(file):
    with open(file) as f:
        dirs = defaultdict(int)
        cwd = []
        for line in f.read().splitlines():
            if line.startswith("$ cd"):
                ls = False
                d = line[5:]
                if d == "..":
                    cwd.pop()
                else:
                    cwd.append(d)
            elif line.startswith("$ ls"):
                continue
            else:
                try:
                    dirs["/".join(cwd)] += int(line.split()[0])
                except ValueError:
                    pass

    for d in sorted(dirs.keys(), key=lambda x: x.count("/"), reverse=True):
        dirs["/".join(d.split("/")[:-1])] += dirs[d]

    free = 70_000_000 - dirs["/"]
    needed = 30_000_000 - free
    print(min(v for v in dirs.values() if v > needed))


if __name__ == "__main__":
    file = "input.txt"
    # trie = Trie()
    # solution(trie=trie, file=file)
    solution(file=file)
