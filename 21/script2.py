step_outcomes = {
    3: 1,
    4: 3,
    5: 6,
    6: 7,
    7: 6,
    8: 3,
    9: 1,
}


def run_game(position, num_rolls_count={}, score=0, num_rolls=1):
    for outcome, occurrances in step_outcomes.items():
        new_position = 1 + (position + outcome - 1) % 10
        new_score = score + new_position
        if new_score < 21:
            outcome_num_rolls_count = run_game(
                new_position, {}, new_score, num_rolls + 1)
            for key, item in outcome_num_rolls_count.items():
                if key not in num_rolls_count:
                    num_rolls_count[key] = 0
                num_rolls_count[key] += item * occurrances
        else:
            if num_rolls not in num_rolls_count:
                num_rolls_count[num_rolls] = 0
            num_rolls_count[num_rolls] += occurrances
    return num_rolls_count


def calc_continues(games):
    last_continue = 1
    for i in range(1, max(games.keys())+1):
        if i not in games:
            games[i] = {'wins': 0, 'continues': 0}
        else:
            games[i] = {'wins': games[i], 'continues': 0}
        plays = last_continue * 27
        games[i]['continues'] = plays - games[i]['wins']
        last_continue = games[i]['continues']
    return games


players = []

with open('./input', encoding='utf8') as file:
    for line in file.readlines():
        players.append({
            'position': int(line.strip().split(': ')[1]),
            'score': 0
        })


res_1 = run_game(players[0]['position'], {})
res_2 = run_game(players[1]['position'], {})

res_1 = calc_continues(res_1)
res_2 = calc_continues(res_2)

p1_wins = 0
p2_wins = 0
for key, val in res_1.items():
    if val['wins'] > 0:
        p1_wins += val['wins'] * res_2[key-1]['continues']

for key, val in res_2.items():
    if val['wins'] > 0:
        p2_wins += val['wins'] * res_1[key]['continues']

print(p1_wins)
print(p2_wins)
