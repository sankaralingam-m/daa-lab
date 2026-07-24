def simple_fit(values, limit=1.0):

    available = []
    packed_bins = []

    for value in values:

        inserted = False

        for index, remaining in enumerate(available):

            if remaining >= value:

                available[index] -= value
                packed_bins[index].append(value)
                inserted = True
                break

        if not inserted:

            available.append(limit - value)
            packed_bins.append([value])

    return packed_bins


def decreasing_simple_fit(values, limit=1.0):

    ordered_values = sorted(values, reverse=True)

    return simple_fit(ordered_values, limit)


def decreasing_best_fit(values, limit=1.0):

    ordered_values = sorted(values, reverse=True)

    free_space = []
    packed_bins = []

    for value in ordered_values:

        selected = -1
        smallest_gap = float("inf")

        for index, remaining in enumerate(free_space):

            gap = remaining - value

            if remaining >= value and gap < smallest_gap:
                smallest_gap = gap
                selected = index

        if selected != -1:

            free_space[selected] -= value
            packed_bins[selected].append(value)

        else:

            free_space.append(limit - value)
            packed_bins.append([value])

    return packed_bins


def show_packing(name, groups):

    print(f"\n{name}: {len(groups)} containers")

    for number, group in enumerate(groups, start=1):

        total = sum(group)

        visual = "*" * int(total * 20)

        print(
            f" Container {number}: {[round(v, 1) for v in group]}"
            f" | Load: {total:.1f} [{visual:<20}]"
        )


objects = [0.6, 0.2, 0.8, 0.4, 0.9, 0.3, 0.7, 0.5, 0.1, 0.6]

container_size = 1.0

minimum_required = int(-(-sum(objects) // container_size))

print("Object Sizes:", objects)
print("Container Capacity:", container_size)
print("Total Size:", sum(objects))
print("Minimum Containers Needed:", minimum_required)


normal_fit = simple_fit(objects, container_size)
sorted_fit = decreasing_simple_fit(objects, container_size)
optimal_fit = decreasing_best_fit(objects, container_size)


show_packing("Simple First Fit", normal_fit)

show_packing("Decreasing First Fit", sorted_fit)

show_packing("Decreasing Best Fit", optimal_fit)


print(
    f"\nResult Summary: Minimum={minimum_required}, "
    f"First Fit={len(normal_fit)}, "
    f"FFD={len(sorted_fit)}, "
    f"BFD={len(optimal_fit)}"
)
