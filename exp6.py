def find_min_operations(dimensions):
   

    total_matrices = len(dimensions) - 1

    cost_table = [[0] * (total_matrices + 1) for _ in range(total_matrices + 1)]
    split_table = [[0] * (total_matrices + 1) for _ in range(total_matrices + 1)]

    for chain_size in range(2, total_matrices + 1):

        for start in range(1, total_matrices - chain_size + 2):

            end = start + chain_size - 1
            cost_table[start][end] = float("inf")

            for split in range(start, end):

                current_cost = (
                    cost_table[start][split]
                    + cost_table[split + 1][end]
                    + dimensions[start - 1] * dimensions[split] * dimensions[end]
                )

                if current_cost < cost_table[start][end]:
                    cost_table[start][end] = current_cost
                    split_table[start][end] = split

    return cost_table, split_table


def display_order(split_table, left, right):

    if left == right:
        return f"M{left}"

    mid = split_table[left][right]

    first = display_order(split_table, left, mid)
    second = display_order(split_table, mid + 1, right)

    return f"({first} × {second})"


def show_cost_matrix(cost_table, matrix_count):

    print("\nMinimum Cost DP Table\n")

    print(f'{"":>8}', end="")
    for col in range(1, matrix_count + 1):
        print(f"M{col:>8}", end="")
    print()

    for row in range(1, matrix_count + 1):

        print(f"M{row:<6}", end="")

        for col in range(1, matrix_count + 1):

            if col < row:
                print(f'{"-":>9}', end="")
            else:
                print(f"{cost_table[row][col]:>9}", end="")

        print()




matrix_dimensions = [15, 20, 35, 10, 25]

matrix_count = len(matrix_dimensions) - 1

print("Matrix Sizes\n")

for index in range(matrix_count):
    print(f"M{index + 1}: {matrix_dimensions[index]} × {matrix_dimensions[index + 1]}")

cost, split = find_min_operations(matrix_dimensions)

print("\nLeast Scalar Multiplications :", cost[1][matrix_count])

print("Best Multiplication Order   :", display_order(split, 1, matrix_count))

show_cost_matrix(cost, matrix_count)
