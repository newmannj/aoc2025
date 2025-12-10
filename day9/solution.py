red_tiles: list[tuple[int, int]] = []
green_tiles = []


def print_grid(red_tiles, green_tiles):
    grid_height = 100_000
    grid_width = 100_000
    grid = [["." for x in range(0, grid_width)] for y in range(0, grid_height)]
    for t in red_tiles:
        grid[t[1]][t[0]] = "#"
    for t in green_tiles:
        grid[t[1]][t[0]] = "X"
    print("-" * grid_width)
    for row in grid:
        print(row)


# UP, RIGHT, DOWN, LEFT
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

with open("input.txt") as file:
    for r, line in enumerate(file):
        next_tile = tuple([int(v) for v in line.strip().split(",")])
        red_tiles.append(next_tile)


i = 0
while i < len(red_tiles) - 1:
    prev_tile = red_tiles[i]
    next_tile = red_tiles[i + 1]
    x_diff = prev_tile[0] - next_tile[0]
    y_diff = prev_tile[1] - next_tile[1]
    if x_diff < 0:
        direction = directions[1]
    elif x_diff > 0:
        direction = directions[3]
    elif y_diff < 0:
        direction = directions[0]
    elif y_diff > 0:
        direction = directions[2]
    while True:
        prev_tile = (prev_tile[0] + direction[0], prev_tile[1] + direction[1])
        if prev_tile == next_tile:
            break
        else:
            green_tiles.append(prev_tile)
    i += 1


prev_tile = red_tiles[-1]
next_tile = red_tiles[0]
x_diff = prev_tile[0] - next_tile[0]
y_diff = prev_tile[1] - next_tile[1]
if x_diff < 0:
    direction = directions[1]
elif x_diff > 0:
    direction = directions[3]
elif y_diff < 0:
    direction = directions[0]
elif y_diff > 0:
    direction = directions[2]
while True:
    prev_tile = (prev_tile[0] + direction[0], prev_tile[1] + direction[1])
    if prev_tile == next_tile:
        break
    else:
        green_tiles.append(prev_tile)

print_grid(red_tiles, green_tiles)


def get_area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


max_area = 0
i = 0
while i < len(red_tiles) - 1:
    j = i + 1
    while j < len(red_tiles):
        check_area = get_area(red_tiles[i], red_tiles[j])
        if check_area > max_area:
            max_area = check_area
        j += 1
    i += 1
print(max_area)
