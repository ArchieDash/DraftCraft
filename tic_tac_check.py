def isSolved(board):
    board = np.array(board)
    if np.isin(0, board):
        return -1
    for row in board:
        if np.unique(row).size == 1 and np.unique(row) != 0:
            return np.unique(row)[0]
    for column in board.T:
        if np.unique(column).size == 1 and np.unique(column) != 0:
            return np.unique(column)[0]
    if np.unique(board.diagonal()).size == 1 and np.unique(board.diagonal()) != 0:
        return np.unique(board.diagonal())[0]
    elif np.unique(np.fliplr(board).diagonal()).size == 1 and np.unique(np.fliplr(board).diagonal()) != 0:
        return np.unique(np.fliplr(board).diagonal())[0]
    else:
        return 0

print(isSolved(board))
