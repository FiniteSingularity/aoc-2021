import math
import numpy as np
import copy


def solve_transform(p1, p2, p3, p4):
    block = np.matrix([
        [p1[0][0], p1[0][1], p1[0][2], 1],
        [p2[0][0], p2[0][1], p2[0][2], 1],
        [p3[0][0], p3[0][1], p3[0][2], 1],
        [p4[0][0], p4[0][1], p4[0][2], 1]
    ])
    M = np.kron(np.eye(3, dtype=int), block)
    y = np.matrix([
        p1[1][0], p2[1][0], p3[1][0], p4[1][0],
        p1[1][1], p2[1][1], p3[1][1], p4[1][1],
        p1[1][2], p2[1][2], p3[1][2], p4[1][2],
    ]).getT()
    res = np.dot(np.linalg.inv(M), y).round().astype(int).getT().tolist()
    res_arr = [
        res[0][0:4],
        res[0][4:8],
        res[0][8:],
        [0, 0, 0, 1]
    ]
    T = np.matrix(res_arr).getT()
    return T


def transform_points(points, T):
    new_points = np.dot(np.matrix([point + [1]
                        for point in points]), T).tolist()
    return [pt[0:3] for pt in new_points]


def merge_points(p1, p2):
    merged = copy.deepcopy(p1)
    matched = 0
    for pt in p2:
        match = next(
            (x for x in merged if x[0] == pt[0] and x[1] == pt[1] and x[2] == pt[2]), None)
        if match is None:
            merged.append(pt)
        else:
            matched += 1
    print('matched ', matched)
    return merged


def common_points(s1, s2):
    common_map = {}
    common = []
    for pd in s1:
        dist = pd[0]
        match = next((x for x in s2 if x[0] == dist), None)
        if match is not None:
            common.append([dist, [pd[1], pd[2]], [match[1], match[2]]])
    idx = 0
    if len(common) < 12:
        return []
    for idx, cur in enumerate(common[0:-1]):
        if not cur[1][0] in common_map:
            match = next(
                (x for x in common[idx+1:] if x[1][0] == cur[1][0] or x[1][1] == cur[1][0]), None)
            if match is None:
                continue
            mapped = list(set(cur[2]) & set(match[2]))
            if len(mapped) > 0:
                common_map[cur[1][0]] = mapped[0]
            else:
                continue
        else:
            mapped = [common_map[cur[1][0]]]
        if not cur[1][1] in common_map:
            mapped2 = list(set(cur[2])-set([mapped[0]]))
            if len(mapped2) > 0:
                common_map[cur[1][1]] = mapped2[0]

    return common_map


def distance_calc(scanner):
    dists = []
    for i in range(0, len(scanner)):
        for j in range(i+1, len(scanner)):
            a = scanner[i]
            b = scanner[j]
            dists.append(
                (
                    int(math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])
                                  ** 2 + (a[2]-b[2])**2) * 1000),
                    i,
                    j
                )
            )
    dists.sort(key=lambda x: x[0])
    return dists


def manhattan_dist(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + abs(p1[2]-p2[2])


scanners = []
distances = []

with open('./input', encoding='utf8') as file:
    file_lines = [line.strip() for line in file.readlines()]

for line in file_lines:
    if line == '':
        pass
    elif line[0:2] == '--':
        scanners.append([])
    else:
        scanners[-1].append([int(val) for val in line.split(',')])

merged = scanners.pop(0)

for scanner in scanners:
    dists = distance_calc(scanner)
    distances.append(dists)

scanner_locations = [[0, 0, 0]]

while len(scanners) > 0:
    merged_distances = distance_calc(merged)
    common_count = 0
    idx = -1
    while common_count < 12:
        idx += 1
        common_map = common_points(merged_distances, distances[idx])
        common_count = len(common_map)
    scanner = scanners[idx]
    keys = list(common_map.keys())
    p1 = [scanner[common_map[keys[0]]], merged[keys[0]]]
    p2 = [scanner[common_map[keys[1]]], merged[keys[1]]]
    p3 = [scanner[common_map[keys[2]]], merged[keys[2]]]
    p4 = [scanner[common_map[keys[3]]], merged[keys[3]]]

    T = solve_transform(p1, p2, p3, p4)
    pts_prime = transform_points(scanner, T)
    print(f'---- {idx} ----')
    scanner_locations.append(T[3, :3][0].tolist()[0])
    merged = merge_points(copy.deepcopy(merged), pts_prime)
    scanners.pop(idx)
    distances.pop(idx)

print(f'Part 1: {len(merged)}')

dists = []
for i, loc in enumerate(scanner_locations):
    for j in range(i+1, len(scanner_locations)):
        dists.append(manhattan_dist(loc, scanner_locations[j]))
print(f'Part 2: {max(dists)}')
