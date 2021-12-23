players = [
    # {'position': 0, 'score': 0}
]

with open('./input', encoding='utf8') as file:
    for line in file.readlines():
        players.append({
            'position': int(line.strip().split(': ')[1]),
            'score': 0
        })

max_score = 0
die_rolls = 0
die_value = 0
player = 0

while max_score < 1000:
    moves = 0
    for _ in range(3):
        die_rolls += 1
        die_val = 1 + (die_rolls - 1) % 100
        moves += die_val
    player_position = players[player]['position']
    player_position = 1 + (player_position + moves - 1) % 10
    players[player]['position'] = player_position
    players[player]['score'] += player_position
    max_score = max(max_score, players[player]['score'])
    score = players[player]['score']
    player = (player + 1) % 2


print(min(players[0]['score'], players[1]['score']) * die_rolls)
