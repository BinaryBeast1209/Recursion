# subarray_sum.py / 02_subarray_sum.py
# Module 7: Array - Lesson 6: Array Problems 4
# Activity 2: SubArraySum
# Description: Finds a contiguous subarray whose sum equals a specified target sum using sliding window.

def win_sum(n):
    """
    Finds the starting index of the first window of size n that sums to target n.
    """
    arr = [0] * n + [1] * n
    size = len(arr)
    for i in range(size - n + 1):
        curr_sum = 0
        for j in range(i, i + n):
            curr_sum += arr[j]
        if curr_sum == n:
            return i
    return -1


def find_subarray_with_target_sum(arr, target):
    """
    Finds contiguous subarray [start, end] (1-based indices) that sums to target.
    Uses O(n) variable-size sliding window technique (two pointers).
    """
    curr_sum = 0
    start = 0
    for end in range(len(arr)):
        curr_sum += arr[end]
        while curr_sum > target and start < end:
            curr_sum -= arr[start]
            start += 1
        if curr_sum == target:
            return start, end, arr[start:end + 1]
    return -1, -1, []


def run_demo():
    print("=" * 60)
    print("       ARRAY PROBLEMS 4 - SUBARRAY TARGET SUM")
    print("=" * 60)

    test_cases = [
        ([1, 2, 3, 7, 5], 12),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15),
        ([5, 3, 4, 1, 2, 7], 7),
        ([1, 4, 0, 0, 3, 10, 5], 7)
    ]

    for idx, (arr, target) in enumerate(test_cases, 1):
        s, e, sub = find_subarray_with_target_sum(arr, target)
        print(f"Test Case {idx}:")
        print(f"  Array: {arr}, Target: {target}")
        if s != -1:
            print(f"  Subarray found from index {s} to {e}: {sub} (Sum = {sum(sub)})")
        else:
            print("  No subarray found with target sum.")
        print("-" * 55)

    print("\n--- Interactive Subarray Sum Search ---")
    user_input = input("Enter array numbers separated by spaces (e.g. 1 2 3 7 5) or press Enter for default: ")
    if user_input.strip():
        try:
            custom_arr = [int(x) for x in user_input.split()]
            t_input = input("Enter target sum: ")
            target = int(t_input)
            s, e, sub = find_subarray_with_target_sum(custom_arr, target)
            if s != -1:
                print(f"Subarray found at indices [{s}..{e}]: {sub}")
            else:
                print("No subarray found with that sum.")
        except ValueError:
            print("Invalid input! Please enter integer values.")
    else:
        n = int(input("Enter n for fixed-window test (try 5 or 6): "))
        guess = input("What is win_sum(" + str(n) + ")? ")
        print(" win_sum(" + str(n) + ") =", win_sum(n), " your guess:", guess)


if __name__ == "__main__":
    run_demo()
