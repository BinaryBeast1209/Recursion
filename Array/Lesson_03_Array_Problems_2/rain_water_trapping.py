# rain_water_trapping.py / 02_rain_water_trapping.py
# Topic: Rainwater Trapped (Left tallest bars, Right tallest bars)

def rainwater(n):
    bars = [0, n, 0, n, 0]
    return min(max(bars[:3]), max(bars[2:])) - bars[2]

def trap_rain_water_general(heights):
    """
    General two-pointer approach to calculate trapped rainwater across any elevation map.
    """
    if not heights:
        return 0
    left, right = 0, len(heights) - 1
    left_max, right_max = heights[left], heights[right]
    water = 0
    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, heights[left])
            water += left_max - heights[left]
        else:
            right -= 1
            right_max = max(right_max, heights[right])
            water += right_max - heights[right]
    return water

if __name__ == "__main__":
    input("rainwater(n) traps water between two bars of height n. Press Enter ")
    print(" rainwater(3) =", rainwater(3))
    print(" rainwater(4) =", rainwater(4))

    n = int(input("Enter bar height (try 5 or 6): "))
    guess = input("What is rainwater(" + str(n) + ")? ")
    input("water = min(left tallest, right tallest) - bar height at the gap. Press Enter ")
    print(" rainwater(" + str(n) + ") =", rainwater(n), " your guess:", guess)
