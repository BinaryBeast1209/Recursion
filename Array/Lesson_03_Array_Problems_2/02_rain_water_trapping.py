# 02_rain_water_trapping.py
# Topic: Rainwater Trapped (Left tallest bars, Right tallest bars)

from rain_water_trapping import rainwater, trap_rain_water_general

if __name__ == "__main__":
    input("rainwater(n) traps water between two bars of height n. Press Enter ")
    print(" rainwater(3) =", rainwater(3))
    print(" rainwater(4) =", rainwater(4))

    n = int(input("Enter bar height (try 5 or 6): "))
    guess = input("What is rainwater(" + str(n) + ")? ")
    input("water = min(left tallest, right tallest) - bar height at the gap. Press Enter ")
    print(" rainwater(" + str(n) + ") =", rainwater(n), " your guess:", guess)
