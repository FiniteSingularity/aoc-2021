from collections import Counter

polymer_map = {}
chars = []

half_length = 20

with open('./input', encoding='utf8') as file:
    template = file.readline().strip()
    _ = file.readline()
    while True:
        line=file.readline()
        if line=='':
            break
        pm = line.strip().split(' -> ')
        polymer_map[pm[0]] = f'{pm[0][0]}{pm[1]}'
        chars.append(pm[0][0])
        chars.append(pm[0][1])

counts = {char: 0 for char in list(set(chars))}

for step in range(0, half_length):
    new_template = ''
    for i in range(0, len(template)-1):
        new_template += polymer_map[template[i:i+2]]
    new_template += template[-1]
    template = new_template

map_counts = {}
for key in polymer_map:
    print(f'--- {key} ---')
    sub_template = f'{key}'
    for step in range(0, half_length):
        new_sub_template = ''
        for i in range(0, len(sub_template)-1):
            new_sub_template += polymer_map[sub_template[i:i+2]]
        new_sub_template += sub_template[-1]
        sub_template = new_sub_template
    
    map_counts[key] = {k: value for k, value in Counter(sub_template[:-1]).items()}

for idx in range(0, len(template[0:-1])):
    char_counts = map_counts[template[idx:idx+2]]
    for char, count in char_counts.items():
        counts[char] += count
counts[template[-1]] = counts[template[-1]] + 1
counts = {value: key for key, value in counts.items()}
max_count = max(counts.keys())
min_count = min(counts.keys())

print(max_count - min_count)