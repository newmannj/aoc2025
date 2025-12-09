posns = []
with open("input.txt") as file:
    for line in file:
        posns.append([int(v) for v in line.strip().split(",")])


def get_area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)


max_area = 0
i = 0
while i < len(posns) - 1:
    j = i + 1
    while j < len(posns):
        check_area = get_area(posns[i], posns[j])
        if check_area > max_area:
            # print("---")
            # print(posns[i])
            # print(posns[j])
            # print(check_area)
            # print("---")
            max_area = check_area
        j += 1
    i += 1
print(max_area)
