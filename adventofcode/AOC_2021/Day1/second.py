def solution(lines):
	print(sum(j > i for i,j in zip(lines,lines[3:])))


if __name__ == "__main__":
	lines = []
	with open("input.txt") as f:
		for l in f:
			lines.append(int(l))
	solution(lines)
	