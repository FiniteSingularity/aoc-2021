def route_count(node_map, next_node, cur_path, revisit=False):
    if next_node.islower() and next_node in cur_path and not revisit:
        revisit=True
    elif next_node.islower() and next_node in cur_path:
        return 0
    elif(next_node == 'end'):
        return 1
    cur_path = cur_path + [next_node]
    count = 0
    for node in node_map[next_node]:
        if node != 'start':
            count += route_count(node_map, node, [c for c in cur_path], revisit)
    return count

nodes = {}
idx = [[0,1], [1,0]]
with open('./input', encoding='utf8') as file:
    for line in file.readlines():
        line = line.strip()
        connection = line.split('-')
        for x,y in idx:
            if connection[x] not in nodes:
                nodes[connection[x]] = []
            nodes[connection[x]].append(connection[y])

print(route_count(nodes, 'start', []))
