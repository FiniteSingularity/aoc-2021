def find_index(nodes, x, y):
    for index, item in enumerate(nodes):
        if item["coord"][0] == x and item["coord"][1] == y:
            return index
    return -1


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
        visited.append([False for _ in line.strip()])
        cumulative_risk_map.append([0 for _ in line.strip()])

# row, col
point = [0, 0]
end = [len(risk_map)-1, len(risk_map[0])-1]

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
    # find next point

print(item['risk'])
