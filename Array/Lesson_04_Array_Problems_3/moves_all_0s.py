# moves_all_0s.py / moves_all_zeros.py / 02_move_zeros.py
# Topic: Same-direction two pointers, Write-pointer pattern

def move_zeros(n):
    arr = [0, 1] * n
    write = 0
    for x in arr:
        if x:
            arr[write] = x
            write += 1
    arr[write:] = [0] * (len(arr) - write)
    return arr

if __name__ == "__main__":
    input("move_zeros(n) moves all zeros to the end of [0,1,0,1,...]. Press Enter ")
    print(" move_zeros(3) =", move_zeros(3))
    print(" move_zeros(4) =", move_zeros(4))

    n = int(input("Enter n (try 5 or 6): "))
    guess = input("What is move_zeros(" + str(n) + ")? ")
    input("write pointer collects non-zeros — fill the rest with zeros. Press Enter ")
    print(" move_zeros(" + str(n) + ") =", move_zeros(n), " your guess:", guess)
