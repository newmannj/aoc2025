# p1
beams: set[int] = set()
splits = 0
with open("input.txt") as file:
    for y, line in enumerate(file):
        # print("Active beams at row: ", y, " beams: ", beams)
        for x, c in enumerate(line):
            if c == "S":
                beams.add(x)
            elif c == "^" and x in beams:
                # print("conflict detected: ", x, " ", beams)
                splits += 1
                beams.remove(x)
                beams.add(x - 1)
                beams.add(x + 1)
print(splits)
