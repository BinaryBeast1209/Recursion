# ================================
# BINARY STREAK TRACKER (ACP)
# Project Code: ACPDSCM7L4
# ================================
# Topics:
# Binary arrays | Streak counter with reset | Best-streak tracker
# Same-direction two pointers | Write-pointer pattern

print("================================")
print("BINARY STREAK TRACKER")
print("================================")

# ------------------------------------------------
# PART 1 — BINARY ARRAY ANALYSIS
# ------------------------------------------------
binary_data = [1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1]
ones_count = binary_data.count(1)
zeros_count = binary_data.count(0)
transitions = sum(1 for i in range(1, len(binary_data)) if binary_data[i] != binary_data[i - 1])

print("\nPART 1: Binary Array Analysis")
print("Array:", binary_data)
print("Count of 1s:", ones_count, "| Count of 0s:", zeros_count)
print("Transitions (value changes):", transitions)

# ------------------------------------------------
# PART 2 — MAX CONSECUTIVE ONES
# ------------------------------------------------
def max_consecutive_ones(arr):
    streak = 0
    best = 0
    for x in arr:
        streak = streak + 1 if x else 0
        best = max(best, streak)
    return best

print("\nPART 2: Max Consecutive Ones")
print("Array:", binary_data)
print("Longest run of 1s:", max_consecutive_ones(binary_data))

# ------------------------------------------------
# PART 3 — MAX CONSECUTIVE ZEROS
# ------------------------------------------------
def max_consecutive_zeros(arr):
    streak = 0
    best = 0
    for x in arr:
        streak = streak + 1 if not x else 0
        best = max(best, streak)
    return best

print("\nPART 3: Max Consecutive Zeros")
print("Array:", binary_data)
print("Longest run of 0s:", max_consecutive_zeros(binary_data))

# ------------------------------------------------
# PART 4 — GENERIC MAX STREAK
# ------------------------------------------------
def max_streak(arr, target):
    streak = 0
    best = 0
    for x in arr:
        streak = streak + 1 if x == target else 0
        best = max(best, streak)
    return best

print("\nPART 4: Generic Max Streak")
print("Max streak of 1:", max_streak(binary_data, 1))
print("Max streak of 0:", max_streak(binary_data, 0))

# ------------------------------------------------
# PART 5 — MOVE ZEROS TO END (SAME-DIRECTION WRITE POINTER)
# ------------------------------------------------
def move_zeros_to_end(arr):
    # In-place write pointer pattern
    result = list(arr)
    write = 0
    for x in result:
        if x != 0:
            result[write] = x
            write += 1
    result[write:] = [0] * (len(result) - write)
    return result

sample_arr = [0, 3, 0, 5, 0, 7]
print("\nPART 5: Move Zeros to End (Write Pointer)")
print("Original Array:", sample_arr)
print("After Moving Zeros:", move_zeros_to_end(sample_arr))

# Edge cases check
print("\nEdge Case Tests:")
print("All zeros [0, 0, 0]:", move_zeros_to_end([0, 0, 0]))
print("All ones [1, 1, 1]:", move_zeros_to_end([1, 1, 1]))

# FINAL SUMMARY
print("\n================================")
print("BINARY STREAK TRACKER SUMMARY")
print("================================")
print("1. Binary arrays contain only 0s and 1s.")
print("2. Streak counter: streak = streak + 1 if x else 0.")
print("3. Best tracker uses best = max(best, streak) to store highest streak.")
print("4. Same-direction write pointer collects non-zeros in O(n) time.")
print("5. Slice fill replaces remaining tail slots with zeros.")
print("================================")
