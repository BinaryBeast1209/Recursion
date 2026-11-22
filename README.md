# Recursion & Arrays Repository

This repository contains Python activities, exercises, and After-Class Projects (ACP) for both the **Recursion** and **Array** modules.

---

## Repository Structure

```
Recursion/
│
├── Array/
│   ├── 01_mean_array_median.py
│   ├── 02_max_array_min.py
│   ├── 03_second_largest_element.py
│   └── reverse_array.py
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

| File | Type | Description |
| :--- | :--- | :--- |
| `01_mean_array_median.py` | Activity 1 (MeanArrayMedian) | Computes the mean (average) and median of an array. |
| `02_max_array_min.py` | Activity 2 (MaxArrayMin) | Finds the minimum and maximum elements of an array using comparisons. |
| `03_second_largest_element.py` | Activity 3 (SecondLargestElement) | Finds the second largest element in an array with single-pass comparison. |
| `reverse_array.py` | ACP Project (ArrayReverse) | In-place array reversal using two-pointer swap and temporary variable, plus palindrome check. |

---

## Lesson 1: Introduction to Recursion

| File | Type | Description |
| :--- | :--- | :--- |
| `01_sum_down.py` | Activity 1 | Introduces `sum_down(n) = n + sum_down(n - 1)`, base case (`n == 0`), and build/unwind phases. |
| `02_factorial.py` | Activity 2 | Implements recursive factorial $n! = n \times (n-1)!$ with base case $0! = 1$. |
| `03_stack_overflow.py` | Activity 3 | Demonstrates call stack depth, stack frames, and Python's default recursion limit (1000). |
| `acp_countdown_timer.py` | ACP Project | **My Countdown Timer Challenge** (`ACPDSCM6L1`): Recursive countdown, count up, build & unwind, and factorial. |

---

## Lesson 2: Types of Recursion

| File | Type | Description |
| :--- | :--- | :--- |
| `01_linear_tail.py` | Activity 1 (Tail Recursion) | Tail recursion using an accumulator (`tail_sum(n, acc)`); work is performed before the recursive call. |
| `02_head_increasing.py` | Activity 2 (Bounce) | Head recursion (`mirror(n)`); recursive call occurs first and work happens during stack unwinding. |
| `03_tree_recursion.py` | Activity 3 (Fibonacci) | Tree recursion (`fib(n) = fib(n-1) + fib(n-2)`); two branching recursive calls per step. |
| `acp_stack_frame_visualizer.py` | ACP Project | **Stack Frame Visualizer** (`ACPDSCM6L2`): Compares linear, tail, head, increasing-decreasing, and tree recursion patterns. |

---

## Lesson 3: Recursion on List

| File | Type | Description |
| :--- | :--- | :--- |
| `01_head_tail.py` | Activity 1 (Head-Tail) | Demonstrates the head-tail pattern (`lst[0]` and `lst[1:]`) and empty list base case `[]`. |
| `02_list_sum.py` | Activity 2 (List Sum) | Adds elements of a list recursively: `head + list_sum(tail)` until empty list base case returns 0. |
| `03_list_max.py` | Activity 3 (List Max) | Finds maximum element recursively: compares head with recursive max of tail; base case is single-element list. |
| `acp_score_list_explorer.py` | ACP Project | **Score List Explorer** (`ACPDSCM6L3`): Head-tail demo, list shrinking, recursive sorted check, recursive sum, and recursive max. |

---

## Lesson 4: Recursive Problems 1

| File | Type | Description |
| :--- | :--- | :--- |
| `01_digit_flip.py` | Activity 1 (Flip Number) | Reverses an integer recursively using `% 10` (peel last digit) and `// 10` (recurse on remaining). |
| `02_flip_name.py` | Activity 2 (Flip a Name) | Reverses a string using head recursion: `flip_name(s[1:]) + s[0]` until base case `len(s) == 1`. |
| `03_power_of_4.py` | Activity 3 (Power of 4 Check) | Recursively checks powers of 4 with two stopping conditions: YES stop (`n == 1`) and NO stop (remainder / non-positive). |
| `acp_flip_it_with_recursion.py` | ACP Project | **Flip It with Recursion** (`ACPDSCM6L4`): Digit extraction, recursive number reversal, string reversal, and power-of-4 verification. |

---

## Lesson 5: Recursive Problems 2

| File | Type | Description |
| :--- | :--- | :--- |
| `01_stair_climb.py` | Activity 1 (Stair Climb) | Counts ways to climb $n$ stairs using 1-step or 2-step choices via branching recursion `ways(n-1) + ways(n-2)`. |
| `02_balanced_parens.py` | Activity 2 (Balanced Parentheses) | Recursive branching to count all valid parentheses/brace combinations with $l > r$ and $l < n$ rules. |
| `acp_stair_climb_and_brace_builder.py` | ACP Project | **Stair Climb and Brace Builder** (`ACPDSCM6L5`): Stair climb solution, call tree trace with indentation, and generating all balanced brace permutations. |

---

## Lesson 6: Recursive Problems 3

| File | Type | Description |
| :--- | :--- | :--- |
| `01_tower_of_hanoi.py` | Activity 1 (Tower of Hanoi) | Calculates minimum moves to shift disks using $hanoi(n) = 2 \times hanoi(n-1) + 1$ ($2^n - 1$). |
| `02_phone_keypad.py` | Activity 2 (Phone Keypad) | Counts all possible letter combinations for keypad digits via linear multiplication chain recursion. |
| `03_recursion_tree.py` | Activity 3 (Recursion Trees) | Counts grid paths with branching recursion $paths(m-1, n) + paths(m, n-1)$, demonstrating recursion tree growth. |
| `acp_keypad_word_generator.py` | ACP Project | **Keypad Word Generator** (`ACPDSCM6L6`): Tower of Hanoi step simulation, keypad combinations generation, and indented recursion tree trace. |

---

## How to Run

### Array Module
```bash
python Array/01_mean_array_median.py
python Array/02_max_array_min.py
python Array/03_second_largest_element.py
python Array/reverse_array.py
```
