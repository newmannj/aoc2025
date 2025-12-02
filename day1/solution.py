import math
# p1
start = 50
z_count = 0
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        if line[0] == 'R':
            start += int(line[1:])
            start = start % 100
        else:
            start -= int(line[1:])
            start = start % 100
            if start < 0:
                start += 100
        if start == 0:
            z_count += 1

print(z_count)


# p2
# gross, but it works!
start = 50
z_count = 0
with open("input.txt") as file:
    for line in file:
        line = line.strip()
        if line[0] == 'R':
            val = int(line[1:])
            while val > 0:
                start += 1
                start = start % 100
                if start == 0:
                    z_count += 1
                val -= 1
        else:
            val = int(line[1:])
            while val > 0:
                start -= 1
                start = start % 100
                if start == 0:
                    z_count += 1
                val -= 1
            if start < 0:
                start += 100 

print(z_count)