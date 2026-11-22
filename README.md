# Recursion & Arrays Repository

This repository contains Python activities, exercises, and After-Class Projects (ACP) for both the **Recursion** and **Array** modules.

---

## Repository Structure

```
Recursion/
│
├── Array/
│   ├── Lesson_01_Introduction_to_Arrays/
│   │   ├── 01_mean_array_median.py
│   │   ├── 02_max_array_min.py
│   │   ├── 03_second_largest_element.py
│   │   └── reverse_array.py
│   ├── Lesson_02_Array_Problems_1/
│   │   ├── 01_two_pointer_reverse.py
│   │   ├── 02_left_rotate.py
│   │   ├── 03_reverse_in_groups.py
│   │   ├── 03_leaders_in_array.py
│   │   ├── leaders_in_array.py
│   │   ├── missing_number.py
│   │   ├── acp_missing_number.py
│   │   └── acp_rotate_my_scores.py
│   ├── Lesson_03_Array_Problems_2/
│   │   ├── 01_max_profit.py
│   │   ├── 02_total_profit.py
│   │   ├── 03_rainwater.py
│   │   └── acp_tallest_bar_scanner.py
│   ├── Lesson_04_Array_Problems_3/
│   │   ├── 01_max_ones.py
│   │   ├── 02_move_zeros.py
│   │   ├── 03_max_zeros.py
│   │   └── acp_binary_streak_tracker.py
│   ├── Lesson_05_Kadane_Algorithm/
│   │   ├── 01_max_mid.py
│   │   ├── 02_max_front.py
│   │   ├── 03_max_after.py
│   │   └── acp_array_energy_tracker.py
│   └── Lesson_06_Array_Problems_4/
│       ├── 01_eq_mid.py
│       ├── 02_eq_val.py
│       ├── 03_win_sum.py
│       └── acp_target_tracker_lab.py
│
├── Lesson_01_Introduction_to_Recursion/
│   ├── 01_sum_down.py
│   ├── 02_factorial.py
│   ├── 03_stack_overflow.py
│   └── acp_countdown_timer.py
│
├── Lesson_02_Types_of_Recursion/
│   ├── 01_linear_tail.py
│   ├── 02_head_increasing.py
│   ├── 03_tree_recursion.py
│   └── acp_stack_frame_visualizer.py
│
├── Lesson_03_Recursion_on_List/
│   ├── 01_head_tail.py
│   ├── 02_list_sum.py
│   ├── 03_list_max.py
│   └── acp_score_list_explorer.py
│
├── Lesson_04_Recursive_Problems_1/
│   ├── 01_digit_flip.py
│   ├── 02_flip_name.py
│   ├── 03_power_of_4.py
│   └── acp_flip_it_with_recursion.py
│
├── Lesson_05_Recursive_Problems_2/
│   ├── 01_stair_climb.py
│   ├── 02_balanced_parens.py
│   └── acp_stair_climb_and_brace_builder.py
│
├── Lesson_06_Recursive_Problems_3/
│   ├── 01_tower_of_hanoi.py
│   ├── 02_phone_keypad.py
│   ├── 03_recursion_tree.py
│   └── acp_keypad_word_generator.py
│
└── README.md
```

---

## Array Module (`Array/`)

### Lesson 1: Introduction to Arrays (`Array/Lesson_01_Introduction_to_Arrays/`)

| File | Type | Description |
| :--- | :--- | :--- |
| `01_mean_array_median.py` | Activity 1 (MeanArrayMedian) | Computes the mean (average) and median of an array. |
| `02_max_array_min.py` | Activity 2 (MaxArrayMin) | Finds the minimum and maximum elements using comparisons. |
| `03_second_largest_element.py` | Activity 3 (SecondLargestElement) | Finds the second largest element in a single pass without sorting. |
| `reverse_array.py` | ACP Project (ArrayReverse) | In-place array reversal using two-pointer swap and temporary variable, plus palindrome check. |

### Lesson 2: Array Problems 1 (`Array/Lesson_02_Array_Problems_1/`)

| File | Type | Description |
| :--- | :--- | :--- |
| `01_two_pointer_reverse.py` | Activity 1 (Two-pointer Reverse) | Reverses `[1..n]` using inward two-pointer swapping (`while i < j`). |
| `02_left_rotate.py` | Activity 2 (Left Rotate / Array Rotate) | Rotates an array to the left by $n$ positions using slice partitioning `arr[n:] + arr[:n]` with a modulo guard. |
| `03_reverse_in_groups.py` | Activity (Reverse in Groups) | Reverses chunks of $k$ elements in place using `arr[i:i+n][::-1]`. |
| `03_leaders_in_array.py` / `leaders_in_array.py` | Activity 3 (Leaders in Array) | Right-to-left scan tracking `max_right` to find all elements strictly greater than all elements to their right. |
| `missing_number.py` / `acp_missing_number.py` | ACP Project (Missing Number) | Finds missing number in $1 \dots n$ array via sum formula $\frac{n(n+1)}{2} - \sum \text{arr}$ and XOR. |
| `acp_rotate_my_scores.py` | ACP Project (Rotate My Scores) | Two-pointer swap, group reverse with `min()`, left rotate by 1 and $n$, and right-to-left leaders scan. |

### Lesson 3: Array Problems 2 (`Array/Lesson_03_Array_Problems_2/`)

| File | Type | Description |
| :--- | :--- | :--- |
| `01_max_profit.py` | Activity 1 (Stocks Buy-Sell) | Greedy single buy-sell profit by tracking the minimum price seen so far. |
| `02_total_profit.py` | Activity 2 (Profit Accumulation) | Unlimited buy-sell profit by summing all positive consecutive price increases (upswings). |
| `03_rainwater.py` | Activity 3 (Rainwater Trapped) | Calculates rainwater trapped between bars using `min(left_max, right_max) - height`. |
| `acp_tallest_bar_scanner.py` | ACP Project (Tallest Bar Scanner) | Full implementation of single buy-sell, profit accumulation, prefix max (left tallest), suffix max (right tallest), and rainwater trapping. |

### Lesson 4: Array Problems 3 (`Array/Lesson_04_Array_Problems_3/`)

| File | Type | Description |
| :--- | :--- | :--- |
| `01_max_ones.py` | Activity 1 (Max Consecutive Ones) | Longest continuous run of 1s using streak counter with reset on 0 and best tracker. |
| `02_move_zeros.py` | Activity 2 (Move Zeros) | Same-direction write pointer collects non-zeros; remaining slots filled with zeros. |
| `03_max_zeros.py` | Activity 3 (Max Consecutive Zeros) | Longest run of 0s using streak counter with reset on 1 and best tracker. |
| `acp_binary_streak_tracker.py` | ACP Project (Binary Streak Tracker) | Binary array analysis, max 1s streak, max 0s streak, generic streak tracker, and in-place move zeros. |

### Lesson 5: Kadane's Algorithm (`Array/Lesson_05_Kadane_Algorithm/`)

| File | Type | Description |
| :--- | :--- | :--- |
| `01_max_mid.py` | Activity 1 (Peak in Middle) | Maximum subarray sum in `[-1, n, -1]`; starting negative resets, locking in peak $n$. |
| `02_max_front.py` | Activity 2 (Front Loaded) | Maximum subarray sum in `[1]*n + [-1]`; tracks sum through positive prefix while best holds. |
| `03_max_after.py` | Activity 3 (Big Reset) | Maximum subarray sum in `[-n] + [1]*n`; large negative triggers immediate reset, then sums $n$ ones. |
| `acp_array_energy_tracker.py` | ACP Project (Array Energy Tracker) | Subarray exploration, Kadane's algorithm, subarray slice tracking with indices, and diverse test cases. |

### Lesson 6: Array Problems 4 (`Array/Lesson_06_Array_Problems_4/`)

| File | Type | Description |
| :--- | :--- | :--- |
| `01_eq_mid.py` | Activity 1 (Equilibrium Index) | Finds index where left sum equals right sum using `sum(arr[:i]) == sum(arr[i+1:])`. |
| `02_eq_val.py` | Activity 2 (Equilibrium Value) | Finds the value located at the equilibrium point in an array. |
| `03_win_sum.py` | Activity 3 (Window Target Sum) | Finds the starting index of the first fixed-size window that sums to target. |
| `acp_target_tracker_lab.py` | ACP Project (Target Tracker Lab) | Slices and balance analysis, equilibrium index, equilibrium value, fixed-size window search, and $O(n)$ sliding window optimization. |

---

## Recursion Module

### Lesson 1: Introduction to Recursion
- `01_sum_down.py`: `sum_down(n) = n + sum_down(n - 1)`.
- `02_factorial.py`: Factorial $n! = n \times (n-1)!$ with base case $0! = 1$.
- `03_stack_overflow.py`: Stack frame growth and 1000 recursion limit.
- `acp_countdown_timer.py`: Countdown, build & unwind, count up, factorial.

### Lesson 2: Types of Recursion
- `01_linear_tail.py`: Tail recursion with accumulator.
- `02_head_increasing.py`: Head recursion (`mirror(n)`).
- `03_tree_recursion.py`: Fibonacci tree branching.
- `acp_stack_frame_visualizer.py`: Visual comparison of recursion patterns.

### Lesson 3: Recursion on List
- `01_head_tail.py`: Head (`lst[0]`) and tail (`lst[1:]`) pattern.
- `02_list_sum.py`: Recursive summation down to `[]`.
- `03_list_max.py`: Recursive maximum with single-element base case.
- `acp_score_list_explorer.py`: List analysis using recursion.

### Lesson 4: Recursive Problems 1
- `01_digit_flip.py`: Digit reversal using `% 10` and `// 10`.
- `02_flip_name.py`: String reversal using head recursion.
- `03_power_of_4.py`: Power of 4 with YES/NO stopping conditions.
- `acp_flip_it_with_recursion.py`: Comprehensive reversal and power checking.

### Lesson 5: Recursive Problems 2
- `01_stair_climb.py`: 1-step or 2-step stair climb combinations.
- `02_balanced_parens.py`: Balanced parentheses counting.
- `acp_stair_climb_and_brace_builder.py`: Stair climb and brace generation.

### Lesson 6: Recursive Problems 3
- `01_tower_of_hanoi.py`: Tower of Hanoi moves ($2^n - 1$).
- `02_phone_keypad.py`: Phone keypad combinations.
- `03_recursion_tree.py`: Grid path finding and tree branching.
- `acp_keypad_word_generator.py`: Hanoi simulation and word generation.

---

## How to Run

### Array Module
```bash
# Lesson 1
python Array/Lesson_01_Introduction_to_Arrays/01_mean_array_median.py
python Array/Lesson_01_Introduction_to_Arrays/02_max_array_min.py
python Array/Lesson_01_Introduction_to_Arrays/03_second_largest_element.py
python Array/Lesson_01_Introduction_to_Arrays/reverse_array.py

# Lesson 2
python Array/Lesson_02_Array_Problems_1/01_two_pointer_reverse.py
python Array/Lesson_02_Array_Problems_1/02_left_rotate.py
python Array/Lesson_02_Array_Problems_1/03_reverse_in_groups.py
python Array/Lesson_02_Array_Problems_1/leaders_in_array.py
python Array/Lesson_02_Array_Problems_1/missing_number.py
python Array/Lesson_02_Array_Problems_1/acp_rotate_my_scores.py

# Lesson 3
python Array/Lesson_03_Array_Problems_2/01_max_profit.py
python Array/Lesson_03_Array_Problems_2/02_total_profit.py
python Array/Lesson_03_Array_Problems_2/03_rainwater.py
python Array/Lesson_03_Array_Problems_2/acp_tallest_bar_scanner.py

# Lesson 4
python Array/Lesson_04_Array_Problems_3/01_max_ones.py
python Array/Lesson_04_Array_Problems_3/02_move_zeros.py
python Array/Lesson_04_Array_Problems_3/03_max_zeros.py
python Array/Lesson_04_Array_Problems_3/acp_binary_streak_tracker.py

# Lesson 5
python Array/Lesson_05_Kadane_Algorithm/01_max_mid.py
python Array/Lesson_05_Kadane_Algorithm/02_max_front.py
python Array/Lesson_05_Kadane_Algorithm/03_max_after.py
python Array/Lesson_05_Kadane_Algorithm/acp_array_energy_tracker.py

# Lesson 6
python Array/Lesson_06_Array_Problems_4/01_eq_mid.py
python Array/Lesson_06_Array_Problems_4/02_eq_val.py
python Array/Lesson_06_Array_Problems_4/03_win_sum.py
python Array/Lesson_06_Array_Problems_4/acp_target_tracker_lab.py
```
