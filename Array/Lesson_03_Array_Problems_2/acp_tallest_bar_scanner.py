# ================================
# TALLEST BAR SCANNER (ACP)
# Project Code: ACPDSCM7L3
# ================================
# Topics:
# Stocks buy-sell | Profit accumulation
# Left tallest bars | Right tallest bars | Rainwater trapped

print("================================")
print("TALLEST BAR SCANNER")
print("================================")

# ------------------------------------------------
# PART 1 — STOCKS BUY-SELL (SINGLE TRANSACTION)
# ------------------------------------------------
# Track lowest price seen so far, update max profit whenever gap is higher
def max_profit(prices):
    if not prices:
        return 0
    min_price = prices[0]
    profit = 0
    for p in prices:
        min_price = min(min_price, p)
        profit = max(profit, p - min_price)
    return profit

prices1 = [7, 1, 5, 3, 6, 4]
print("\nPART 1: Stocks Buy-Sell (Single Transaction)")
print("Stock Prices:", prices1)
print("Max Profit:", max_profit(prices1))

# ------------------------------------------------
# PART 2 — PROFIT ACCUMULATION (UNLIMITED TRANSACTIONS)
# ------------------------------------------------
# Sum all consecutive upward price movements
def total_profit(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    return profit

prices2 = [1, 5, 2, 8]
print("\nPART 2: Profit Accumulation (Unlimited Transactions)")
print("Stock Prices:", prices2)
print("Total Accumulated Profit:", total_profit(prices2))

# ------------------------------------------------
# PART 3 — LEFT TALLEST BARS (PREFIX MAXIMUM)
# ------------------------------------------------
# Prefix max: left[i] = max(left[i-1], bars[i])
def get_left_tallest(bars):
    n = len(bars)
    if n == 0:
        return []
    left = [0] * n
    left[0] = bars[0]
    for i in range(1, n):
        left[i] = max(left[i - 1], bars[i])
    return left

bars = [0, 3, 0, 5, 0, 4, 0]
left_tallest = get_left_tallest(bars)
print("\nPART 3: Left Tallest Bars (Prefix Maximum)")
print("Bars:", bars)
print("Left Tallest Array:", left_tallest)

# ------------------------------------------------
# PART 4 — RIGHT TALLEST BARS (SUFFIX MAXIMUM)
# ------------------------------------------------
# Suffix max: right[i] = max(right[i+1], bars[i])
def get_right_tallest(bars):
    n = len(bars)
    if n == 0:
        return []
    right = [0] * n
    right[-1] = bars[-1]
    for i in range(n - 2, -1, -1):
        right[i] = max(right[i + 1], bars[i])
    return right

right_tallest = get_right_tallest(bars)
print("\nPART 4: Right Tallest Bars (Suffix Maximum)")
print("Bars:", bars)
print("Right Tallest Array:", right_tallest)

# ------------------------------------------------
# PART 5 — RAINWATER TRAPPED
# ------------------------------------------------
# Water trapped at position i = max(0, min(left[i], right[i]) - bars[i])
def trap_rainwater(bars):
    if not bars:
        return 0
    left = get_left_tallest(bars)
    right = get_right_tallest(bars)
    total_water = 0
    for i in range(len(bars)):
        water_level = min(left[i], right[i])
        trapped_at_i = max(0, water_level - bars[i])
        total_water += trapped_at_i
    return total_water

print("\nPART 5: Trapping Rain Water")
print("Bars:", bars)
print("Total Rainwater Trapped:", trap_rainwater(bars))

# FINAL SUMMARY
print("\n================================")
print("TALLEST BAR SCANNER SUMMARY")
print("================================")
print("1. Stocks Buy-Sell tracks the minimum price so far to find the maximum gap.")
print("2. Profit Accumulation captures every upward jump for unlimited trades.")
print("3. Prefix maximum array tracks tallest barriers from the left.")
print("4. Suffix maximum array tracks tallest barriers from the right.")
print("5. Rainwater trapped equals min(left, right) - bar height at each position.")
print("================================")
