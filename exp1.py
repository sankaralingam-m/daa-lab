import time
import random


def interpolation_search(data, key):
    """
    Interpolation Search
    Average Time: O(log log n)
    Worst Time: O(n)
    Space: O(1)
    """

    left = 0
    right = len(data) - 1
    checks = 0

    while left <= right and left < len(data) and data[left] <= key <= data[right]:
        checks += 1

        if left == right:
            if data[left] == key:
                return left, checks
            return -1, checks

        # Prevent division by zero
        if data[left] == data[right]:
            break

        position = left + (
            (key - data[left]) * (right - left)
        ) // (data[right] - data[left])

        if data[position] == key:
            return position, checks
        elif data[position] < key:
            left = position + 1
        else:
            right = position - 1

    return -1, checks


def binary_search(data, key):
    """Binary Search Algorithm"""

    left = 0
    right = len(data) - 1
    checks = 0

    while left <= right:
        checks += 1
        middle = (left + right) // 2

        if data[middle] == key:
            return middle, checks
        elif data[middle] < key:
            left = middle + 1
        else:
            right = middle - 1

    return -1, checks


def compare_performance():
    test_sizes = [1000, 5000, 10000, 50000, 100000]

    print("\nPerformance Comparison")
    print("=" * 78)
    print(
        f"{'Array Size':<12}"
        f"{'Interpolation(ms)':>20}"
        f"{'Binary(ms)':>15}"
        f"{'IS Checks':>15}"
        f"{'BS Checks':>15}"
    )
    print("-" * 78)

    for size in test_sizes:
        numbers = sorted(random.sample(range(size * 10), size))
        key = random.choice(numbers)

        # Interpolation Search
        start = time.perf_counter()
        for _ in range(100):
            _, is_checks = interpolation_search(numbers, key)
        interpolation_time = (time.perf_counter() - start) * 10

        # Binary Search
        start = time.perf_counter()
        for _ in range(100):
            _, bs_checks = binary_search(numbers, key)
        binary_time = (time.perf_counter() - start) * 10

        print(
            f"{size:<12}"
            f"{interpolation_time:>20.4f}"
            f"{binary_time:>15.4f}"
            f"{is_checks:>15}"
            f"{bs_checks:>15}"
        )


def main():
    sample_array = [4, 9, 13, 21, 28, 36, 45, 57, 68, 79, 91, 104, 118]
    target = 57

    index, comparisons = interpolation_search(sample_array, target)

    print("Interpolation Search Demo")
    print("-" * 30)
    print("Array :", sample_array)
    print("Target:", target)

    if index != -1:
        print(f"Element found at index {index}")
    else:
        print("Element not found")

    print(f"Comparisons made: {comparisons}")

    compare_performance()


if __name__ == "__main__":
    main()