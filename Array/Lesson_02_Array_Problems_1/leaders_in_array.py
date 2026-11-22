# leaders_in_array.py
# Topic: Leaders in an Array (Right-to-Left Traversal with Max-So-Far)

def find_leaders(arr):
    """
    Finds all 'leader' elements in the list.
    An element is a leader if it is strictly greater than all elements to its right.
    The rightmost element is always a leader.
    """
    if not arr:
        return []
    
    n = len(arr)
    max_from_right = arr[-1]
    leaders = [max_from_right]
    
    # Traverse from right to left starting from second to last element
    for i in range(n - 2, -1, -1):
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            leaders.append(arr[i])
            
    # Reverse to preserve original left-to-right order
    leaders.reverse()
    return leaders


if __name__ == "__main__":
    input("find_leaders(arr) identifies elements greater than all values to their right. Press Enter ")
    
    sample1 = [16, 17, 4, 3, 5, 2]
    print("  find_leaders([16, 17, 4, 3, 5, 2]) =", find_leaders(sample1))
    
    sample2 = [1, 2, 3, 4, 0]
    print("  find_leaders([1, 2, 3, 4, 0]) =", find_leaders(sample2))
    
    user_input = input("Enter numbers separated by space (or press Enter for default [7, 10, 4, 10, 6, 5, 2]): ")
    if user_input.strip():
        test_arr = [int(x) for x in user_input.split()]
    else:
        test_arr = [7, 10, 4, 10, 6, 5, 2]
        
    guess = input("What are the leaders in " + str(test_arr) + "? ")
    input("Traversing from right to left tracking max_right. Press Enter to view result ")
    result = find_leaders(test_arr)
    print("  find_leaders(" + str(test_arr) + ") =", result, "  your guess:", guess)
