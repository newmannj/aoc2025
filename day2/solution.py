# p1
with open("input.txt") as file:
    total = 0
    for line in file:
        ranges = line.split(",")
        for r in ranges:
            bounds = r.split("-")
            start = int(bounds[0])
            end = int(bounds[1])
            for x in range(start, end + 1):
                as_string = str(x)
                str_len = len(as_string)
                if as_string[0 : int(str_len / 2)] == as_string[int(str_len / 2) :]:
                    total += x
    print(total)

# p2
with open("input.txt") as file:
    total = 0
    for line in file:
        ranges = line.split(",")
        for r in ranges:
            bounds = r.split("-")
            start = int(bounds[0])
            end = int(bounds[1])
            for x in range(start, end + 1):
                # For each value, take substring up to 1/2 the length
                # and see if it is solely that sequence
                as_string = str(x)
                str_len = len(as_string)
                for i in range(1, int(str_len / 2) + 1):
                    # First, calculate the check string
                    check = as_string[0:i]
                    # Then, compare the check to each substring of length i
                    count = as_string.count(check)
                    if count * i == str_len:
                        total += x
                        break
    print(total)
