import json
import math
import copy


def reduce(sn):
    found = True
    while found:
        exp_found = True
        while exp_found:
            sn, _, _, exp_found = explode(sn)
        sn, found = split(sn)
    return sn


def add_dir(sn, idx, val):
    if isinstance(sn[idx], list):
        sn[idx] = add_dir(sn[idx], idx, val)
    else:
        sn[idx] += val
    return sn


def explode(sn, depth=0):
    left = 0
    right = 0
    found = False
    if isinstance(sn, int):
        return (sn, left, right, found)
    if(depth != 3):
        sn[0], l_left, l_right, found = explode(sn[0], depth+1)
        if found:
            if isinstance(sn[1], list) and l_right > 0:
                sn[1] = add_dir(sn[1], 0, l_right)
                #sn[1][0] += l_right
            elif l_right > 0:
                sn[1] += l_right
            left = l_left
        else:
            sn[1], r_left, r_right, found = explode(sn[1], depth+1)
            if found:
                if isinstance(sn[0], list) and r_left > 0:
                    sn[0] = add_dir(sn[0], 1, r_left)
                    #sn[0][1] += r_left
                elif r_left > 0:
                    sn[0] += r_left
                right = r_right
    else:
        if isinstance(sn[0], list):
            if isinstance(sn[1], int):
                sn[1] += sn[0][1]
            else:
                sn[1] = add_dir(sn[1], 0, sn[0][1])
            left = sn[0][0]
            sn[0] = 0
            found = True
        elif isinstance(sn[1], list):
            if isinstance(sn[0], int):
                sn[0] += sn[1][0]
            else:
                sn[0] = add_dir(sn[0], 1, sn[1][0])
            right = sn[1][1]
            sn[1] = 0
            found = True
    return (sn, left, right, found)


def split(sn):
    if isinstance(sn, int):
        if sn > 9:
            return ([math.floor(sn/2), math.ceil(sn/2)], True)
        else:
            return (sn, False)
    else:
        sn[0], found = split(sn[0])
        if not found:
            sn[1], found = split(sn[1])
    return (sn, found)


def addition(sn1, sn2):
    return reduce([copy.deepcopy(sn1), copy.deepcopy(sn2)])


def magnitude(sn):
    if isinstance(sn[0], list):
        l = 3 * magnitude(sn[0])
    else:
        l = 3 * sn[0]
    if isinstance(sn[1], list):
        r = 2 * magnitude(sn[1])
    else:
        r = 2 * sn[1]
    return l + r


with open('./input', encoding='utf8') as file:
    sns = [json.loads(val.strip()) for val in file.readlines()]

max_mag = 0

for i in range(0, len(sns)):
    for j in range(0, len(sns)):
        if i != j:
            max_mag = max(max_mag, magnitude(addition(sns[i], sns[j])))

print(max_mag)
