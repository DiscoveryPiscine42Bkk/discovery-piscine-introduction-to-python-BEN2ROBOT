def is_in_check(board_str):
    board = board_str.splitlines()

    if not board or not all(len(row) == len(board) for row in board):
        return

    size = len(board)
    king_found = False

    for i in range(size):
        for j in range(size):
            if board[i][j] == 'K':
                king_x, king_y = i, j
                king_found = True
                break
        if king_found:
            break
    else:
        return

    directions = {
        'Q': [(-1, 0), (1, 0), (0, -1), (0, 1),  (-1, -1), (1, 1), (-1, 1), (1, -1)],
        'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],
        'B': [(-1, -1), (1, 1), (-1, 1), (1, -1)],
        'P': [(1, -1), (1, 1)],
    }

    for piece, dirs in directions.items():
        for dx, dy in dirs:
            x, y = king_x + dx, king_y + dy
            while 0 <= x < size and 0 <= y < size:
                cell = board[x][y]
                if cell == '.':
                    x += dx
                    y += dy
                    continue
                if cell == piece:
                    print("Success")
                    return
                break

    print("Fail")
