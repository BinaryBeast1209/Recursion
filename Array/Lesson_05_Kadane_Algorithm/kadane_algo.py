# kadane_algo.py / 01_max_mid.py
# Topic: Subarrays, Running Sum with Reset, Max-So-Far Tracker, Kadane's Algorithm

def max_mid(n):
    arr = [-1, n, -1]
    current = best = arr[0]
    for x in arr[1:]:
        if current < 0:
            current = x
        else:
            current = current + x
        if current > best:
            best = current
    return best

def kadane_algorithm(arr):
    """
    Standard Kadane's algorithm to find maximum subarray sum in any array.
    """
    if not arr:
        return 0
    max_so_far = arr[0]
    curr_max = arr[0]
    for x in arr[1:]:
        curr_max = max(x, curr_max + x)
        max_so_far = max(max_so_far, curr_max)
    return max_so_far

if __name__ == "__main__":
    input("max_mid(n) finds the max subarray sum in [-1, n, -1]. Press Enter ")
    print(" max_mid(3) =", max_mid(3))
    print(" max_mid(4) =", max_mid(4))

    n = int(input("Enter n (try 5 or 6): "))
    guess = input("What is max_mid(" + str(n) + ")? ")
    input("negative at start resets — best locks in the peak value n. Press Enter ")
    print(" max_mid(" + str(n) + ") =", max_mid(n), " your guess:", guess)
