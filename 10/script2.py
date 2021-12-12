from statistics import median

pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

with open('./input', encoding='utf8') as file:
    lines = [line.strip() for line in file.readlines()]

line_scores = []

for line in lines:
    next_char = []
    invalid = False
    for char in line:
        if char in pairs:
            next_char.append(pairs[char])
        elif char == next_char[-1]:
            next_char.pop()
        else:
            invalid = True
            break
    if invalid:
        continue
    completion = next_char[-1::-1]
    line_score = 0
    for char in completion:
        line_score *= 5
        line_score += scores[char]
    line_scores.append(line_score)

print(median(line_scores))
