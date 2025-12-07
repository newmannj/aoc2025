from collections import defaultdict
import re
from functools import reduce

# p1
columns = defaultdict(list)
with open("input.txt") as file:
    for line in file:
        values = re.findall(r"\S+", line)
        for i, v in enumerate(values):
            columns[i].append(v)

total = 0
for col in columns.values():
    operation = col.pop(-1)
    acc = int(col.pop(0))
    for r in col:
        if operation == "+":
            acc += int(r)
        elif operation == "*":
            acc *= int(r)
    total += acc
# print(total)

# p2
grid = []
with open("input.txt") as file:
    for line in file:
        grid.append(line.replace("\n", ""))


x = len(grid[0]) - 1
problem_inputs: list[int] = []
total = 0
while x >= 0:
    y = 0
    # Ignore the last row for now
    col_acc: str = ""
    while y <= len(grid) - 1:
        if grid[y][x] in ["+", "*"]:
            problem_inputs.append(int("".join(col_acc)))
            if grid[y][x] == "+":
                total += sum(problem_inputs)
            else:
                total += reduce(lambda x, y: x * y, problem_inputs)
            break
        else:
            col_acc += grid[y][x]
        y += 1
    result = [x for x in col_acc if x != " "]
    if len(result) == 0:
        problem_inputs = []
    else:
        problem_inputs.append(int("".join(result)))
    x -= 1
print(total)
