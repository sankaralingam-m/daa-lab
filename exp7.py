def valid_position(layout, current_row, current_col):

    for r in range(current_row):

        c = layout[r]

        if c == current_col:
            return False

        if abs(current_row - r) == abs(current_col - c):
            return False

    return True


def queens_solver(size):

    arrangement = [-1] * size
    answer_list = []
    search_steps = [0]

    def search(row):

        if row == size:
            answer_list.append(arrangement[:])
            return

        for column in range(size):

            if valid_position(arrangement, row, column):

                arrangement[row] = column
                search(row + 1)
                arrangement[row] = -1

        search_steps[0] += 1

    search(0)

    return answer_list, search_steps[0]


def print_chessboard(solution, size):

    border = "+" + "----+" * size

    print(border)

    for r in range(size):

        print("|", end="")

        for c in range(size):

            symbol = "Q" if solution[r] == c else "."

            print(f" {symbol} |", end="")

        print()
        print(border)


board_sizes = [4, 5, 7]

for board_size in board_sizes:

    result, steps = queens_solver(board_size)

    print(f"\nBoard Size : {board_size}")
    print(f"Solutions  : {len(result)}")
    print(f"Searches   : {steps}")

    if board_size == 4:

        print("\nPossible Arrangements:\n")

        for number, layout in enumerate(result, start=1):

            print(f"Arrangement {number}: {layout}")
            print_chessboard(layout, board_size)
            print()
