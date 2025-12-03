## ✅ 679. 24 Game  
**Difficulty:** Hard  

### 📝 Description
You are given an integer array `cards` of length 4. Each value is between `1` and `9`.

Using all four numbers exactly once, determine whether you can form a mathematical expression equal to **24**, using:

- Operators: `+`, `-`, `*`, `/`
- Parentheses: `(`, `)`

### 📌 Rules
- Division `/` is **real division**, not integer division  
  - Example: `4 / (1 - 2 / 3) = 12`
- Only **binary operations** are allowed  
  - Unary `-` is **not allowed** (`-1 - 1 - 1 - 1` ❌)
- **Concatenation of numbers is not allowed**  
  - Example: `"12 + 12"` ❌ for cards `[1,2,1,2]`

Return `true` if you can get the value `24`, otherwise return `false`.

---

### 🔍 Examples

#### Example 1
Input:  cards = [4,1,8,7]
Output: true
Explanation: (8 - 4) * (7 - 1) = 24

#### Example 2
Input:  cards = [1,2,1,2]
Output: false

---

### ✅ Constraints
- `cards.length == 4`
- `1 <= cards[i] <= 9`

---

## ✅ 3321. Find X-Sum of All K-Long Subarrays II  
**Difficulty:** Hard

### 📝 Description
You are given an integer array `nums` of length `n` and two integers `k` and `x`.

For each contiguous subarray of length `k`, compute the **x-sum**:

1. Count frequencies of all elements in the subarray  
2. Keep only the `x` most frequent values  
   - If frequency ties, keep the **larger value**
3. Sum all kept values (respecting their counts)
4. If fewer than `x` distinct values exist, return the **sum of the whole subarray**

Return an array `answer` where `answer[i]` is the x-sum of subarray `nums[i..i+k-1]`.

---

### 📥 Input
- `nums`: integer array
- `k`: subarray size  
- `x`: number of most frequent values to consider

### 📤 Output
- Integer array of x-sums for each sliding window

---

### 🔍 Examples

#### Example 1
Input:  nums = [1,1,2,2,3,4,2,3], k = 6, x = 2
Output: [6,10,12]

**Explanation:**

- `[1,1,2,2,3,4]` → keep `1,2` → `1+1+2+2 = 6`  
- `[1,2,2,3,4,2]` → keep `2,4` → `2+2+2+4 = 10`  
- `[2,2,3,4,2,3]` → keep `2,3` → `2+2+2+3+3 = 12`

---

#### Example 2
Input:  nums = [3,8,7,8,7,5], k = 2, x = 2
Output: [11,15,15,15,12]

When `k == x`, x-sum = sum of the window.

---

### ✅ Constraints
- `nums.length == n`
- `1 <= n <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= x <= k <= n`

---

# 757. Set Intersection Size At Least Two

## 🧩 Problem Summary
You are given a list of intervals `intervals[i] = [start, end]`.  
You must choose a set of integers such that **each interval contains at least two integers** from this set.

Your goal: **Return the minimum possible size** of such a set.

---

## 📘 Examples

### Example 1
```
Input: intervals = [[1,3],[3,7],[8,9]]
Output: 5
Explanation: A valid minimal set is [2, 3, 4, 8, 9].
```

### Example 2
```
Input: intervals = [[1,3],[1,4],[2,5],[3,5]]
Output: 3
Explanation: A valid minimal set is [2, 3, 4].
```

### Example 3
```
Input: intervals = [[1,2],[2,3],[2,4],[4,5]]
Output: 5
Explanation: A valid minimal set is [1, 2, 3, 4, 5].
```

---

## ✅ Greedy Strategy (Optimal)
To minimize the number of chosen integers:

1. **Sort intervals** by:
   - `end` ascending  
   - if equal, `start` descending  
   This handles nested intervals correctly.

2. Maintain two points:
   - `a` = largest chosen number  
   - `b` = second largest chosen number  

3. For each interval `[l, r]`:
   - If the interval currently includes **0** of our chosen numbers → add two: `r-1`, `r`
   - If it includes **1** of our chosen numbers → add one: `r`
   - If it includes **2 or more** → do nothing

This ensures the smallest possible set.

---

## 🧠 Time & Space Complexity

- **Time Complexity:** `O(n log n)` (sorting)
- **Space Complexity:** `O(1)` extra

---

## ✔️ Result
This algorithm computes the **minimum number of integers** needed so that every interval contains **at least two** of them.

---

# 2435. Paths in Matrix Whose Sum Is Divisible by K

## 🧩 Problem Summary
You are given an `m × n` integer matrix `grid` and an integer `k`.

You start at **(0,0)** and can move only **right** or **down** until reaching **(m−1, n−1)**.  
Your task: count the number of paths whose **sum of values** is divisible by `k`.

Return the result modulo **1,000,000,007**.

---

## 📘 Examples

### Example 1
```
Input:
grid = [[5,2,4],
        [3,0,5],
        [0,7,2]], k = 3

Output: 2
```

### Example 2
```
Input:
grid = [[0,0]], k = 5
Output: 1
```

### Example 3
```
Input:
grid = [[7,3,4,9],
        [2,3,6,2],
        [2,3,7,0]], k = 1

Output: 10
```

---

## ✅ Approach: Dynamic Programming with Remainders

We define a DP where:

```
dp[i][j][r] = #paths to cell (i,j) such that the path sum % k == r
```

### Transitions
You can come from:
- Top: `(i−1, j)`
- Left: `(i, j−1)`

Let:
```
val = grid[i][j] % k
new_r = (r + val) % k
```

Then:
```
dp[i][j][new_r] += dp[i−1][j][r]
dp[i][j][new_r] += dp[i][j−1][r]
```

Finally:
```
answer = dp[m−1][n−1][0]
```

---

## 🧠 Complexity
- **Time:** `O(m × n × k)`
- **Space:** `O(m × n × k)`
- Works under constraint `m × n ≤ 50,000`.

---

## ✔️ Summary
This solution uses a modulo-state DP that efficiently counts paths with sum divisible by `k`, avoiding overflow and satisfying hard constraints.

---

# 2872. Maximum Number of K-Divisible Components

## 🧩 Problem Summary
You are given an undirected tree with `n` nodes labeled from `0` to `n−1`.

- `edges[i] = [a, b]` indicates an undirected edge between nodes `a` and `b`.
- Each node `i` has a value `values[i]`.
- You are also given an integer `k`.

You may **remove any set of edges** such that every resulting connected component has a **total value divisible by `k`**.

Your goal is to return the **maximum number of such components**.

---

## 📘 Examples

### Example 1
```
Input:
n = 5
edges = [[0,2],[1,2],[1,3],[2,4]]
values = [1,8,1,4,4]
k = 6

Output: 2
```

### Example 2
```
Input:
n = 7
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
values = [3,0,6,1,5,2,1]
k = 3

Output: 3
```

---

## ✅ Key Insight

This is a **tree DP** problem using **DFS + modulo accumulation**.

For each node:
1. Compute the subtree sum modulo `k`.
2. For each child:
   - If child remainder = `0`, that subtree already forms a valid component → we increase the count and **do not propagate** its sum upward.
   - Otherwise, we accumulate its remainder upward.

Because the full tree sum is guaranteed divisible by `k`, the root subtree is always valid.

---

## 🧠 Complexity

- **Time:** `O(n)`
- **Space:** `O(n)`

Efficient for `n ≤ 30,000`.

---

## ✔️ Summary
We process the tree bottom-up:

- Child subtree divisible by `k` → becomes its own component.
- Other subtree remainders bubble to the parent.
- Final count is the number of divisible subtrees.

This produces the maximum possible number of `k`-divisible components.

---

# 2141. Maximum Running Time of N Computers

## 🧩 Problem Summary
You are given:
- `n` computers that must run **simultaneously**
- A list `batteries` where each element represents how many minutes that battery can power a computer

You may:
- Insert **one battery per computer**
- Swap batteries between computers at any integer moment (swapping takes **zero time**)
- Not recharge batteries

Your task:
> Compute the **maximum number of minutes** all `n` computers can run at the same time.

---

## 📘 Example 1
```
n = 2
batteries = [3, 3, 3]
Output: 4
```
By swapping drained batteries with fresh ones, both computers run for 4 minutes.

---

## 📘 Example 2
```
n = 2
batteries = [1, 1, 1, 1]
Output: 2
```
Each computer cycles through two batteries → 2 minutes total.

---

## ✅ Key Insight

Since we can swap batteries *freely*, we only care about **total usable battery time**, not which battery goes to which computer.

To check whether we can run all computers for `T` minutes:

- Each battery contributes at most `min(battery, T)`
- Total needed: `n * T`

Condition:
```
sum(min(b, T) for b in batteries)  >=  n * T
```

We binary-search for the maximum `T` satisfying this.

### Search Range
```
0 ≤ T ≤ sum(batteries) // n
```

---

## 🧠 Complexity Analysis

- **Time:** `O(m log(sum(batteries)))`
- **Space:** `O(1)`

Efficient for up to `10^5` batteries.

---

## ✔️ Summary

This problem is solved via **binary search on running time**, using the condition:

```
sum(min(b, T)) ≥ n * T
```

Swapping batteries freely turns the problem into testing whether total available energy can sustain all computers for a given time.

---

# 3625 Count Number of Trapezoids II --- LeetCode (Hard)

This problem asks to count how many **unique trapezoids** can be formed
from a given set of points on the Cartesian plane. A *trapezoid* is
defined as a **convex quadrilateral with at least one pair of parallel
sides**.

### 🔍 Key Idea

A trapezoid requires at least one pair of **parallel segments** lying on
**different supporting lines**. The high‑level strategy:

1.  Enumerate all point pairs to generate all segments.
2.  Compute each segment's **slope** and **line identifier** to detect
    parallel but non‑collinear pairs.
3.  Count valid parallel segment pairs using combinatorics.
4.  Correct for overcounted special cases (e.g., parallelogram-like
    symmetries) by grouping segments by midpoint.

### 🧠 Algorithm Summary (Abstract)

-   Group segments by slope and supporting line.
-   Count pairs of parallel segments on distinct lines.
-   Subtract configurations counted multiple times using midpoint
    groups.

### ⏱️ Complexity

-   **Time:** O(n²)
-   **Space:** O(n²)

Efficient for up to 500 input points.

---
