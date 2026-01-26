# LeetCode Problems

---

## ✅ 1768. Merge Strings Alternately  
**Difficulty:** Easy

### 📝 Description
You are given two strings `word1` and `word2`. Merge the strings by adding letters in alternating order, starting with `word1`. If one string is longer, append the remaining letters at the end.

### 📥 Input
- `word1`: string  
- `word2`: string  

### 📤 Output
- `string` — merged string

### 🔍 Examples

#### Example 1
Input:  word1 = “abc”, word2 = “pqr”
Output: “apbqcr”

#### Example 2
Input:  word1 = “ab”, word2 = “pqrs”
Output: “apbqrs”

#### Example 3
Input:  word1 = “abcd”, word2 = “pq”
Output: “apbqcd”

### ✅ Constraints
- `1 <= word1.length, word2.length <= 100`
- Strings contain lowercase English letters only

---

## ✅ 3318. Find X-Sum of All K-Long Subarrays I  
**Difficulty:** Easy

### 📝 Description
You are given an array `nums` and two integers `k` and `x`.

For each subarray of length `k`:

1. Count occurrences of all elements  
2. Keep only the `x` most frequent elements  
   - If frequencies are equal, keep the **larger** value  
3. Return the **sum** of the kept elements

If there are fewer than `x` distinct elements, the x-sum is the sum of the entire subarray.

### 📥 Input
- `nums`: integer array  
- `k`: sliding window size  
- `x`: number of most frequent elements to keep  

### 📤 Output
- `integer[]` — x-sums for each sliding window

### 🔍 Examples

#### Example 1
Input:  nums = [1,1,2,2,3,4,2,3], k = 6, x = 2
Output: [6,10,12]

#### Example 2
Input:  nums = [3,8,7,8,7,5], k = 2, x = 2
Output: [11,15,15,15,12]

### ✅ Constraints
- `1 <= n == nums.length <= 50`
- `1 <= nums[i] <= 50`
- `1 <= x <= k <= nums.length`

---

## ✅ 1437. Check If All 1's Are at Least Length K Places Away  
**Difficulty:** Easy

### 📝 Description
Given a **binary** array `nums` and an integer `k`, return `true` if **every pair of 1s** in `nums` are at least `k` positions apart; otherwise return `false`.

- “At least `k` apart” means the **gap** between indices of consecutive 1s is **≥ k** zeros in between (i.e., index difference **> k**).

---

### 📥 Input
- `nums`: list of integers, each `0` or `1`
- `k`: non-negative integer

### 📤 Output
- `bool`: `True` if all 1s are spaced by at least `k`, else `False`

---

### 🔍 Examples

#### Example 1
**Input:**  
`nums = [1,0,0,0,1,0,0,1]`, `k = 2`  
**Output:** `true`  
**Explanation:** Gaps between 1s are 3 and 3 (> 2).

#### Example 2
**Input:**  
`nums = [1,0,0,1,0,1]`, `k = 2`  
**Output:** `false`  
**Explanation:** The last two 1s are only 2 apart in indices → 1 zero between them (< 2).

---

### 💡 Approach
Track the **index of the last seen `1`**. For each new `1` at index `i`, check the distance:
- If `i - last_index <= k`, return `False`.
- Otherwise update `last_index = i` and continue.

Initialize `last_index = -k - 1` so the very first `1` always passes.

---

### ⏱️ Complexity
- **Time:** O(n)  
- **Space:** O(1)

---

### 🧪 Edge Cases
- `k = 0` → always `True` (no spacing required).
- No `1`s → `True`.
- All `1`s with insufficient gaps → `False`.

---

# 717. 1-bit and 2-bit Characters

## 🧩 Problem Summary
You are given a binary array `bits` representing characters encoded in one-bit and two-bit formats:

- **One-bit character:** represented by `0`
- **Two-bit character:** represented by `10` or `11`

The array always ends with `0`, and you must determine whether the last character is necessarily a one-bit character.

---

## 📘 Examples

**Example 1**
```
Input:  [1,0,0]
Output: true
Explanation: The only valid decoding is [10], [0].
```

**Example 2**
```
Input:  [1,1,1,0]
Output: false
Explanation: The valid decoding is [11], [10].
```

---

## ✅ Approach

We decode the array from left to right:

- If we see a `1`, it must start a **two-bit character**, so we skip 2 positions.
- If we see a `0`, it is a **one-bit character**, so we skip 1 position.
- We repeat until we reach (or pass) the last index.

If our pointer lands **exactly on the final index**, the last character is a one-bit character.

---

## 🧠 Time & Space Complexity

- **Time Complexity:** `O(n)` — single linear scan  
- **Space Complexity:** `O(1)` — constant extra space

---

## ✔️ Result
Return `True` if the final character must be a one-bit character, otherwise `False`.

---

# 2154. Keep Multiplying Found Values by Two

## 🧩 Problem Summary
You are given an integer array `nums` and an integer `original`.  
Your task is to repeatedly check whether `original` exists in `nums`.

### Process:
1. If `original` is found in `nums`, multiply it by 2.  
2. If not found, stop the process.  
3. Return the final value of `original`.

---

## 📘 Examples

**Example 1**
```
Input: nums = [5,3,6,1,12], original = 3
Output: 24

Explanation:
3 → found → becomes 6  
6 → found → becomes 12  
12 → found → becomes 24  
24 → not found → return 24
```

**Example 2**
```
Input: nums = [2,7,9], original = 4
Output: 4

Explanation:
4 not found → return 4
```

---

## ✅ Approach

- Convert `nums` to a **set** for `O(1)` lookup time.
- While `original` is found in the set → multiply it by 2.
- Stop when it is no longer present.

---

## 🧠 Time & Space Complexity

- **Time Complexity:** `O(n)`  
- **Space Complexity:** `O(n)` — for the set

---

## ✔️ Result
This function returns the final doubled value of `original` after repeating the search process.

---

# 1018. Binary Prefix Divisible By 5

## 🧩 Problem Summary
You are given a binary array `nums`, where each element is either `0` or `1`.

For each index `i`, define `xᵢ` as the **decimal value** of the binary number represented by `nums[0..i]`.  
You must return an array of booleans where:

```
answer[i] = True  if xᵢ is divisible by 5
answer[i] = False otherwise
```

---

## 📘 Examples

### Example 1
```
Input: nums = [0,1,1]
Binary prefixes:
- 0      → 0   → divisible → true
- 01     → 1   → false
- 011    → 3   → false

Output: [true, false, false]
```

### Example 2
```
Input: nums = [1,1,1]
Binary prefixes:
- 1   → 1   → false
- 11  → 3   → false
- 111 → 7   → false

Output: [false, false, false]
```

---

## ✅ Approach

Instead of constructing full binary numbers, which would grow too large, we track the **prefix modulo 5**.

Given:
```
current_value = x
next bit = b
```

The updated prefix value is:
```
x_new = (x * 2 + b) % 5
```

If `x_new == 0`, the prefix is divisible by 5.

This allows us to process all prefixes efficiently in **O(n)** time.

---

## 🧠 Complexity

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)` for the result list

---

## ✔️ Final Result

This algorithm efficiently determines which binary prefixes represent numbers divisible by 5 using only modulo arithmetic, ensuring optimal performance even for the largest inputs.

---

# 3512. Minimum Operations to Make Array Sum Divisible by K

## 🧩 Problem Summary
You are given:
- An integer array `nums`
- An integer `k`
- An allowed operation:  
  **Choose any index `i` and replace `nums[i]` with `nums[i] - 1`**

Each operation reduces the **total sum** of the array by exactly **1**.

Your task is to determine the **minimum number of operations** needed to make:

```
sum(nums) % k == 0
```

---

## 📘 Examples

### Example 1
```
Input: nums = [3, 9, 7], k = 5
Output: 4

Explanation:
Sum = 19 → 19 % 5 = 4
We need 4 operations to reach a sum divisible by 5.
```

### Example 2
```
Input: nums = [4, 1, 3], k = 4
Output: 0

Explanation:
Sum = 8, already divisible by 4.
```

### Example 3
```
Input: nums = [3, 2], k = 6
Output: 5

Explanation:
Sum = 5 → 5 % 6 = 5
We need 5 operations to reach 0 (divisible by 6).
```

---

## ✅ Key Insight

Every operation decreases the total sum by **1**.

Let:
```
S = sum(nums)
```

We want the smallest `t ≥ 0` such that:
```
(S - t) % k == 0
```

This rearranges to:
```
t % k == S % k
```

Thus the **minimum number of operations** is:
```
t = S % k
```

(When `S % k == 0`, the answer is `0`.)

---

## 🧠 Complexity

- **Time:** O(n)
- **Space:** O(1)

---

## ✔️ Summary
Because each operation decreases the total sum by exactly 1, the minimal number of operations needed to make the sum divisible by `k` is simply:

```
sum(nums) % k
```

This provides a simple and optimal 1-line solution.

---

# 3432 Count Partitions with Even Sum Difference --- LeetCode (Easy)

This problem asks you to count how many valid partitions of an array
result in an **even difference** between the sum of the left subarray
and that of the right subarray.

A partition at index *i* divides the array into: - Left: `nums[0..i]` -
Right: `nums[i+1..n-1]`

Both must be non-empty.

------------------------------------------------------------------------

## 🔍 Key Insight

Let: - `left_sum = sum(nums[0..i])` - `total = sum(nums)`

The difference simplifies to:

\[ left_sum - (total - left_sum) = 2 `\cdot `{=tex}left_sum - total \]

Because `2 × left_sum` is always even:

> The parity of the difference depends **only on the total sum**.

-   If `total` is **even** → the difference is always even → **all
    `n - 1` partitions are valid**.
-   If `total` is **odd** → the difference is always odd → **zero valid
    partitions**.

------------------------------------------------------------------------

## 🧠 Algorithm Summary

1.  Compute the total sum of the array.
2.  If total is odd → return `0`.
3.  Otherwise → return `n - 1`.

------------------------------------------------------------------------

## ⏱️ Complexity

-   **Time:** O(n)
-   **Space:** O(1)

------------------------------------------------------------------------

# Count Odd Numbers in an Interval Range --- LeetCode 1523 (Easy)

This problem asks you to count how many **odd numbers** appear in the
inclusive interval:

\[ \[low, high\] \]

Both endpoints are non‑negative integers, and the range may be as large
as 10⁹.

------------------------------------------------------------------------

## 🔍 Key Insight

The total number of integers in the interval is:

\[ high - low + 1 \]

Odd numbers occur every two integers.\
Therefore:

-   If **either** `low` or `high` is odd, the interval contains one
    extra odd number.
-   Otherwise, the count of odd numbers is simply half the interval
    length.

This leads to a constant‑time arithmetic solution.

------------------------------------------------------------------------

## 🧠 Formula

\[ `\text{odds}`{=tex} =
```{=tex}
\begin{cases}
\frac{high - low}{2} + 1, & \text{if low or high is odd} \\
\frac{high - low}{2}, & \text{otherwise}
\end{cases}
```
\]

------------------------------------------------------------------------

## ⏱️ Complexity

-   **Time:** O(1)\
-   **Space:** O(1)

------------------------------------------------------------------------

# 1925 Count Square Sum Triples — LeetCode (Easy)

A **square triple** `(a, b, c)` is defined as a triple of integers such that:

\[
a^2 + b^2 = c^2
\]

Given an integer `n`, the task is to count how many such triples satisfy:

\[
1 \le a, b, c \le n
\]

Note that `(a, b, c)` and `(b, a, c)` are considered **different** triples.

---

## 🔍 Key Idea

- Since `n ≤ 250`, a simple brute-force approach is efficient enough.
- We can:
  - Iterate over all possible `c` from `1` to `n`.
  - For each `c`, iterate over all `a` and `b` from `1` to `n`.
  - Count each pair `(a, b)` such that `a² + b² = c²`.

Alternatively, we can precompute all squares `i²` for `1 ≤ i ≤ n` and work with them directly to avoid recomputing powers repeatedly.

---

## 🧠 Optimization Possibility

Instead of three nested loops, you can:

- Precompute all squares in an array or set.
- Loop over `a` and `b`, compute `a² + b²`, and check if it equals some `c²` with `c ≤ n`.

Both versions are acceptable given the small constraint.

---

## ⏱️ Complexity

- **Time:** O(n²) or O(n³) depending on the implementation (both are fine for `n ≤ 250`)
- **Space:** O(n) if you store precomputed squares, otherwise O(1)

---

# 3606 Coupon Code Validator --- LeetCode (Easy)

This problem asks you to validate and filter a list of coupon codes
based on specific rules, then return the valid coupons in a required
sorted order.

You are given three arrays of equal length: - `code`: coupon
identifiers - `businessLine`: business category for each coupon -
`isActive`: whether the coupon is currently active

------------------------------------------------------------------------

## ✅ Coupon Validity Rules

A coupon is considered **valid** if **all** of the following conditions
hold:

1.  **Code format**
    -   Non‑empty
    -   Contains only alphanumeric characters (`a–z`, `A–Z`, `0–9`) or
        underscore (`_`)
2.  **Business line**
    -   Must be one of:
        -   `electronics`
        -   `grocery`
        -   `pharmacy`
        -   `restaurant`
3.  **Active status**
    -   `isActive[i]` must be `true`

------------------------------------------------------------------------

## 🔍 Sorting Requirements

Valid coupons must be returned: 1. Sorted by `businessLine` in this
exact order: - `electronics` - `grocery` - `pharmacy` - `restaurant` 2.
Sorted lexicographically by `code` **within each business line**

------------------------------------------------------------------------

## 🧠 Algorithm Summary

1.  Define the allowed business lines and their priority order.
2.  Filter coupons that:
    -   Are active
    -   Have a valid code format
    -   Belong to a valid business line
3.  Sort valid coupons by `(businessLineOrder, code)`.
4.  Return only the coupon codes.

------------------------------------------------------------------------

## ⏱️ Complexity

-   **Time:** O(n log n)
-   **Space:** O(n)

Efficient for the given constraints (`n ≤ 100`).

------------------------------------------------------------------------

# 2054 Two Best Non-Overlapping Events --- LeetCode (Medium)

This problem asks you to choose **at most two non-overlapping events**
such that the **sum of their values is maximized**.

Each event is represented as:

    [startTime, endTime, value]

Event times are **inclusive**, meaning if one event ends at time `t`,
the next event must start at **`t + 1` or later** to be considered
non-overlapping.

------------------------------------------------------------------------

## 🔍 Key Insight

You can attend: - **One event**, or - **Two events** that do not overlap
in time

A brute-force approach is too slow due to large constraints. Instead,
the problem can be solved efficiently by:

-   Sorting events by start time
-   For each event, finding the **best possible second event** that
    starts after it ends
-   Precomputing maximum values to avoid repeated scans

------------------------------------------------------------------------

## 🧠 Algorithm Summary

1.  Sort events by `startTime`.
2.  Build a suffix array where each position stores the maximum event
    value from that index to the end.
3.  For each event:
    -   Consider taking only this event
    -   Binary search to find the first event that starts at or after
        `endTime + 1`
    -   Combine values using the precomputed suffix maximum
4.  Track the maximum total value found.

------------------------------------------------------------------------

## ⏱️ Complexity

-   **Time:** O(n log n)
-   **Space:** O(n)

Efficient for up to 100,000 events.

------------------------------------------------------------------------

# 1351 Count Negative Numbers in a Sorted Matrix --- LeetCode (Easy)

This problem asks you to count how many **negative numbers** appear in a
matrix that is sorted in **non‑increasing order** both row‑wise and
column‑wise.

------------------------------------------------------------------------

## 🔍 Key Insight

Because the matrix is sorted: - Rows go from **larger to smaller** left
→ right - Columns go from **larger to smaller** top → bottom

This structure allows us to count negatives without checking every cell.

------------------------------------------------------------------------

## 🧠 Algorithm Strategy (O(m + n))

Start from the **top‑right corner** of the matrix:

-   If the current value is **negative**:
    -   All values **below** it in the same column are also negative
    -   Count them at once and move **left**
-   If the current value is **non‑negative**:
    -   Move **down** to find smaller values

This guarantees each row and column is visited at most once.

------------------------------------------------------------------------

## ⏱️ Complexity

-   **Time:** O(m + n)
-   **Space:** O(1)

Efficient and optimal given the matrix constraints.

------------------------------------------------------------------------

# 981 N-Repeated Element in Size 2N Array

## Problem Description

You are given an integer array `nums` with the following properties:

- The length of the array is `2 * n`
- The array contains exactly `n + 1` unique elements
- Exactly one element is repeated `n` times
- All other elements appear exactly once

Your task is to identify and return the element that is repeated `n` times.

---

## Examples

| Input | Output |
|------|--------|
| `[1, 2, 3, 3]` | `3` |
| `[2, 1, 2, 5, 3, 2]` | `2` |
| `[5, 1, 5, 2, 5, 3, 5, 4]` | `5` |

---

## Key Observations

- Since one element appears exactly half of the array size, it must repeat frequently.
- Given the constraints, the repeated element is guaranteed to appear close to itself in the array.
- This allows the problem to be solved efficiently without sorting.

---

## Approach

### Optimized Approach (Constant Extra Space)

- Compare each element with nearby elements at small index distances.
- The repeated element will always match one of these nearby elements.
- This method avoids using additional memory.

### Alternative Approach (Using Extra Memory)

- Keep track of elements that have already been seen.
- The first element encountered twice is the answer.

---

## Complexity Analysis

| Approach | Time Complexity | Space Complexity |
|--------|----------------|-----------------|
| Optimized (Index Comparison) | `O(n)` | `O(1)` |
| Set-Based | `O(n)` | `O(n)` |

---

## Constraints

- `2 ≤ n ≤ 5000`
- `nums.length = 2 * n`
- `0 ≤ nums[i] ≤ 10⁴`
- Exactly one element is repeated `n` times

---

# 1266. Minimum Time Visiting All Points

**Difficulty:** Easy  
**Topic:** Geometry, Greedy

## Problem Summary
You are given a list of points on a 2D plane and must visit them **in order**.  
In one second, you can move:
- 1 unit horizontally
- 1 unit vertically
- 1 unit diagonally (both directions at once)

Your task is to compute the **minimum time** required to visit all points sequentially.

## Key Insight
For two consecutive points:
- Let `dx = |x2 - x1|`
- Let `dy = |y2 - y1|`

The minimum time to move between them is:
```
max(dx, dy)
```

This is because diagonal moves reduce both `dx` and `dy` simultaneously.

## Algorithm
- Iterate through the points
- For each adjacent pair, add `max(dx, dy)` to the total time

## Constraints
- `1 ≤ n ≤ 100`
- Coordinates are between `-1000` and `1000`

## Example
**Input**
```
[[1,1],[3,4],[-1,0]]
```

**Output**
```
7
```

## Complexity
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

This is a simple greedy problem that relies on understanding diagonal movement efficiency.

---

# 1984. Minimum Difference Between Highest and Lowest of K Scores

## Problem Overview
You are given an array `nums` representing student scores and an integer `k`.  
Select scores of any `k` students such that the difference between the highest and lowest scores is minimized.

Return this minimum possible difference.

---

## Approach
1. Sort the array.
2. Use a sliding window of size `k`.
3. For each window, compute the difference between the maximum and minimum values.
4. Track and return the smallest difference.

---

## Algorithm
- If `k == 1`, the answer is `0`.
- Sort `nums`.
- Iterate through all contiguous subarrays of length `k`.
- Compute `nums[i + k - 1] - nums[i]` and keep the minimum.

---

## Complexity Analysis
- **Time Complexity:** `O(n log n)` due to sorting
- **Space Complexity:** `O(1)` (ignoring input storage)

---

## Example
```python
Input: nums = [9,4,1,7], k = 2
Output: 2
```
---

# 1200. Minimum Absolute Difference

## Problem Summary
Given an array of **distinct integers**, find all pairs of elements with the **minimum absolute difference**.  
Each pair must be in ascending order, and the final list of pairs should also be sorted.

## Approach
1. **Sort** the array.
2. Traverse adjacent elements to compute differences.
3. Track the **minimum difference** found.
4. Collect all pairs whose difference equals this minimum.

Sorting ensures the smallest absolute differences appear between neighboring elements.

## Complexity
- **Time Complexity:** `O(n log n)` due to sorting  
- **Space Complexity:** `O(1)` (excluding output)

## Example
Input:
[4,2,1,3]

Output:
[[1,2],[2,3],[3,4]]

## Notes
- Works efficiently for large inputs up to `10^5` elements.
- Guaranteed distinct integers simplify comparison logic.

---
