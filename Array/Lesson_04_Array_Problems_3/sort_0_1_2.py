# sort_0_1_2.py / acp_sort_012.py
# Module 7: Array - Lesson 4: Array Problems 3
# ACP: Sort0's1's2's (Dutch National Flag Algorithm)
# Description: Sorts an array consisting of only 0s, 1s, and 2s in-place with O(n) time and O(1) space.

def sort_012_dutch_flag(arr):
    """
    Sorts an array of 0s, 1s, and 2s in a single pass using the Dutch National Flag algorithm.
    Pointers:
      - low: boundary where elements before low are all 0
      - mid: current scanning pointer
      - high: boundary where elements after high are all 2
    Time Complexity: O(n) (one pass)
    Space Complexity: O(1) in-place
    """
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else: # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr


def sort_012_counting(arr):
    """
    Counting approach: counts 0s, 1s, and 2s, then overwrites the array.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    c0 = arr.count(0)
    c1 = arr.count(1)
    c2 = arr.count(2)

    arr[:c0] = [0] * c0
    arr[c0:c0 + c1] = [1] * c1
    arr[c0 + c1:] = [2] * c2
    return arr


def run_acp_demo():
    print("=" * 60)
    print("    ARRAY PROBLEMS 3 - ACP: SORT 0's, 1's, 2's")
    print("        (Dutch National Flag 3-Pointer Algorithm)")
    print("=" * 60)

    test_cases = [
        [2, 0, 2, 1, 1, 0],
        [1, 2, 0],
        [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1],
        [2, 2, 2, 1, 1, 0, 0],
        [0, 0, 0],
        [2, 1, 0]
    ]

    for idx, original in enumerate(test_cases, 1):
        arr_df = list(original)
        arr_cnt = list(original)
        sort_012_dutch_flag(arr_df)
        sort_012_counting(arr_cnt)
        is_sorted = (arr_df == sorted(original)) and (arr_df == arr_cnt)

        print(f"Test Case {idx}:")
        print(f"  Original:    {original}")
        print(f"  Sorted (DF): {arr_df}")
        print(f"  Status:      {'PASSED' if is_sorted else 'FAILED'}")
        print("-" * 55)

    print("\n--- Try Your Own Sequence of 0s, 1s, and 2s ---")
    user_input = input("Enter numbers (0, 1, 2) separated by spaces or press Enter to skip: ")
    if user_input.strip():
        try:
            custom_arr = [int(x) for x in user_input.split()]
            if all(x in (0, 1, 2) for x in custom_arr):
                sorted_custom = list(custom_arr)
                sort_012_dutch_flag(sorted_custom)
                print(f"Original Array: {custom_arr}")
                print(f"Sorted Array:   {sorted_custom}")
            else:
                print("Array should only contain 0, 1, and 2.")
        except ValueError:
            print("Invalid input! Please enter integer values.")

    print("\n" + "=" * 60)
    print("                     PROJECT SUMMARY")
    print("=" * 60)
    print("1. Dutch National Flag algorithm uses 3 pointers: low, mid, high.")
    print("2. Elements < low are 0s; between high & end are 2s; mid scans.")
    print("3. Single-pass O(n) runtime and in-place O(1) auxiliary space.")
    print("=" * 60)


if __name__ == "__main__":
    run_acp_demo()
