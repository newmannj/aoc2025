grid = []
with open("input.txt") as file:
    for line in file:
        grid.append(list(line.strip()))


def get_neighbors(grid, y, x) -> list[tuple[int, int]]:
    # Return a list of neighbor rolls
    directions = [
        # Top left
        (-1, -1),
        # Top
        (-1, 0),
        # Top right
        (-1, 1),
        # Left
        (0, -1),
        # Right
        (0, 1),
        # Bottom right
        (1, 1),
        # Bottom
        (1, 0),
        # Bottom left
        (1, -1),
    ]
    result: list[tuple[int, int]] = []
    for d in directions:
        next_pos = (y + d[0], x + d[1])
        if (
            next_pos[0] >= 0
            and next_pos[0] < len(grid)
            and next_pos[1] >= 0
            and next_pos[1] < len(grid[y])
        ):
            # We're in bounds!
            next_char = grid[next_pos[0]][next_pos[1]]
            if next_char == "@":
                result.append(next_pos)
    return result


# p1
total = 0
y = 0
while y < len(grid):
    x = 0
    while x < len(grid[y]):
        if grid[y][x] == "@":
            neighbors = get_neighbors(grid, y, x)
            if len(neighbors) < 4:
                total += 1
        x += 1
    y += 1

print(total)


def remove_accessible_rolls(grid):
    # Removes accessible rolls, returns updated grid and number of rolls removed
    rolls_to_remove = []
    total = 0
    y = 0
    while y < len(grid):
        x = 0
        while x < len(grid[y]):
            if grid[y][x] == "@":
                neighbors = get_neighbors(grid, y, x)
                if len(neighbors) < 4:
                    rolls_to_remove.append((y, x))
                    total += 1
            x += 1
        y += 1
    for roll in rolls_to_remove:
        grid[roll[0]][roll[1]] = "."
    return grid, total


final_result = 0
while True:
    grid, rolls_removed = remove_accessible_rolls(grid)
    if rolls_removed == 0:
        break
    final_result += rolls_removed

print(final_result)
