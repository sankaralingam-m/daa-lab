import random
import time
import sys

sys.setrecursionlimit(20000)

count = 0


def split_array(data, start, end):

    global count

    pivot_value = data[end]

    position = start - 1

    for index in range(start, end):

        count += 1

        if data[index] <= pivot_value:

            position += 1

            data[position], data[index] = data[index], data[position]

    data[position + 1], data[end] = data[end], data[position + 1]

    return position + 1



def normal_quick_sort(data, start, end):

    if start < end:

        middle = split_array(data, start, end)

        normal_quick_sort(data, start, middle - 1)

        normal_quick_sort(data, middle + 1, end)



def random_quick_sort(data, start, end):

    if start < end:

        selected = random.randint(start, end)

        data[selected], data[end] = data[end], data[selected]

        middle = split_array(data, start, end)

        random_quick_sort(data, start, middle - 1)

        random_quick_sort(data, middle + 1, end)



def evaluate(method, numbers):

    global count

    copied = numbers[:]

    count = 0

    begin = time.perf_counter()

    method(copied, 0, len(copied) - 1)

    duration = (time.perf_counter() - begin) * 1000

    return count, duration



size = 5000


inputs = {

    "Unordered": [random.randint(1, 100000) for _ in range(size)],

    "Ascending": list(range(size)),

    "Descending": list(range(size, 0, -1)),

    "Almost Sorted": list(range(size))

}


almost = inputs["Almost Sorted"]


for _ in range(size // 20):

    first = random.randint(0, size - 1)

    second = random.randint(0, size - 1)

    almost[first], almost[second] = almost[second], almost[first]



print(f"{'Data Type':<18} {'Normal Comp':>12} {'Normal Time':>14} {'Random Comp':>14} {'Random Time':>14}")

print("-" * 75)


for label, values in inputs.items():

    normal_count, normal_time = evaluate(normal_quick_sort, values)

    random_count, random_time = evaluate(random_quick_sort, values)

    print(
        f"{label:<18} "
        f"{normal_count:>12} "
        f"{normal_time:>14.2f} "
        f"{random_count:>14} "
        f"{random_time:>14.2f}"
    )
