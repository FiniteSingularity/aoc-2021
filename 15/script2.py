def find_index(nodes, x, y):
    for index, item in enumerate(nodes):
        if item["coord"][0] == x and item["coord"][1] == y:
            return index
    return -1


def tile_input(risk_nodes, x=5, y=5):
    tiled = tile_x(risk_nodes, x)
    tiled = tile_x([list(x) for x in zip(*tiled)], y)
    return [list(x) for x in zip(*tiled)]


def tile_x(risk_nodes, x=5):
    tiled = []
    for row in risk_nodes:
        row_vals = []
        for loop in range(0, x):
            row_vals += [1 + ((val - 1 + loop) % 9) for val in row]
        tiled.append(row_vals)
    return tiled


risk_map = []
cumulative_risk_map = []

visited = []
active_nodes = [
    {"coord": [0, 0], "risk": 0, "from": None}
]

#  {"coord": [52, 50], "risk": 123, "from": [51, 50]}

with open('./input', encoding='utf8') as file:
    for line in file.readlines():
        risk_map.append([int(val) for val in line.strip()])

risk_map = tile_input(risk_map, 5)
for row in risk_map:
    visited.append([False for _ in row])
    cumulative_risk_map.append([0 for _ in row])


# row, col
point = [0, 0]
end = [len(risk_map)-1, len(risk_map[0])-1]
max_x = 0
max_y = 0

found = False
while not found:
    # do some anylitical crazy stuff
    visited[point[0]][point[1]] = True
    dir_x = list(set([max(0, point[0]-1), point[0], min(point[0]+1, end[0])]))
    dir_y = list(set([max(0, point[1]-1), point[1], min(point[1]+1, end[1])]))
    points = []
    for x in dir_x:
        if(x != point[0]):
            points.append([x, point[1]])
    for y in dir_y:
        if(y != point[1]):
            points.append([point[0], y])

    for x, y in points:
        if(not visited[x][y]):
            index = find_index(active_nodes, x, y)
            risk = risk_map[x][y] + cumulative_risk_map[point[0]][point[1]]
            if index == -1:
                active_nodes.append({
                    "coord": [x, y],
                    "risk": risk,
                    "from": [point[0], point[1]]
                })
                cumulative_risk_map[x][y] = risk
            else:
                if active_nodes[index]["risk"] > risk:
                    active_nodes[index]["risk"] = risk
                    active_nodes[index]["from"] = [point[0], point[1]]
                    cumulative_risk_map[x][y] = risk

    # remove point from active list
    index = find_index(active_nodes, point[0], point[1])
    active_nodes.pop(index)
    cur_risk = 9999999999999
    min_index = 0
    for index, item in enumerate(active_nodes):
        if item["risk"] < cur_risk:
            min_index = index
            point = [item["coord"][0], item["coord"][1]]
            cur_risk = item["risk"]
    if point[0] == end[0] and point[1] == end[1]:
        break
print(item['risk'])
