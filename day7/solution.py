from collections import defaultdict

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


# p2
beam_dict: dict[int, int] = defaultdict(int)
with open("input.txt") as file:
    for y, line in enumerate(file):
        for x, c in enumerate(line):
            if c == "S":
                beam_dict[x] += 1
            elif c == "^" and x in beam_dict:
                path_count = beam_dict[x]
                beam_dict[x] = 0
                beam_dict[x - 1] += path_count
                beam_dict[x + 1] += path_count
print(sum(beam_dict.values()))
