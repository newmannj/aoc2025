import math
from functools import reduce

coordinates = []
with open("test.txt") as file:
    for line in file:
        as_arr = line.strip().split(",")
        coordinates.append(tuple([int(x) for x in as_arr]))


def euclidian_distance(p1, p2):
    return math.sqrt(
        ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2) + ((p1[2] - p2[2]) ** 2)
    )


# Construct an array holding the distances between each point
i = 0
distances: list[tuple[int, tuple, tuple]] = []
while i < len(coordinates) - 1:
    curr = coordinates[i]
    j = i + 1
    while j < len(coordinates):
        check = coordinates[j]
        distance = euclidian_distance(curr, check)
        distances.append((distance, curr, check))
        j += 1
    i += 1
distances = sorted(distances, key=lambda x: x[0])
# Construct a list of dicts with the coordinates of all boxes in circuit
circuits: list[dict[tuple, bool]] = []
num_connected = 0
for d in distances:
    if num_connected >= 10:
        break
    placed = False
    for c in circuits:
        # If both are in the circuit, "nothing happened :)"
        if d[1] in c and d[2] in c:
            placed = True
            continue
        # If either is in the circuit, re-enable both
        elif d[1] in c or d[2] in c:
            c[d[1]] = True
            c[d[2]] = True
            placed = True
            num_connected += 1
            break
    # If we haven't found a match, append a new circuit
    if not placed:
        new = {}
        new[d[1]] = True
        new[d[2]] = True
        circuits.append(new)
        num_connected += 1
circuit_lengths = sorted([len(c.keys()) for c in circuits], reverse=True)
print(circuit_lengths)
result = reduce(lambda x, y: x * y, circuit_lengths[:3])
print(result)
