# ================================
# ARRAY ENERGY TRACKER (ACP)
# Project Code: ACPDSCM7L5
# ================================
# Topics:
# Subarrays | Drag of Negatives
# Running Sum with Reset | Max-So-Far Tracker
# Kadane's Algorithm

print("================================")
print("ARRAY ENERGY TRACKER (KADANE'S ALGORITHM)")
print("================================")

# ------------------------------------------------
# PART 1 — WHAT IS A SUBARRAY?
# ------------------------------------------------
sample = [-2, 3, -1, 4]
print("\nPART 1: Subarray Exploration")
print("Array:", sample)
print("A subarray is a contiguous slice of consecutive elements.")
print("Contiguous subarrays for [-2, 3, -1, 4]:")
for length in range(1, len(sample) + 1):
    for start in range(len(sample) - length + 1):
        sub = sample[start:start + length]
        print(f"  {sub} -> sum = {sum(sub)}")

# ------------------------------------------------
# PART 2 — KADANE'S ALGORITHM IMPLEMENTATION
# ------------------------------------------------
# Running sum with reset: if current < 0: current = x else: current = current + x
# Max-so-far tracker: if current > best: best = current
def kadane(arr):
    if not arr:
        return 0
    current = best = arr[0]
    for x in arr[1:]:
        if current < 0:
            current = x
        else:
            current = current + x
        if current > best:
            best = current
    return best

print("\nPART 2: Basic Kadane's Algorithm")
print("Array:", sample)
print("Max Subarray Sum:", kadane(sample))

# ------------------------------------------------
# PART 3 — EXTENDED KADANE'S (TRACKING INDICES)
# ------------------------------------------------
def kadane_with_indices(arr):
    if not arr:
        return 0, -1, -1
    best = arr[0]
    current = arr[0]
    start = end = temp_start = 0

    for i in range(1, len(arr)):
        if current < 0:
            current = arr[i]
            temp_start = i
        else:
            current += arr[i]

        if current > best:
            best = current
            start = temp_start
            end = i

    return best, start, end

best_sum, s_idx, e_idx = kadane_with_indices(sample)
print("\nPART 3: Kadane with Best Subarray Slices")
print("Best Subarray:", sample[s_idx:e_idx + 1])
print(f"Max Sum: {best_sum} (from index {s_idx} to {e_idx})")

# ------------------------------------------------
# PART 4 — TESTING DIVERSE SCENARIOS
# ------------------------------------------------
test_cases = [
    ("Peak in Middle [-1, 5, -1]", [-1, 5, -1]),
    ("Front-Loaded [3, 3, 3, -10]", [3, 3, 3, -10]),
    ("Big Reset [-100, 4, 3]", [-100, 4, 3]),
    ("All Positive [1, 2, 3, 4]", [1, 2, 3, 4]),
    ("All Negative [-5, -2, -8, -1]", [-5, -2, -8, -1]),
    ("LeetCode #53 Classic [-2, 1, -3, 4, -1, 2, 1, -5, 4]", [-2, 1, -3, 4, -1, 2, 1, -5, 4])
]

print("\nPART 4: Diverse Scenario Tests")
for label, arr in test_cases:
    ans, start, end = kadane_with_indices(arr)
    print(f"{label}:")
    print(f"  Best sum = {ans} | Slice = {arr[start:end + 1]}")

# FINAL SUMMARY
print("\n================================")
print("ARRAY ENERGY TRACKER SUMMARY")
print("================================")
print("1. Subarrays are contiguous slices of an array.")
print("2. Negative running sum is a drag that degrades future subarrays.")
print("3. Reset rule: if current < 0, reset current = x (start fresh).")
print("4. Ratchet rule: if current > best, update best.")
print("5. Initialising to arr[0] correctly handles all-negative arrays.")
print("6. Kadane's algorithm runs in O(n) time and O(1) extra space.")
print("================================")
