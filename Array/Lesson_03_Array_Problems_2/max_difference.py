# max_difference.py / acp_max_difference.py
# Module 7: Array - Lesson 3: Array Problems 2
# ACP: MaxDifference
# Description: Finds the maximum difference arr[j] - arr[i] such that j > i and arr[j] > arr[i].

def max_difference_optimal(arr):
    """
    Finds the maximum difference between two elements such that the larger element
    appears after the smaller element (arr[j] - arr[i] where j > i).
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if len(arr) < 2:
        return -1
    
    min_element = arr[0]
    max_diff = -1
    
    for j in range(1, len(arr)):
        diff = arr[j] - min_element
        if diff > max_diff:
            max_diff = diff
        if arr[j] < min_element:
            min_element = arr[j]
            
    return max_diff


def max_difference_bruteforce(arr):
    """
    Brute-force O(n^2) approach for verification.
    """
    max_diff = -1
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                diff = arr[j] - arr[i]
                if diff > max_diff:
                    max_diff = diff
    return max_diff


def run_acp_demo():
    print("=" * 60)
    print("   ARRAY PROBLEMS 2 - ACP: MAX DIFFERENCE")
    print("=" * 60)
    print("Goal: Find maximum arr[j] - arr[i] where j > i and arr[j] > arr[i].\n")
    
    test_cases = [
        [2, 3, 10, 6, 4, 8, 1],
        [7, 9, 5, 6, 3, 2],
        [10, 8, 7, 6, 5],
        [1, 2, 90, 10, 110],
        [34, 8, 10, 3, 2, 80, 30, 33, 1]
    ]
    
    for idx, arr in enumerate(test_cases, 1):
        opt_ans = max_difference_optimal(arr)
        bf_ans = max_difference_bruteforce(arr)
        print(f"Test Case {idx}:")
        print(f"  Array: {arr}")
        print(f"  Max Difference (Optimal O(n)): {opt_ans}")
        print(f"  Max Difference (Brute Force):   {bf_ans}")
        print(f"  Status: {'PASSED' if opt_ans == bf_ans else 'FAILED'}")
        print("-" * 55)
        
    print("\n--- Interactive Custom Array Test ---")
    user_input = input("Enter array numbers separated by spaces (e.g. 2 3 10 6 4 8 1) or press Enter to skip: ")
    if user_input.strip():
        try:
            custom_arr = [int(x) for x in user_input.split()]
            ans = max_difference_optimal(custom_arr)
            print(f"Your Array: {custom_arr}")
            print(f"Maximum Difference (j > i): {ans}")
        except ValueError:
            print("Invalid input! Please enter integer values.")
            
    print("\n" + "=" * 60)
    print("                     PROJECT SUMMARY")
    print("=" * 60)
    print("1. Problem: Find max(arr[j] - arr[i]) where j > i.")
    print("2. Optimal Algorithm: Keep track of min_element seen so far.")
    print("3. Time Complexity: O(n) with single-pass scan.")
    print("4. Space Complexity: O(1) auxiliary space.")
    print("=" * 60)


if __name__ == "__main__":
    run_acp_demo()
