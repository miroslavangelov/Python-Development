chess_board = list()
is_king_safe = True

for i in range(0, 8):
    board_row = input().split(' ')
    chess_board.append(board_row)

for i in range(0, len(chess_board)):
    current_row = chess_board[i]
    for j in range(0, len(current_row)):
        current_cell = current_row[j]

        if current_cell == 'Q':
            king_captured = False

            # start moving right
            for k in range(j + 1, len(current_row)):
                if current_row[k] == 'Q':
                    break

                if current_row[k] == 'K':
                    king_captured = True
                    print(f'[{i}, {j}]')
                    is_king_safe = False
                    break
            if is_king_safe:
                continue

            # start moving left
            for k in range(j - 1, 0, -1):
                if current_row[k] == 'Q':
                    break

                if current_row[k] == 'K':
                    king_captured = True
                    print(f'[{i}, {j}]')
                    is_king_safe = False
                    break
            if king_captured:
                continue

            # start moving up
            for k in range(i - 1, 0, -1):
                current_row_up = chess_board[k]
                if current_row_up[j] == 'Q':
                    break

                if current_row_up[j] == 'K':
                    king_captured = True
                    print(f'[{i}, {j}]')
                    is_king_safe = False
                    break
            if king_captured:
                continue

            # start moving down
            for k in range(i + 1, len(chess_board)):
                current_row_down = chess_board[k]
                if current_row_down[j] == 'Q':
                    break

                if current_row_down[j] == 'K':
                    king_captured = True
                    print(f'[{i}, {j}]')
                    is_king_safe = False
                    break
            if king_captured:
                continue

            # start moving right down
            index = j
            for k in range(i + 1, len(chess_board)):
                index += 1
                current_row_right_down = chess_board[k]
                if index >= len(current_row_right_down) or current_row_right_down[index] == 'Q':
                    break

                if current_row_right_down[index] == 'K':
                    king_captured = True
                    print(f'[{i}, {j}]')
                    is_king_safe = False
                    break
            if king_captured:
                continue

            # start moving right up
            index = j
            for k in range(i - 1, 0, -1):
                index += 1
                current_row_right_up = chess_board[k]
                if index >= len(current_row_right_up) or current_row_right_up[index] == 'Q':
                    break

                if current_row_right_up[index] == 'K':
                    king_captured = True
                    print(f'[{i}, {j}]')
                    is_king_safe = False
                    break
            if king_captured:
                continue

            # start moving left down
            index = j
            for k in range(i + 1, len(chess_board)):
                index -= 1
                current_row_left_down = chess_board[k]
                if index < 0 or current_row_left_down[index] == 'Q':
                    break

                if current_row_left_down[index] == 'K':
                    king_captured = True
                    print(f'[{i}, {j}]')
                    is_king_safe = False
                    break
            if king_captured:
                continue

            # start moving left up
            index = j
            for k in range(i - 1, 0, -1):
                index -= 1
                current_row_left_up = chess_board[k]
                if index < 0 or current_row_left_up[index] == 'Q':
                    break

                if current_row_left_up[index] == 'K':
                    king_captured = True
                    print(f'[{i}, {j}]')
                    is_king_safe = False
                    break

if is_king_safe:
    print('The king is safe!')
