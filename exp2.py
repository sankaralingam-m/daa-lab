import random


def naive_search(source_text, search_key):
    text_len = len(source_text)
    pattern_len = len(search_key)

    positions = []
    checks = 0

    for start in range(text_len - pattern_len + 1):
        index = 0

        while index < pattern_len:
            checks += 1

            if source_text[start + index] != search_key[index]:
                break

            index += 1

        if index == pattern_len:
            positions.append(start)

    return positions, checks


def build_lps(search_key):
    pattern_len = len(search_key)
    lps = [0] * pattern_len

    prefix = 0
    current = 1

    while current < pattern_len:
        if search_key[current] == search_key[prefix]:
            prefix += 1
            lps[current] = prefix
            current += 1
        elif prefix != 0:
            prefix = lps[prefix - 1]
        else:
            lps[current] = 0
            current += 1

    return lps


def kmp_search(source_text, search_key):
    text_len = len(source_text)
    pattern_len = len(search_key)

    lps = build_lps(search_key)

    positions = []
    checks = 0

    text_index = 0
    pattern_index = 0

    while text_index < text_len:
        checks += 1

        if source_text[text_index] == search_key[pattern_index]:
            text_index += 1
            pattern_index += 1

            if pattern_index == pattern_len:
                positions.append(text_index - pattern_index)
                pattern_index = lps[pattern_index - 1]

        elif pattern_index != 0:
            pattern_index = lps[pattern_index - 1]

        else:
            text_index += 1

    return positions, checks


def rabin_karp(source_text, search_key, prime=101):
    text_len = len(source_text)
    pattern_len = len(search_key)

    base = 256
    highest_power = pow(base, pattern_len - 1, prime)

    pattern_hash = 0
    text_hash = 0

    positions = []
    checks = 0

    for i in range(pattern_len):
        pattern_hash = (base * pattern_hash + ord(search_key[i])) % prime
        text_hash = (base * text_hash + ord(source_text[i])) % prime

    for start in range(text_len - pattern_len + 1):

        if pattern_hash == text_hash:
            for j in range(pattern_len):
                checks += 1

                if source_text[start + j] != search_key[j]:
                    break
            else:
                positions.append(start)

        if start < text_len - pattern_len:
            text_hash = (
                base * (text_hash - ord(source_text[start]) * highest_power)
                + ord(source_text[start + pattern_len])
            ) % prime

            if text_hash < 0:
                text_hash += prime

    return positions, checks


# ------------------ Main Program ------------------

source_text = "COMPUTERSCIENCECOMPUTER"
search_key = "COM"

print("Source Text :", source_text)
print("Search Key  :", search_key)

result1, checks1 = naive_search(source_text, search_key)
result2, checks2 = kmp_search(source_text, search_key)
result3, checks3 = rabin_karp(source_text, search_key)

print("\nSearch Results")
print("-" * 45)
print(f"Naive Search      : {result1} | Checks = {checks1}")
print(f"KMP Search        : {result2} | Checks = {checks2}")
print(f"Rabin-Karp Search : {result3} | Checks = {checks3}")

# ---------------- Performance Comparison ----------------

large_text = "".join(random.choices("ABCDE", k=12000))
test_patterns = ["ABC", "BCDE", "ABCDE", "CDEAB"]

print("\nPerformance Comparison")
print("=" * 60)
print(f'{"Pattern":<12}{"Naive":>12}{"KMP":>12}{"Rabin-Karp":>18}')
print("-" * 60)

for pattern in test_patterns:
    _, naive_checks = naive_search(large_text, pattern)
    _, kmp_checks = kmp_search(large_text, pattern)
    _, rk_checks = rabin_karp(large_text, pattern)

    print(
        f"{pattern:<12}"
        f"{naive_checks:>12}"
        f"{kmp_checks:>12}"
        f"{rk_checks:>18}"
    )