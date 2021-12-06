def line_to_board_row(line):
    return [int(val) for val in line.strip().replace('  ', ' ').split(' ')]


def play_board(board, number):
    played_board = []
    for row in board:
        row = [x if x != number else -1 for x in row]
        played_board.append(row)
    return played_board


def check_board(board):
    board_t = list(map(list, zip(*board)))
    for row in board:
        if sum(row) == -5:
            return True
    for col in board_t:
        if sum(col) == -5:
            return True
    return False


def board_score(board):
    score = 0
    for row in board:
        score += sum([x if x != -1 else 0 for x in row])
    return score


with open('./input', encoding='utf8') as file:
    picked_numbers = [int(val) for val in file.readline().split(',')]
    boards = []
    while file.readline():
        boards.append([
            line_to_board_row(file.readline()),
            line_to_board_row(file.readline()),
            line_to_board_row(file.readline()),
            line_to_board_row(file.readline()),
            line_to_board_row(file.readline()),
        ])

winner = None
for number in picked_numbers:
    for i, board in enumerate(boards):
        boards[i] = play_board(board, number)
        if check_board(boards[i]):
            winner = boards[i]
            break
    if winner is not None:
        break

score = board_score(winner)
print(score * number)
