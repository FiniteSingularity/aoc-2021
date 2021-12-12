pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

with open('./input', encoding='utf8') as file:
    lines = [line.strip() for line in file.readlines()]

score = 0
for line in lines:
    next_char = []
    for char in line:
        if char in pairs:
            next_char.append(pairs[char])
        elif char == next_char[-1]:
            next_char.pop()
        else:
            score += scores[char]
            break

print(score)
