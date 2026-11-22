# max_circular_sum.py / 02_max_circular_sum.py
# Module 7: Array - Lesson 5: Kadane's Algorithm
# Activity 2: MaxCircularSum
# Description: Finds the maximum contiguous subarray sum in a circular array using Kadane's algorithm.

def kadane_max(arr):
    """
    Standard Kadane's algorithm for maximum subarray sum.
    """
    max_so_far = arr[0]
    curr_max = arr[0]
    for x in arr[1:]:
        curr_max = max(x, curr_max + x)
        max_so_far = max(max_so_far, curr_max)
    return max_so_far


def kadane_min(arr):
    """
    Kadane's algorithm variant to find minimum subarray sum.
    """
    min_so_far = arr[0]
    curr_min = arr[0]
    for x in arr[1:]:
        curr_min = min(x, curr_min + x)
        min_so_far = min(min_so_far, curr_min)
    return min_so_far


def max_circular_sum(arr):
    """
    Calculates maximum circular subarray sum.
    Case 1: Subarray does not wrap -> standard Kadane max.
    Case 2: Subarray wraps around -> Total sum - min subarray sum.
    Edge case: If all elements are negative, return standard Kadane max.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if not arr:
        return 0
    
    total_sum = sum(arr)
    max_linear = kadane_max(arr)
    min_linear = kadane_min(arr)
    
    # If all elements are negative, total_sum == min_linear
    if total_sum == min_linear:
        return max_linear
        
    max_wrapped = total_sum - min_linear
    return max(max_linear, max_wrapped)


def run_demo():
    print("=" * 60)
    print("      KADANE'S ALGORITHM - MAX CIRCULAR SUBARRAY SUM")
    print("=" * 60)
    
    test_cases = [
        [5, -3, 5],
        [1, -2, 3, -2],
        [3, -1, 2, -1],
        [3, -2, 2, -3],
        [-2, -3, -1],
        [8, -8, 9, -9, 10, -11, 12]
    ]
    
    for idx, arr in enumerate(test_cases, 1):
        ans = max_circular_sum(arr)
        print(f"Test Case {idx}:")
        print(f"  Array: {arr}")
        print(f"  Total Sum: {sum(arr)}, Max Linear: {kadane_max(arr)}, Min Linear: {kadane_min(arr)}")
        print(f"  Max Circular Sum: {ans}")
        print("-" * 55)
        
    print("\n--- Try Your Own Circular Array ---")
    user_input = input("Enter numbers separated by spaces (e.g. 5 -3 5) or press Enter to skip: ")
    if user_input.strip():
        try:
            custom_arr = [int(x) for x in user_input.split()]
            ans = max_circular_sum(custom_arr)
            print(f"Your Array: {custom_arr}")
            print(f"Max Circular Subarray Sum: {ans}")
        except ValueError:
            print("Invalid input! Please enter integer values.")
            
    print("\n" + "=" * 60)
    print("                     TOPIC SUMMARY")
    print("=" * 60)
    print("1. Non-wrapping max = Kadane(arr)")
    print("2. Wrapping max = Total_Sum - MinSubarray(arr)")
    print("3. Result = max(Non-wrapping, Wrapping)")
    print("4. Edge case: If all elements are negative, return Kadane(arr)")
    print("=" * 60)


if __name__ == "__main__":
    run_demo()
