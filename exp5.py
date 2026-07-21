import random

check_count = 0


def divide_conquer_min_max(numbers, left, right):
    global check_count

    if left == right:
        return numbers[left], numbers[left]

    if right == left + 1:
        check_count += 1

        if numbers[left] < numbers[right]:
            return numbers[left], numbers[right]

        return numbers[right], numbers[left]

    middle = (left + right) // 2

    left_min, left_max = divide_conquer_min_max(numbers, left, middle)
    right_min, right_max = divide_conquer_min_max(numbers, middle + 1, right)

    check_count += 1
    smallest = left_min if left_min < right_min else right_min

    check_count += 1
    largest = left_max if left_max > right_max else right_max

    return smallest, largest


def linear_min_max(numbers):

    smallest = numbers[0]
    largest = numbers[0]

    checks = 0

    for value in numbers[1:]:

        checks += 1
        if value < smallest:
            smallest = value

        checks += 1
        if value > largest:
            largest = value

    return smallest, largest, checks


sample_numbers = [12, 45, 8, 63, 21, 90, 34, 56, 17, 72]

check_count = 0

minimum, maximum = divide_conquer_min_max(
    sample_numbers,
    0,
    len(sample_numbers) - 1
)

dc_checks = check_count

_, _, linear_checks = linear_min_max(sample_numbers)

print("Sample Array")
print(sample_numbers)

print(f"\nMinimum Value : {minimum}")
print(f"Maximum Value : {maximum}")

print(f"\nDivide & Conquer Checks : {dc_checks}")
print(f"Linear Search Checks    : {linear_checks}")

print("\nPerformance Comparison")
print("=" * 58)
print(f'{"Size":<10}{"D&C Checks":>15}{"Linear Checks":>18}{"Expected":>15}')
print("-" * 58)

for size in [20, 200, 2000, 20000]:

    values = [random.randint(100, 50000) for _ in range(size)]

    check_count = 0

    divide_conquer_min_max(values, 0, len(values) - 1)
    dc_result = check_count

    _, _, linear_result = linear_min_max(values)

    expected = (3 * size) // 2 - 2

    print(
        f"{size:<10}"
        f"{dc_result:>15}"
        f"{linear_result:>18}"
        f"{expected:>15}"
    )