import math
from functools import reduce

coordinates = []
with open("input.txt") as file:
    for line in file:
        as_arr = line.strip().split(",")
        coordinates.append(tuple([int(x) for x in as_arr]))


def euclidian_distance(p1, p2):
    return math.sqrt(
        ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2) + ((p1[2] - p2[2]) ** 2)
    )


boxes = set()
# Construct an array holding the distances between each point
i = 0
distances: list[tuple[int, tuple, tuple]] = []
while i < len(coordinates) - 1:
    curr = coordinates[i]
    boxes.add(curr)
    j = i + 1
    while j < len(coordinates):
        check = coordinates[j]
        boxes.add(check)
        distance = euclidian_distance(curr, check)
        distances.append((distance, curr, check))
        j += 1
    i += 1
distances = sorted(distances, key=lambda x: x[0])
# Construct a list of sets with the coordinates of all boxes in circuit
# TODO: Need to merge circuits that may have been connected by something down the line
circuits: list[set[tuple]] = []
num_connected = 0
for d in distances:
    # Get the circuit for each box. We assume there will only ever be one
    possible_d1_circuits = [c for c in circuits if d[1] in c]
    possible_d2_circuits = [c for c in circuits if d[2] in c]
    d1_circuit = possible_d1_circuits[0] if len(possible_d1_circuits) != 0 else set()
    d2_circuit = possible_d2_circuits[0] if len(possible_d2_circuits) != 0 else set()
    # If there is no circuits for either node, create a new one
    if not d1_circuit and not d2_circuit:
        new = {d[1], d[2]}
        circuits.append(new)
        num_connected += 1
    elif difference := d1_circuit ^ d2_circuit:
        # If there is a difference, remove both circuits, merge to d1, add back
        circuits = [c for c in circuits if c != d1_circuit and c != d2_circuit]
        merged = d1_circuit.union(d2_circuit)
        merged.add(d[1])
        merged.add(d[2])
        circuits.append(merged)
        num_connected += 1
    else:
        num_connected += 1
    boxes.discard(d[1])
    boxes.discard(d[2])
    if len(boxes) == 0:
        print("no more to join!")
        print(d)
        break


circuit_lengths = sorted([len(c) for c in circuits], reverse=True)
print(circuit_lengths)
result = reduce(lambda x, y: x * y, circuit_lengths[:3])
print(result)
