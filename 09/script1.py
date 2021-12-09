

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

for lr, rr, ur, dr, depthr in zip(left_compare, right_compare, up_compare, down_compare, depth_map):
    for l, r, u, d, depth in zip(lr, rr, ur, dr, depthr):
        if l and r and u and d:
            risk_sum += (1+depth)

print(risk_sum)
