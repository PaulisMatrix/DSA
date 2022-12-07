# from trie import Trie
from collections import defaultdict

"""
Trying trie based solution:
def solution(trie: Trie, file):
    root = False
    last_parent = ""
    with open(file) as file:
        for line in file:
            try:
                f, s, t = line.strip().split(" ")
            except:
                f, s = line.strip().split(" ")
                t = ""

            # skip the first line
            if t == "/":
                root = True
                continue

            if root and (not t) and t != "/":
                # parse the root folder
                if f == "dir":
                    trie.parent_dirs(dir=s)
            else:
                # stop parsing. You are not in root folder anymore.
                root = False
                if f == "$" and s == "cd" and (t not in [".", ".."]):
                    # if t is one of the parent dirs
                    last_child = t
                    if t in trie.root.children:
                        last_parent = t
                elif (not t) and f == "dir" and s:
                    # dir e
                    child_dir = s
                    trie.parse_dirs(
                        parent_dir=last_parent, child_dir=child_dir, file_size=None
                    )
                elif (not t) and f.isnumeric() and s:
                    # 29116 f
                    file_size = int(f)
                    trie.parse_dirs(
                        parent_dir=last_parent,
                        child_dir=last_child,
                        file_size=file_size,
                    )
    final = 0
    for k, v in trie.root.children.items():
        parent = 0
        parent += v.size  # parent
        if parent <= 100000:
            final += parent

        if v.children:
            child = 0
            for kc, vc in v.children.items():
                child += vc.size

            if child <= 100000:
                final += child

        print(final)
    print(trie.root.children)
"""


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

    print(sum(s for s in dirs.values() if s <= 100_000))


if __name__ == "__main__":
    file = "input.txt"
    # trie = Trie()
    # solution(trie=trie, file=file)
    solution(file=file)
