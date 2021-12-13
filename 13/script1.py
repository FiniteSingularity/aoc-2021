def fold_along_y(page, fold_row):
    folded_page = page[0:fold_row]
    past_fold = page[-1:fold_row:-1]
    len_diff = len(folded_page) - len(past_fold)
    if(len_diff > 0):
        # add rows to beginning of past_fold if too small
        past_fold = [ [0] * len(past_fold[0]) for _ in range(len_diff)] + past_fold
    else:
        # add rows to beginning of folded_page if past_fold too big
        folded_page = [ [0] * len(folded_page[0]) for _ in range(-len_diff)] + folded_page
    for i, row in enumerate(past_fold):
        for j, val in enumerate(row):
            if val == 1:
                folded_page[i][j] = 1
    return folded_page


# to fold_along_x using the fold_along_y algorithm, simply
# transpose the list of lists, fold along y, then transpose
# the result back.
def fold_along_x(page, fold_row):
    # fold along y for the transpose version of page
    folded_page = fold_along_y([list(x) for x in zip(*page)], fold_row)
    # return the transposed result to go back to x
    return [list(x) for x in zip(*folded_page)]

dots = []
folds = []
rows = 0
cols = 0
with open('./input', encoding='utf8') as file:
    while True:
        line=file.readline()
        if line.strip() == '':
            break
        dots.append([int(val) for val in line.strip().split(',')])
        cols = max(cols, dots[-1][0]+1)
        rows = max(rows, dots[-1][1]+1)
    while True:
        line=file.readline()
        if line=='':
            break
        fold = line.strip().split(' ')[2].split('=')
        folds.append({'along': fold[0], 'coord': int(fold[1])})

page = [ [0] * cols for _ in range(rows)]

for dot in dots:
    page[dot[1]][dot[0]] = 1

if(folds[0]['along'] == 'y'):
    folded_page = fold_along_y(page, folds[0]['coord'])
else:
    folded_page = fold_along_x(page, folds[0]['coord'])

count = 0
for row in folded_page:
    count += sum(row)
print(count)