def calc_num_chips(waffles):
    num_chips = 0
    for row in waffles:
        num_chips += sum([1 for x in row if x == '@'])
    return num_chips

def horizontal_cut(waffles, chips_per_cell):

    cells = []
    start = 0
    chips_now = 0
    for i in xrange(len(waffles)):
        chips_now += sum([1 for x in waffles[i] if x =='@'])
        # impossible case
        if chips_now > chips_per_cell:
            return []

        elif chips_now == chips_per_cell:
            cells.append(waffles[start:i+1])
            start = i + 1
            chips_now = 0
    return cells

def calc_col_chips(cell, idx):
    num_chips = 0
    for r in cell:
        if r[idx] == '@':
            num_chips += 1
    return num_chips

def vertical_cut(cells, V, chips_per_cell):
    start = 0
    chips_now = [0] * len(cells)
    num_col = len(cells[0][0])
    num_cuts = 0

    for col in xrange(num_col):
        for i in xrange(len(cells)):
            chips_now[i] += calc_col_chips(cells[i], col)
            if chips_now[i] > chips_per_cell:
                return False

        allMatched = True
        for i in xrange(len(cells)):
            if chips_now[i] != chips_per_cell:
                allMatched = False
                break
        if allMatched:
            num_cuts += 1
            chips_now = [0] * len(cells)
    
    return (V + 1) == num_cuts

def waffle_choppers(waffles, H, V):
    num_chips = calc_num_chips(waffles)
    if num_chips == 0:
        return 'POSSIBLE'
    num_cells = (H + 1) * (V + 1)
    if num_chips % num_cells != 0:
        return 'IMPOSSIBLE'

    h_cells = horizontal_cut(waffles, num_chips / (H + 1))
    if len(h_cells) == 0:
        return 'IMPOSSIBLE'
    
    if vertical_cut(h_cells, V, num_chips / num_cells):
        return 'POSSIBLE'
    return 'IMPOSSIBLE'

def __main__():
    t = int(raw_input())
    for i in xrange(t):
        R, C, H, V = [int(x) for x in raw_input().split(' ')]
        waffles = []
        for r in xrange(R):
            waffles.append(list(raw_input()))

        print 'Case #{0}: {1}'.format(i + 1, waffle_choppers(waffles, H, V))

if __name__ == '__main__':
    __main__()
