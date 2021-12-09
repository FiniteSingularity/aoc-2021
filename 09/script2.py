import pprint


def row_connected(row, col, row_connect, depth_map):
    i = col
    while i < cols and depth_map[row][i] < 9:
        row_connect[i] = True
        i += 1
    i = col - 1
    while i >= 0 and depth_map[row][i] < 9:
        row_connect[i] = True
        i -= 1


with open('./input', encoding='utf8') as file:
    depth_map = [[int(char) for char in line.strip()]
                 for line in file.readlines()]

rows = len(depth_map)
cols = len(depth_map[0])

flat_map = [val for row in depth_map for val in row]

left_compare = [[True] + [l > r for l,
                          r in zip(row[0:-1], row[1:])] for row in depth_map]

right_compare = [[r > l for l, r in zip(
    row[0:-1], row[1:])] + [True] for row in depth_map]

up_compare = [[True]*cols] + [[uv > dv for uv,
                               dv in zip(u, d)] for u, d in zip(depth_map[0:-1], depth_map[1:])]

down_compare = [[dv > uv for uv,
                 dv in zip(u, d)] for u, d in zip(depth_map[0:-1], depth_map[1:])] + [[True]*cols]

risk_sum = 0

low_points = []
# for r in range(0, rows):
#     low_points.append([False]*cols)

for row, (lr, rr, ur, dr, depthr) in enumerate(zip(left_compare, right_compare, up_compare, down_compare, depth_map)):
    for col, (l, r, u, d, depth) in enumerate(zip(lr, rr, ur, dr, depthr)):
        if l and r and u and d:
            low_points.append([row, col])

basin_sizes = []

for row, col in low_points:
    basin = []
    row_connect = [False]*cols
    row_connected(row, col, row_connect, depth_map)
    cur_row = row
    cur_row_connect = [val for val in row_connect]
    if cur_row == 0:
        basin = [row_connect]
    while cur_row > 0 and len(list(filter(lambda x: x == True, row_connect))) > 0:
        basin = [row_connect] + basin
        cur_row_connect = [False]*cols
        for c, connected in enumerate(row_connect):
            if connected and depth_map[cur_row-1][c] < 9:
                row_connected(cur_row-1, c, cur_row_connect, depth_map)
        row_connect = [val for val in cur_row_connect]
        cur_row -= 1

    row_connect = [False]*cols
    row_connected(row, col, row_connect, depth_map)
    cur_row = row

    while cur_row < rows-1 and len(list(filter(lambda x: x == True, row_connect))) > 0:
        cur_row_connect = [False]*cols
        for c, connected in enumerate(row_connect):
            if connected and depth_map[cur_row+1][c] < 9:
                row_connected(cur_row+1, c, cur_row_connect, depth_map)
        row_connect = [val for val in cur_row_connect]
        basin = basin + [row_connect]
        cur_row += 1

    basin_size = 0
    for row in basin:
        basin_size += sum(row)
    basin_sizes.append(basin_size)

basin_sizes = sorted(basin_sizes)[-3:]
prod = 1
for size in basin_sizes:
    prod *= size

print(prod)
