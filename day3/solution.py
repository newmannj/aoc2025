# p1
with open("input.txt") as file:
    total = 0
    for line in file:
        cur_max = 0
        j = 0
        while j < len(line) - 1:
            i = j + 1
            while i < len(line) - 1:
                check = line[j] + line[i]
                if int(check) > cur_max:
                    cur_max = int(check)
                i += 1
            j += 1
        total += cur_max
    print(total)

# p2
with open("test.txt") as file:
    total = 0
    for line in file:
        line = line.strip()
        cur_max = 0
        start = len(line) - 12
        left_bounds = 0
        acc = []
        n = 0
        for x in range(start, len(line)):
            n += 1
            max_battery = int(line[x])
            changed = False
            for j in range(left_bounds, x):
                cmp = int(line[j])
                if cmp > max_battery:
                    max_battery = cmp
                    # Set the left bounds for future checks
                    left_bounds = j + 1
                    changed = True
            if not changed:
                left_bounds = x + 1

            acc.append(str(max_battery))

        print(acc)
        total += int("".join(acc))

    print(total)
