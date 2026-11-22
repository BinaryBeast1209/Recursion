# ================================
# TARGET TRACKER LAB (ACP)
# Project Code: ACPDSCM7L6
# ================================
# Topics:
# Slices and their sums | Left-right balance
# Equilibrium point | Subarray window | Target sum search

print("================================")
print("TARGET TRACKER LAB")
print("================================")

# ------------------------------------------------
# PART 1 — SLICES AND THEIR SUMS
# ------------------------------------------------
sample = [1, 3, 5, 2, 2]
print("\nPART 1: Slices and Balance Analysis")
print("Sample Array:", sample)
for i in range(len(sample)):
    left_part = sample[:i]
    right_part = sample[i + 1:]
    l_sum = sum(left_part)
    r_sum = sum(right_part)
    status = "BALANCED" if l_sum == r_sum else "unbalanced"
    print(f"Index {i} (val={sample[i]}): Left {left_part} = {l_sum} | Right {right_part} = {r_sum} -> {status}")

# ------------------------------------------------
# PART 2 — EQUILIBRIUM INDEX
# ------------------------------------------------
def find_eq_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1

print("\nPART 2: Equilibrium Index Search")
print(f"Equilibrium index for [1, 3, 5, 2, 2]: {find_eq_index([1, 3, 5, 2, 2])}")
print(f"Equilibrium index for [2, 4, 2]: {find_eq_index([2, 4, 2])}")
print(f"Equilibrium index for [3, 1, 2] (no balance): {find_eq_index([3, 1, 2])}")

# ------------------------------------------------
# PART 3 — EQUILIBRIUM VALUE
# ------------------------------------------------
def find_eq_value(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return arr[i]
    return -1

print("\nPART 3: Equilibrium Value Search")
print(f"Equilibrium value for [1, 1, 99, 1, 1]: {find_eq_value([1, 1, 99, 1, 1])}")
print(f"Equilibrium value for [1, 3, 5, 2, 2]: {find_eq_value([1, 3, 5, 2, 2])}")

# ------------------------------------------------
# PART 4 — SUBARRAY WINDOW & TARGET SUM SEARCH
# ------------------------------------------------
def find_window(arr, k, target):
    # k is window size
    for i in range(len(arr) - k + 1):
        window = arr[i:i + k]
        if sum(window) == target:
            return i
    return -1

win_arr = [0, 0, 1, 1, 0]
print("\nPART 4: Fixed-Size Window Search")
print(f"Array: {win_arr}, Window size k=2, Target=2")
print(f"First matching window start index: {find_window(win_arr, 2, 2)}")

# ------------------------------------------------
# PART 5 — BONUS: O(n) SLIDING WINDOW OPTIMISATION
# ------------------------------------------------
def find_window_optimized(arr, k, target):
    if len(arr) < k:
        return -1
    curr_sum = sum(arr[:k])
    if curr_sum == target:
        return 0

    for i in range(1, len(arr) - k + 1):
        curr_sum += arr[i + k - 1] - arr[i - 1]
        if curr_sum == target:
            return i
    return -1

print("\nPART 5: Optimized O(n) Sliding Window")
test_window = [0, 0, 0, 1, 1, 1]
print(f"Array: {test_window}, k=3, Target=3")
print(f"Matched start index: {find_window_optimized(test_window, 3, 3)}")

# FINAL SUMMARY
print("\n================================")
print("TARGET TRACKER LAB SUMMARY")
print("================================")
print("1. Equilibrium index is where sum(arr[:i]) == sum(arr[i+1:]).")
print("2. The pivot element at index i is excluded from both sums.")
print("3. Fixed window of size k slides across len(arr) - k + 1 positions.")
print("4. Target sum search returns the starting index of the first match.")
print("5. O(n) sliding window updates running sum by adding new and subtracting old elements.")
print("================================")
