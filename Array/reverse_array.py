# reverse_array.py
# Assignment: ArrayReverse
# Goal: Reverse an array without using reverse(), [::-1] or reversed()

arr = [6, 5, 4, 3, 2, 1]
arr_size = len(arr)
print("Original array:", arr)

# Swap the first with the last, the second with the second last, and so on
def reverseArray(arr, arr_size):
    for i in range(arr_size // 2):
        j = arr_size - 1 - i
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

reverseArray(arr, arr_size)
print("Reversed array:", arr)

# ------------------------------------------------
# Optional Challenge: Palindrome Check
# ------------------------------------------------
def isPalindrome(arr, arr_size):
    for i in range(arr_size // 2):
        if arr[i] != arr[arr_size - 1 - i]:
            return False
    return True

print("\n--- Challenge: Palindrome Check ---")
print("Is [1, 2, 3, 2, 1] a palindrome?", isPalindrome([1, 2, 3, 2, 1], 5))
print("Is [1, 2, 3] a palindrome?", isPalindrome([1, 2, 3], 3))
