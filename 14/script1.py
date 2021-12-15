from collections import Counter

polymer_map = {}

with open('./input_test', encoding='utf8') as file:
    template = file.readline().strip()
    _ = file.readline()
    while True:
        line=file.readline()
        if line=='':
            break
        pm = line.strip().split(' -> ')
        polymer_map[pm[0]] = f'{pm[0][0]}{pm[1]}'

for step in range(0, 10):
    new_template = ''
    for i in range(0, len(template)-1):
        new_template += polymer_map[template[i:i+2]]
    new_template += template[-1]
    template = new_template

count = Counter(new_template)
count = {value: key for key, value in count.items()}
max_count = max(count.keys())
min_count = min(count.keys())

print(max_count - min_count)
