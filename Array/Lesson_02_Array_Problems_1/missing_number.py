# missing_number.py / acp_missing_number.py
# Module 7: Array - Lesson 2: Array Problems 1
# ACP: MissingNumber
# Description: Finds the missing number from an array of size n-1 containing distinct integers from 1 to n.

def find_missing_number_sum(arr):
    """
    Finds the missing number using the mathematical sum formula:
    Sum of 1 to n = n * (n + 1) // 2
    Missing = Expected Sum - Actual Sum
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(arr) + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


def find_missing_number_xor(arr):
    """
    Finds the missing number using bitwise XOR.
    XOR of a number with itself is 0, XOR with 0 is the number.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(arr) + 1
    xor_all = 0
    for i in range(1, n + 1):
        xor_all ^= i
        
    xor_arr = 0
    for num in arr:
        xor_arr ^= num
        
    return xor_all ^ xor_arr


def run_acp_demo():
    print("=" * 55)
    print("   ARRAY PROBLEMS 1 - ACP: MISSING NUMBER")
    print("=" * 55)
    print("Goal: Find the single missing number from sequence 1 to n.\n")
    
    # Pre-defined test cases
    test_cases = [
        ([1, 2, 4, 5], 5),
        ([1, 2, 3, 5, 6, 7], 7),
        ([2, 3, 1, 5], 5),
        ([6, 1, 2, 8, 3, 4, 7, 10, 5], 10),
    ]
    
    for idx, (arr, n) in enumerate(test_cases, 1):
        missing_sum = find_missing_number_sum(arr)
        missing_xor = find_missing_number_xor(arr)
        print(f"Test Case {idx}:")
        print(f"  Array: {arr}")
        print(f"  Range: 1 to {n}")
        print(f"  Missing Number (Sum Method): {missing_sum}")
        print(f"  Missing Number (XOR Method): {missing_xor}")
        print(f"  Verification: {'PASSED' if missing_sum == missing_xor else 'FAILED'}")
        print("-" * 50)
        
    # Interactive input
    print("\n--- Try Your Own Sequence ---")
    user_input = input("Enter array elements separated by space (e.g. 1 2 4 5) or press Enter to skip: ")
    if user_input.strip():
        try:
            custom_arr = [int(x) for x in user_input.split()]
            ans_sum = find_missing_number_sum(custom_arr)
            ans_xor = find_missing_number_xor(custom_arr)
            print(f"\nYour Array: {custom_arr}")
            print(f"Detected Range: 1 to {len(custom_arr) + 1}")
            print(f"Missing Number: {ans_sum}")
        except ValueError:
            print("Invalid input! Please enter integer values.")
            
    print("\n" + "=" * 55)
    print("                PROJECT SUMMARY")
    print("=" * 55)
    print("1. Formula: Missing = [n * (n + 1) // 2] - sum(arr)")
    print("2. XOR Property: A ^ A = 0, A ^ 0 = A")
    print("3. Time Complexity: O(n), Space Complexity: O(1)")
    print("=" * 55)


if __name__ == "__main__":
    run_acp_demo()
