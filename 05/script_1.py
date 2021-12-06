# Open input, and split each line into list of 0 or 1 integers
with open('./input', encoding='utf8') as file:
    vent_lines = [[[int(val) for val in endpoint.split(',')]
                   for endpoint in line.split(' -> ')] for line in file]

dims = [0, 0]
for line in vent_lines:
    for val in line:
        dims[0] = max(dims[0], val[0]+1)
        dims[1] = max(dims[1], val[1]+1)

points = [[0] * dims[1] for _ in range(dims[0])]

for line in vent_lines:
    if line[0][1] == line[1][1]:
        for col in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0])+1):
            points[line[0][1]][col] += 1
    if line[0][0] == line[1][0]:
        for row in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1])+1):
            points[row][line[0][0]] += 1

count = 0
for row in points:
    for col in row:
        if col > 1:
            count += 1

print(count)
