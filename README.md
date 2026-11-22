# Introduction to Recursion

This repository contains Python activities and the After-Class Project (ACP) for **Introduction to Recursion**.

## Repository Structure

| File | Description | Topics Covered |
| :--- | :--- | :--- |
| `01_sum_down.py` | Activity 1: Recursion + Base Case + Build & Unwind | What is Recursion, The Base Case, Build and Unwind |
| `02_factorial.py` | Activity 2: Counting with Recursion + Factorial | Recursive factorial, $0! = 1$ base case |
| `03_stack_overflow.py` | Activity 3: Call Stack & Stack Overflow | Stack frames, recursion limits, safe depths |
| `acp_countdown_timer.py` | After-Class Project: My Countdown Timer Challenge | Countdown, count-up, build & unwind, factorial, stack safety |

---

## Activities Overview

### 1. `01_sum_down.py` (Activity 1)
- Introduces recursive function `sum_down(n) = n + sum_down(n - 1)`.
- Identifies the base case `n == 0: return 0`.
- Demonstrates build and unwind phases.

### 2. `02_factorial.py` (Activity 2)
- Calculates factorial recursively using $n! = n \times (n-1)!$.
- Implements base case $0! = 1$.

### 3. `03_stack_overflow.py` (Activity 3)
- Shows how each recursive call places a frame on Python's call stack.
- Explains the default 1000-frame recursion limit and why a base case is vital to avoid `RecursionError`.

### 4. `acp_countdown_timer.py` (After-Class Project: My Countdown Timer Challenge)
- Project code: `ACPDSCM6L1`
- Includes recursive countdown (`countdown(5)`), build and unwind demo (`build_and_unwind(3)`), count up (`count_up(1)`), factorial (`factorial(5)`), and stack overflow safety discussion (`unsafe_countdown`).

---

## How to Run

Run any file with Python:

```bash
python 01_sum_down.py
python 02_factorial.py
python 03_stack_overflow.py
python acp_countdown_timer.py
```
