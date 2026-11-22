# Recursion Repository

This repository contains Python activities, exercises, and After-Class Projects (ACP) for the **Recursion** module.

---

## Repository Structure

```
Recursion/
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
└── README.md
```

---

## Lesson 1: Introduction to Recursion

| File | Type | Description |
| :--- | :--- | :--- |
| `01_sum_down.py` | Activity 1 | Introduces `sum_down(n) = n + sum_down(n - 1)`, the base case (`n == 0`), and build/unwind phases. |
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

## How to Run

Navigate into any lesson folder and run the scripts:

### Lesson 1
```bash
python Lesson_01_Introduction_to_Recursion/01_sum_down.py
python Lesson_01_Introduction_to_Recursion/02_factorial.py
python Lesson_01_Introduction_to_Recursion/03_stack_overflow.py
python Lesson_01_Introduction_to_Recursion/acp_countdown_timer.py
```

### Lesson 2
```bash
python Lesson_02_Types_of_Recursion/01_linear_tail.py
python Lesson_02_Types_of_Recursion/02_head_increasing.py
python Lesson_02_Types_of_Recursion/03_tree_recursion.py
python Lesson_02_Types_of_Recursion/acp_stack_frame_visualizer.py
```

### Lesson 3
```bash
python Lesson_03_Recursion_on_List/01_head_tail.py
python Lesson_03_Recursion_on_List/02_list_sum.py
python Lesson_03_Recursion_on_List/03_list_max.py
python Lesson_03_Recursion_on_List/acp_score_list_explorer.py
```
