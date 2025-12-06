# parsing
ranges: list[tuple[int, int]] = []
read_ids = False
raw_ids = []
fresh_id_count = 0
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        if len(line) == 0:
            read_ids = True
            continue
        if not read_ids:
            as_arr = line.split("-")
            ranges.append((int(as_arr[0]), int(as_arr[1])))
        if read_ids:
            raw_ids.append(int(line))

# p1
for x in raw_ids:
    for r in ranges:
        if x >= r[0] and x <= r[1]:
            fresh_id_count += 1
            break
print(fresh_id_count)

# p2
sorted_ranges = sorted(ranges, key=lambda r: r[0])
# First, combine any ranges that overlap
i = 0
j = 1
while j < len(sorted_ranges):
    # Check to see if neighboring ranges overlap
    r0 = sorted_ranges[i]
    r1 = sorted_ranges[j]
    if r1[0] <= r0[1]:
        # combine
        upper_limit = max(r1[1], r0[1])
        combined = (r0[0], upper_limit)
        # Remove comparison range in place
        sorted_ranges.pop(j)
        sorted_ranges[i] = combined
        # Because we've removed, we'll already be checking the next one
    else:
        # Otherwise, we know we can bump both values
        i += 1
        j += 1
# Then for each range, calculate the difference
fresh_id_count = 0
for r in sorted_ranges:
    # Add one since we're including the bounds
    fresh_id_count += r[1] - r[0] + 1
print(fresh_id_count)
