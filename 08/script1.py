data = []
with open('./input', encoding='utf8') as file:
    for line in file.readlines():
        s_dat, d_dat = line.strip().split(' | ')
        signals = [digit for digit in s_dat.split(' ')]
        digits = [digit for digit in d_dat.split(' ')]
        data.append({'signals': signals, 'digits': digits})

count = 0

lengths = [2, 4, 3, 7]

for row in data:
    for digit in filter(lambda x: len(x) in lengths, row['digits']):
        count += 1

print(count)
