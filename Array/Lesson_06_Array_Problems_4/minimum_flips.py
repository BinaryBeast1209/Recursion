# minimum_flips.py / acp_minimum_flips.py
# Module 7: Array - Lesson 6: Array Problems 4
# ACP: MinimumFlips
# Description: Finds the minimum group flips needed to make all binary array elements the same,
#              and prints the exact index ranges to flip.

def min_group_flips(arr):
    """
    Finds the minimum consecutive group flips to make all elements same in a binary array.
    Always flipping groups different from arr[0] is mathematically guaranteed to be optimal.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(arr)
    if n == 0:
        return []

    flips = []
    start = -1

    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            if arr[i] != arr[0]:
                start = i
            else:
                flips.append((start, i - 1))
                start = -1

    if arr[n - 1] != arr[0] and start != -1:
        flips.append((start, n - 1))

    return flips


def min_sign_flips_to_zero_sum(arr):
    """
    For an array of 1s and -1s, finds minimum flips to make sum equal to 0.
    Returns -1 if impossible (when length is odd).
    """
    n = len(arr)
    if n % 2 != 0:
        return -1
    total_sum = sum(arr)
    return abs(total_sum) // 2


def run_acp_demo():
    print("=" * 60)
    print("      ARRAY PROBLEMS 4 - ACP: MINIMUM FLIPS")
    print("=" * 60)
    print("Goal: Find minimum consecutive group flips to make binary array same.\n")

    test_cases = [
        [1, 1, 0, 0, 0, 1],
        [0, 0, 1, 1, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0],
        [1, 1, 1],
        [0, 1, 1, 0, 0, 1, 0, 0, 1]
    ]

    for idx, arr in enumerate(test_cases, 1):
        flips = min_group_flips(arr)
        target_val = 1 - arr[0] if flips else None
        print(f"Test Case {idx}:")
        print(f"  Array: {arr}")
        print(f"  Total Flips Needed: {len(flips)}")
        if flips:
            flip_details = ", ".join([f"From index {s} to {e} (flip {target_val}s)" for s, e in flips])
            print(f"  Flip Ranges: {flip_details}")
        else:
            print("  Array already uniform; 0 flips needed.")
        print("-" * 55)

    print("\n--- Interactive Custom Binary Array Test ---")
    user_input = input("Enter binary numbers (0s and 1s) separated by spaces or press Enter to skip: ")
    if user_input.strip():
        try:
            custom_arr = [int(x) for x in user_input.split()]
            if all(x in (0, 1) for x in custom_arr):
                flips = min_group_flips(custom_arr)
                print(f"Your Array: {custom_arr}")
                print(f"Minimum Group Flips: {len(flips)}")
                for s, e in flips:
                    print(f"  - Flip index {s} to {e} (change {custom_arr[s]} to {1 - custom_arr[s]})")
            else:
                print("Array elements should only be 0 or 1.")
        except ValueError:
            print("Invalid input! Please enter integer values.")

    print("\n" + "=" * 60)
    print("                     PROJECT SUMMARY")
    print("=" * 60)
    print("1. In any binary array, count of 0-groups and 1-groups differs by at most 1.")
    print("2. Flipping groups of elements different from arr[0] is always minimal.")
    print("3. Single-pass traversal: O(n) Time Complexity and O(1) Space Complexity.")
    print("=" * 60)


if __name__ == "__main__":
    run_acp_demo()
