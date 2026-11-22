# longest_odd_even_subarray.py / acp_longest_odd_even_subarray.py
# Module 7: Array - Lesson 5: Kadane's Algorithm
# ACP: LongestOddEvenSubarray
# Description: Finds the length and elements of the longest contiguous subarray with alternating even and odd elements.

def longest_odd_even_subarray(arr):
    """
    Finds the length and subarray of the longest contiguous alternating odd/even elements
    using a Kadane-style streak counter with reset.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return 0, []

    max_len = 1
    current_len = 1
    best_end_idx = 0

    for i in range(1, len(arr)):
        # Check if current element and previous element have alternating parity
        if arr[i] % 2 != arr[i - 1] % 2:
            current_len += 1
        else:
            current_len = 1

        if current_len > max_len:
            max_len = current_len
            best_end_idx = i

    best_subarray = arr[best_end_idx - max_len + 1 : best_end_idx + 1]
    return max_len, best_subarray


def run_acp_demo():
    print("=" * 60)
    print("   KADANE'S ALGORITHM - ACP: LONGEST ODD-EVEN SUBARRAY")
    print("=" * 60)
    print("Goal: Find longest subarray where adjacent numbers alternate parity.\n")

    test_cases = [
        [10, 12, 14, 7, 8],
        [5, 10, 20, 63, 14],
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8],
        [1, 3, 5, 7],
        [1, 2, 2, 3, 4, 5, 6, 8, 10]
    ]

    for idx, arr in enumerate(test_cases, 1):
        max_l, sub = longest_odd_even_subarray(arr)
        print(f"Test Case {idx}:")
        print(f"  Array:            {arr}")
        print(f"  Longest Subarray: {sub}")
        print(f"  Length:           {max_l}")
        print("-" * 55)

    print("\n--- Interactive Custom Array Test ---")
    user_input = input("Enter numbers separated by spaces (e.g. 10 12 14 7 8) or press Enter to skip: ")
    if user_input.strip():
        try:
            custom_arr = [int(x) for x in user_input.split()]
            max_l, sub = longest_odd_even_subarray(custom_arr)
            print(f"Your Array:            {custom_arr}")
            print(f"Longest Alternating:   {sub}")
            print(f"Length:                {max_l}")
        except ValueError:
            print("Invalid input! Please enter integer values.")

    print("\n" + "=" * 60)
    print("                     PROJECT SUMMARY")
    print("=" * 60)
    print("1. Parity alternation: (arr[i] % 2) != (arr[i - 1] % 2)")
    print("2. Extends current streak when true; resets streak to 1 when false.")
    print("3. Tracks max_len and slice indices in a single pass.")
    print("4. Time Complexity: O(n), Space Complexity: O(1).")
    print("=" * 60)


if __name__ == "__main__":
    run_acp_demo()
