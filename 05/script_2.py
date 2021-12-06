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
    col_step = 1 if line[0][0] <= line[1][0] else -1
    row_step = 1 if line[0][1] <= line[1][1] else -1
    cols = range(line[0][0], line[1][0]+col_step, col_step)
    rows = range(line[0][1], line[1][1]+row_step, row_step)
    if line[0][1] == line[1][1]:
        for col in cols:
            points[line[0][1]][col] += 1
    elif line[0][0] == line[1][0]:
        for row in rows:
            points[row][line[0][0]] += 1
    else:
        steps = zip(cols, rows)
        for step in list(steps):
            points[step[1]][step[0]] += 1

count = 0
for row in points:
    for col in row:
        if col > 1:
            count += 1

print(count)
