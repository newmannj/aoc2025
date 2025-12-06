from collections import defaultdict
import re

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
print(total)

# p2
columns_2 = []
with open("test.txt") as file:
    for line in file:
        values = re.findall(r"\S+", line)
        for i, v in enumerate(values):
            digits = list(v)
            digits.reverse()
            print(digits)

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
print(total)
