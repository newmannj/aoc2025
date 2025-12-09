red_tiles: list[tuple[int, int]] = []
green_tiles = []


def print_grid(red_tiles, green_tiles):
    grid_height = 15
    grid_width = 15
    grid = [["." for x in range(0, grid_width)] for y in range(0, grid_height)]
    for t in red_tiles:
        grid[t[0]][t[1]] = "#"
    for t in green_tiles:
        grid[t[0]][t[1]] = "X"
    print("-" * grid_width)
    for row in grid:
        print(row)
    print("-" * grid_width)


with open("test.txt") as file:
    for r, line in enumerate(file):
        next_tile = tuple([int(v) for v in line.strip().split(",")])
        # Starting at second tile location, calculate green tiles
        if len(red_tiles) > 0:
            prev_tile = red_tiles[r - 1]
            # If y is aligned, shift x otherwise shift y
            index_to_shift = 0 if prev_tile[1] == next_tile[1] else 1
            aligned_index = 0 if index_to_shift == 1 else 1
            step = -1 if prev_tile[index_to_shift] > next_tile[index_to_shift] else 1
            # Don't put a green tile where a red tile is
            for x in range(
                prev_tile[index_to_shift] + 1, next_tile[index_to_shift], step
            ):
                new_tile = [0, 0]
                new_tile[index_to_shift] = x
                new_tile[aligned_index] = prev_tile[aligned_index]
                green_tiles.append(tuple(new_tile))
        red_tiles.append(next_tile)
        print_grid(red_tiles, green_tiles)
        if r == 3:
            break


# TODO: Connect the last and first tile


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
