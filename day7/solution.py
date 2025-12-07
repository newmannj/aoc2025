# p1
# beams: set[int] = set()
# splits = 0
# with open("input.txt") as file:
#     for y, line in enumerate(file):
#         # print("Active beams at row: ", y, " beams: ", beams)
#         for x, c in enumerate(line):
#             if c == "S":
#                 beams.add(x)
#             elif c == "^" and x in beams:
#                 # print("conflict detected: ", x, " ", beams)
#                 splits += 1
#                 beams.remove(x)
#                 beams.add(x - 1)
#                 beams.add(x + 1)
# print(splits)


# p2
# Kindof a DFS problem
grid = []
with open("input.txt") as file:
    for line in file:
        grid.append(line.strip())

pos_x = grid[0].index("S")

hits = 0


def dfs(x, y, grid, path):
    if y >= len(grid):
        global hits
        hits += 1
        return path
    if grid[y][x] == "^":
        left_path = list(path)
        left_path.append("L")
        right_path = list(path)
        right_path.append("R")
        dfs(x - 1, y, grid, left_path)
        dfs(x + 1, y, grid, right_path)
    else:
        dfs(x, y + 1, grid, path)


dfs(pos_x, 0, grid, [])
print(hits)
