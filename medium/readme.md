## ✅ 151. Reverse Words in a String  
**Difficulty:** Medium

### 📝 Description
Given a string `s`, reverse the order of the words.

- A word is a sequence of non-space characters.
- Words are separated by at least one space.
- The result must **not** contain leading/trailing spaces.
- Multiple spaces between words must be reduced to **a single space**.

### 📥 Input
- `s`: string containing letters, digits, spaces

### 📤 Output
- A new string with words in reverse order

---

### 🔍 Examples

#### Example 1
Input:  s = “the sky is blue”
Output: “blue is sky the”


#### Example 2
Input:  s = “a good   example”
Output: “example good a”
Explanation: Collapse multiple spaces into one.

---

### ✅ Constraints
- `1 <= s.length <= 10^4`
- String contains letters, digits, and spaces
- At least one word exists

---

### 🔁 Follow-up
If the string is mutable in your language, can you do it **in-place with O(1) extra space**?

---

## ✅ 1578. Minimum Time to Make Rope Colorful  
**Difficulty:** Medium

### 📝 Description
You are given:

- String `colors` — color of each balloon
- Integer array `neededTime` — time to remove each balloon

Two adjacent balloons **cannot** have the same color.  
You may remove balloons to satisfy this rule.

Return the **minimum total time** required to make the rope colorful.

---

### 📥 Input
- `colors`: string of lowercase letters
- `neededTime`: integer array

### 📤 Output
- Integer representing minimum removal time

---

### 🔍 Examples

#### Example 1
Input: colors = “abaac”, neededTime = [1,2,3,4,5]
Output: 3
Explanation:
Remove balloon at index 2 (time = 3). No duplicates remain.

#### Example 2
Input: colors = “abc”, neededTime = [1,2,3]
Output: 0
Explanation: Already colorful.

#### Example 3
Input: colors = “aabaa”, neededTime = [1,2,3,4,1]
Output: 2
Explanation:
Remove balloons at indices 0 and 4 → 1 + 1 = 2

---

### ✅ Constraints
- `n == colors.length == neededTime.length`
- `1 <= n <= 10^5`
- `1 <= neededTime[i] <= 10^4`
- `colors` only lowercase English letters

---

## ✅ 3607. Power Grid Maintenance  
**Difficulty:** Medium  

### 📝 Description
You are given an integer `c` representing the number of power stations, each with a unique ID from `1` to `c` (1-based indexing).

These stations are connected via `n` bidirectional cables given as a 2D array `connections`, where  
`connections[i] = [ui, vi]` means there is a cable between stations `ui` and `vi`.

Stations that are directly or indirectly connected form a **power grid**.  
Initially, all stations are **online** (operational).

You are also given an array `queries`, where each query has one of two forms:

- `[1, x]`: a maintenance check request for station `x`  
  - If station `x` is **online**, it handles the check itself.  
  - If station `x` is **offline**, the check is handled by the **online station with the smallest ID** in the same grid.  
  - If no online stations exist in that grid, return `-1`.

- `[2, x]`: station `x` goes **offline** (non-operational).  

The **structure of the grid does not change** when stations go offline —  
offline nodes remain part of their original grid.

Return an array of integers representing results for all `[1, x]` queries in order.

---

### 📥 Input
- `c`: integer (number of stations)  
- `connections`: 2D list of bidirectional links between stations  
- `queries`: list of operations `[1, x]` or `[2, x]`

### 📤 Output
- Integer array — results of all maintenance queries `[1, x]`

---

### 🔍 Examples  

#### Example 1
Input:
c = 5
connections = [[1,2],[2,3],[3,4],[4,5]]
queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]

Output: [3,2,3]

**Explanation:**

- Initially, all stations `{1,2,3,4,5}` are online in one grid.  
- `[1,3]`: station 3 is online → resolves itself → output `3`  
- `[2,1]`: station 1 goes offline → remaining `{2,3,4,5}`  
- `[1,1]`: station 1 is offline → handled by smallest online ID `2`  
- `[2,2]`: station 2 goes offline → remaining `{3,4,5}`  
- `[1,2]`: station 2 offline → handled by smallest online ID `3`  

---

#### Example 2
Input:
c = 3
connections = []
queries = [[1,1],[2,1],[1,1]]

Output: [1,-1]

**Explanation:**

- No connections → each station is its own grid.  
- `[1,1]`: station 1 online → result `1`  
- `[2,1]`: station 1 goes offline  
- `[1,1]`: station 1 offline → no stations in grid → `-1`  

---

### ✅ Constraints
- `1 <= c <= 10^5`  
- `0 <= n == connections.length <= min(10^5, c * (c - 1) / 2)`  
- `connections[i].length == 2`  
- `1 <= ui, vi <= c`, `ui != vi`  
- `1 <= queries.length <= 2 * 10^5`  
- `queries[i].length == 2`  
- `queries[i][0] ∈ {1, 2}`  
- `1 <= queries[i][1] <= c`

---

## ✅ 474. Ones and Zeroes  
**Difficulty:** Medium  

### 📝 Description
You are given an array of binary strings `strs` and two integers `m` and `n`.

Find the size of the **largest subset** of `strs` such that the subset contains **at most** `m` zeros and **at most** `n` ones in total.  
(A subset means you choose some strings from `strs`; every chosen string contributes its zeros and ones to the totals.)

Return the **maximum number of strings** you can pick.

---

### 📥 Input
- `strs`: array of binary strings (consisting only of `'0'` and `'1'`)
- `m`: maximum number of zeros allowed
- `n`: maximum number of ones allowed

### 📤 Output
- An integer — the **maximum size** of a valid subset.

---

### 🔍 Examples

#### Example 1
**Input:**  
`strs = ["10","0001","111001","1","0"], m = 5, n = 3`  
**Output:** `4`  

**Explanation:**  
A largest valid subset is `{"10","0001","1","0"}` which uses 5 zeros and 3 ones.

---

#### Example 2
**Input:**  
`strs = ["10","0","1"], m = 1, n = 1`  
**Output:** `2`  

**Explanation:**  
A largest valid subset is `{"0","1"}`.

---

### ✅ Constraints
- `1 <= strs.length <= 600`  
- `1 <= strs[i].length <= 100`  
- Each `strs[i]` contains only `'0'` and `'1'`  
- `1 <= m, n <= 100`

---

### 💡 Note
This is a **0/1 knapsack** variant with **two capacities** (zeros and ones).  
A common solution uses 2D DP: `dp[i][j]` = max strings using at most `i` zeros and `j` ones.

---

## ✅ 3228. Maximum Number of Operations to Move Ones to the End  
**Difficulty:** Medium

### 📝 Description
You are given a **binary string** `s`. You may repeat the following operation any number of times:

- Choose an index `i` with `i + 1 < s.length` such that `s[i] == '1'` and `s[i + 1] == '0'`.
- **Move** the character `s[i]` (that `'1'`) to the **right** until it reaches the **end of the string** or the position **just before the next `'1'`**.  
  - Example: for `s = "010010"`, choosing `i = 1` yields `"000110"`.

Return the **maximum number of operations** you can perform.

---

### 📥 Input
- `s`: a binary string (characters are `'0'` or `'1'`)

### 📤 Output
- An integer — the maximum number of operations possible

---

### 🔍 Examples

#### Example 1
Input:  
`s = "1001101"`  
Output:  
`4`  
Explanation (one optimal sequence):
1. `1001101` → choose `i=0` → `0011101`  
2. `0011101` → choose `i=4` → `0011011`  
3. `0011011` → choose `i=3` → `0010111`  
4. `0010111` → choose `i=2` → `0001111`

#### Example 2
Input:  
`s = "00111"`  
Output:  
`0`

---

### ✅ Constraints
- `1 <= s.length <= 10^5`  
- `s[i] ∈ {'0', '1'}`

---

## ✅ 2536. Increment Submatrices by One  
**Difficulty:** Medium  

### 📝 Description
You are given an integer `n`, representing an initial `n x n` matrix `mat` filled with zeros, and a list of queries `queries`, where each query is `[r1, c1, r2, c2]`.  
For each query, add `1` to every cell inside the submatrix with **top-left** `(r1, c1)` and **bottom-right** `(r2, c2)` (inclusive).  
Return the final matrix after applying all queries.

---

### 💡 Key Idea (2D Difference Array)
A naive per-cell increment per query is too slow (`O(q * n^2)` in the worst case).  
Instead, use a **2D difference array** with prefix sums:

For each query `[r1, c1, r2, c2]`, apply:
- `diff[r1][c1] += 1`
- `diff[r1][c2 + 1] -= 1`
- `diff[r2 + 1][c1] -= 1`
- `diff[r2 + 1][c2 + 1] += 1`

Then:
1. Take prefix sums row-wise.
2. Take prefix sums column-wise.
3. Trim back to `n x n` to get the result.

This turns each query into **O(1)** work and reconstruction into **O(n²)**.

---

### ✅ Algorithm
1. Initialize a `(n+1) x (n+1)` `diff` matrix with zeros.
2. For each query, mark its corners in `diff` as above.
3. Compute horizontal prefix sums (rows), then vertical prefix sums (columns).
4. Extract the top-left `n x n` as the answer.

---

### ⏱️ Complexity
- **Time:** `O(n² + q)` — each query is O(1), plus two passes over the grid.
- **Space:** `O(n²)` for the difference matrix.

---

### 🧩 Edge Cases
- Single query covering the whole matrix.
- Queries that are single cells (`r1 == r2` and `c1 == c2`).
- `n = 1`.
- Many small overlapping queries.

---

### 🧪 Example
**Input:**  
`n = 3`, `queries = [[1,1,2,2],[0,0,1,1]]`  
**Output:**  
`[[1,1,0],[1,2,1],[0,1,1]]`

---

## ✅ 3234. Count the Number of Substrings With Dominant Ones
**Difficulty:** Medium

### 📝 Description
You are given a binary string `s`. A substring has **dominant ones** if:
```
#ones >= (#zeros)^2
```
Return the **number of substrings** of `s` that satisfy this property.

---

### 💡 Approach (High Level)
1. **All-ones substrings** (no zeros) are always valid. Count them in O(n) by summing lengths of 1-runs.
2. For substrings with **z ≥ 1 zeros**, the minimal length must be at least `z*(z+1)` (since `ones >= z^2` ⇒ `length >= z^2 + z`).  
   - Precompute positions of all zeros and slide a window of `z` zeros across them.
   - For each window, compute how many ways you can **extend left/right** while keeping the condition:
     - Let `left_choices` be the free characters before the first zero in the window.
     - Let `right_choices` be the free characters after the last zero in the window.
     - Let `core_len` be the length from first to last zero (inclusive).
     - You need `a + b >= Lmin - core_len` with `a ∈ [0, left_choices-1]`, `b ∈ [0, right_choices-1]`.
     - Count such pairs in **O(1)** with a small combinatorial helper.
3. Only consider `z` up to `Zmax = floor((sqrt(1+4n)-1)/2)`, because larger `z` cannot meet the length bound inside a length-`n` string.
4. Total time is about **O(n · Zmax)** ≈ **O(n√n)**, space **O(n)**.

> 🔧 **Python 2 note:** If your judge runs Python 2, replace `math.isqrt` with `math.sqrt` and guard the floor computation.

---

### ⏱️ Complexity
- **Time:** `O(n√n)` (since `Zmax = Θ(√n)`)
- **Space:** `O(n)`

---

### 🧪 Examples
**Example 1**
```
Input:  s = "00011"
Output: 5
Explanation substrings with dominant ones:
"1" (x2), "01", "11", "011"
```

**Example 2**
```
Input:  s = "101101"
Output: 16
```

---

## 1513. Number of Substrings With Only 1s
**Difficulty:** Medium

### 📝 Problem
Given a binary string `s`, return the number of substrings that contain **only** `'1'` characters.  
Because the count can be large, return the result modulo **1e9+7**.

### 💡 Intuition
A contiguous run of `'1'`s of length `L` contributes:
```
1 + 2 + ... + L = L * (L + 1) / 2
```
substrings consisting only of `'1'`.  
So we just scan the string, accumulate the length of the current run of `'1'`s, and add the triangular number each time a `'0'` breaks the run (and once at the end).

### ✅ Algorithm
1. Initialize `ans = 0`, `run = 0`.
2. For each character:
   - If it's `'1'`, increment `run`.
   - If it's `'0'`, add `run * (run + 1) // 2` to `ans` and reset `run` to 0.
3. After the loop, add the contribution of the final run.
4. Return `ans % MOD`.

### ⏱️ Complexity
- **Time:** `O(n)` — single pass.
- **Space:** `O(1)` — constant extra space.

### 🧪 Examples
- `s = "0110111"` → runs: [2, 3] → `2*3/2 + 3*4/2 = 3 + 6 = 9`
- `s = "101"` → runs: [1, 1] → `1 + 1 = 2`

---

# 1930. Unique Length-3 Palindromic Subsequences

## 🧩 Problem Summary
You are given a string `s` containing only lowercase English letters.  
Your task is to count how many **unique** palindromic subsequences of **length 3** appear in `s`.

A length‑3 palindrome must look like:

```
c x c
```

- The first and last characters must be **the same**.
- The middle character can be **any character**.
- A subsequence does **not** need to be contiguous.
- Identical palindromes formed in different ways count **only once**.

---

## 📘 Examples

### Example 1
```
Input: s = "aabca"
Output: 3

Unique palindromes:
- "aba"
- "aaa"
- "aca"
```

### Example 2
```
Input: s = "adc"
Output: 0
```

### Example 3
```
Input: s = "bbcbaba"
Output: 4

Unique palindromes:
- "bbb"
- "bcb"
- "bab"
- "aba"
```

---

## ✅ Approach

For each letter `'a'` to `'z'`:

1. Find its **first position** and **last position** in the string.
2. If the letter appears **at least twice**, then:
   - Any **distinct** character between those two positions can form  
     a palindrome `c x c`.
3. Count these distinct middle characters.
4. Sum results over all 26 letters.

This avoids searching all subsequences and works in **linear time**.

---

## 🧠 Complexity

- **Time Complexity:** `O(n)`  
- **Space Complexity:** `O(1)` (only 26 characters tracked)

---

## ✔️ Result

This solution efficiently counts all *unique* palindromic subsequences of length 3  
by identifying valid outer characters and scanning distinct middle characters.

---

# 1015. Smallest Integer Divisible by K

## 🧩 Problem Summary
Given a positive integer `k`, find the **length** of the smallest positive integer made only of digit `'1'` that is divisible by `k`.

Such numbers are called **repunits**, e.g.:
```
1, 11, 111, 1111, ...
```

If no such repunit exists, return **-1**.

---

## 📘 Examples

### Example 1
```
Input: k = 1
Output: 1
```

### Example 2
```
Input: k = 2
Output: -1
```

### Example 3
```
Input: k = 3
Output: 3
```

---

## ❗ Key Observations

### ➤ Repunits cannot be divisible by 2 or 5  
Any number formed only of '1's is **odd** and never ends with 0 or 5.  
Thus:

```
If k % 2 == 0 or k % 5 == 0 → return -1
```

### ➤ Track remainder instead of constructing the number  
To avoid overflow:

```
Rₙ = (Rₙ₋₁ * 10 + 1) % k
```

If `Rₙ == 0`, then the repunit of length `n` is divisible by `k`.

### ➤ Check only up to k iterations  
There are only `k` possible remainders (`0..k-1`).  
After `k` steps, if we haven’t seen remainder 0, we are in a cycle → no solution.

---

## 🧠 Complexity

- **Time Complexity:** `O(k)`  
- **Space Complexity:** `O(1)`  

Efficient for all valid constraints (`k ≤ 100000`).

---

## ✔️ Summary
This solution uses modular arithmetic and the pigeonhole principle to find the smallest repunit divisible by `k` without ever constructing large integers.

---

# 3381. Maximum Subarray Sum With Length Divisible by K

## 🧩 Problem Summary
You are given an integer array `nums` and an integer `k`.

Your goal is to compute the **maximum possible sum of any subarray whose length is divisible by `k`**.

A subarray is a contiguous segment of the array.

---

## 📘 Examples

### Example 1
```
Input: nums = [1, 2], k = 1
Output: 3

Explanation:
The subarray [1, 2] has length 2 (divisible by 1) and sum = 3.
```

### Example 2
```
Input: nums = [-1, -2, -3, -4, -5], k = 4
Output: -10

Explanation:
The subarray [-1, -2, -3, -4] has length 4 and is the best possible.
```

### Example 3
```
Input: nums = [-5, 1, 2, -3, 4], k = 2
Output: 4

Explanation:
The best valid subarray is [1, 2, -3, 4] with length 4.
```

---

## ✅ Key Insight

Let:
```
pref[i] = sum of nums[0..i-1]
```

Then:
```
sum(nums[l..r]) = pref[r+1] - pref[l]
length = r - l + 1
```

We need:
```
(r - l + 1) % k == 0
⇔ (r + 1) % k == l % k
```

Thus, valid subarrays correspond to **pairs of prefix indices with the same modulo k**.

For each remainder class, we keep the **minimum prefix sum** seen so far.

For prefix index `i` with sum `pref[i]`:
```
candidate_sum = pref[i] - minPref[i % k]
```

We track the maximum such value.

---

## 🧠 Complexity

- **Time Complexity:** O(n)
- **Space Complexity:** O(k)

Efficient for n up to 2 × 10⁵.

---

## ✔️ Summary
This prefix-sum + modulo technique efficiently finds the best subarray whose size is divisible by `k`.  
It handles negative numbers and works in linear time, making it perfect for large inputs.

---

# 3623. Count Number of Trapezoids I

## 🧩 Problem Summary
You are given an array of points on a 2D plane.  
Your task is to count how many **horizontal trapezoids** can be formed by choosing **four distinct points**.

A **horizontal trapezoid** is a convex quadrilateral with at least one pair of **horizontal** (parallel to x-axis) sides.

Return the result modulo **1,000,000,007**.

---

## 🧠 Key Insight

To form a horizontal trapezoid, we must pick:

- **Two points from y = y₁**
- **Two points from y = y₂**, where `y₁ ≠ y₂`

These pairs form two horizontal segments → which guarantees a trapezoid.

Thus the problem reduces to:

### ✔️ Step 1 — Group points by y‑coordinate  
If a y-level has `cnt` points, then the number of horizontal segments is:

```
C(cnt, 2) = cnt * (cnt - 1) / 2
```

Call this value `a_i`.

### ✔️ Step 2 — Every trapezoid = picking one segment from level i and one from level j  
Total trapezoids:

\[
\sum_{i < j} a_i \cdot a_j
\]

We compute this efficiently using:

\[
rac{(\sum a_i)^2 - \sum a_i^2}{2}
\]

---

## 📘 Example

### Example 1
```
Input:
points = [[1,0],[2,0],[3,0],[2,2],[3,2]]

Output: 3
```

Horizontal segments:
- y=0 → C(3,2)=3
- y=2 → C(2,2)=1

Total = 3×1 = 3 trapezoids.

---

## 📈 Complexity

- **Time:** O(n)  
- **Space:** O(n) for grouping y-coordinates  

Efficient for up to **100,000** points.

---

## ✔️ Summary

This problem becomes a clean combinatorics task:

1. Count all horizontal segments on each y-level: `a_i = C(cnt_i, 2)`
2. Any pair of horizontal segments from distinct y-levels forms a trapezoid.
3. Count combinations with:

\[
rac{(\sum a_i)^2 - \sum a_i^2}{2}
\]

This gives an optimal and elegant O(n) solution.

---

# 2211 Count Collisions on a Road --- LeetCode (Medium)

This problem asks you to determine how many **collisions** occur among
cars moving on an infinitely long road.\
Each car can move **Left (L)**, **Right (R)**, or **Stay (S)**. After
any collision, involved cars become stationary.

------------------------------------------------------------------------

## 🚗 Key Insight

Instead of simulating movement, we use structural observations:

### 1. Cars that will **never** collide:

-   Leading `'L'` cars at the far **left** move outward.
-   Trailing `'R'` cars at the far **right** move outward.

### 2. All moving cars in the **middle segment** will eventually collide:

Once the outer non-colliding cars are removed, every remaining `'L'` or
`'R'` car must collide with something.

Thus:

> In the middle substring, each non‑stationary car contributes **exactly
> 1 collision**.

------------------------------------------------------------------------

## 🧠 Algorithm Overview

1.  Trim leading `'L'` cars.
2.  Trim trailing `'R'` cars.
3.  Count characters in the remaining substring that are not `'S'`.

The result is the total number of collisions.

------------------------------------------------------------------------

## ⏱️ Complexity

-   **Time:** O(n)\
-   **Space:** O(1)

------------------------------------------------------------------------

# 3578 Count Partitions With Max--Min Difference at Most K --- LeetCode (Medium)

This problem asks you to count the number of ways to partition an array
into one or more **contiguous segments**, such that in every segment:

\[ `\max`{=tex}(segment) - `\min`{=tex}(segment) `\le `{=tex}K \]

Because the number of valid partitions can be large, the result is
returned modulo **10⁹ + 7**.

------------------------------------------------------------------------

## 🔍 Key Insight

For each index *j*, consider all starting indices *s* such that the
segment `nums[s..j]` satisfies:

\[ `\max`{=tex}(nums\[s..j\]) - `\min`{=tex}(nums\[s..j\]) `\le `{=tex}K
\]

Let `dp[i]` represent the number of valid partitions of the prefix
`nums[0..i-1]`. Then:

\[ dp\[j+1\] = `\sum`{=tex}\_{s=L_j}\^{j} dp\[s\] \]

where `L_j` is the smallest valid starting point for a segment ending at
`j`.

------------------------------------------------------------------------

## 🧠 Efficient Strategy

To avoid recomputing max and min for each segment:

-   Maintain a **sliding window** `[l..j]`.
-   Use **two monotonic deques**:
    -   One tracks the maximum in the window.
    -   One tracks the minimum.
-   Increase `l` while the window violates `max - min ≤ K`.
-   Use **prefix sums** to compute the DP range sum efficiently.

This reduces the complexity from O(n²) to **O(n)**.

------------------------------------------------------------------------

## ⏱️ Complexity

-   **Time:** O(n)\
-   **Space:** O(n)

------------------------------------------------------------------------

# 3531 Count Covered Buildings --- LeetCode (Medium)

This problem asks you to determine how many buildings in an **n × n**
city grid are *covered*.\
A building located at coordinates **(x, y)** is considered *covered* if
it has at least one other building:

-   **Left** of it in the same row\
-   **Right** of it in the same row\
-   **Above** it in the same column\
-   **Below** it in the same column

All building coordinates are unique.

------------------------------------------------------------------------

## 🔍 Key Insight

Instead of checking every building pair, we only need the **minimum and
maximum positions** in each row and column.

For a building at `(x, y)` to be covered:

-   Its `y` must satisfy:\
    `row_min[x] < y < row_max[x]`\
-   Its `x` must satisfy:\
    `col_min[y] < x < col_max[y]`

If both conditions hold, the building has neighbors in all four
directions.

------------------------------------------------------------------------

## 🧠 Algorithm Summary

1.  Create arrays:
    -   `row_min[x]`, `row_max[x]`
    -   `col_min[y]`, `col_max[y]`
2.  First pass over all buildings:
    -   Update row and column min/max values.
3.  Second pass:
    -   Count how many buildings satisfy the four-direction constraint.

------------------------------------------------------------------------

## ⏱️ Complexity

-   **Time:** O(m), where m = number of buildings\
-   **Space:** O(n)

------------------------------------------------------------------------

# 3433  Count Mentions Per User --- LeetCode(Medium)

This problem simulates a **user‑mention system** where users can
temporarily go offline and messages can mention users in different ways.

You are given: - `numberOfUsers`: total users, labeled from `0` to
`numberOfUsers - 1` - `events`: a list of timestamped events

The task is to return how many times **each user is mentioned** across
all message events.

------------------------------------------------------------------------

## 📌 Event Types

### MESSAGE

    ["MESSAGE", timestamp, mentions_string]

The `mentions_string` may contain: - `id<number>` → mentions a specific
user (counts even if the user is offline) - `ALL` → mentions all users
(online and offline) - `HERE` → mentions only users who are online at
that timestamp

Each mention counts separately, including duplicates in the same
message.

------------------------------------------------------------------------

### OFFLINE

    ["OFFLINE", timestamp, user_id]

-   The user becomes offline at `timestamp`
-   They automatically return online at `timestamp + 60`
-   Status changes are processed **before** any message at the same
    timestamp

------------------------------------------------------------------------

## 🔍 Key Insight

To solve this problem:

-   Track each user's offline window using a timestamp (`offline_until`)
-   Process events in chronological order
-   Ensure OFFLINE events are handled before MESSAGE events at the same
    time
-   Apply mention rules depending on the message token (`id`, `ALL`,
    `HERE`)

Since constraints are small, iterating over users is efficient.

------------------------------------------------------------------------

## 🧠 Algorithm Summary

1.  Sort events by `(timestamp, type)` with OFFLINE first.
2.  Maintain an array to track when users come back online.
3.  For each MESSAGE event:
    -   Count mentions based on the token rules.
4.  Return the final mention counts.

------------------------------------------------------------------------

## ⏱️ Complexity

-   **Time:** O(events × numberOfUsers)
-   **Space:** O(numberOfUsers)

------------------------------------------------------------------------

# 955 Delete Columns to Make Sorted II --- LeetCode (Medium)

This problem asks you to remove the **minimum number of columns** from
an array of equal‑length strings so that the resulting strings are in
**lexicographic (non‑decreasing) order**.

All deletions apply to **every string** at the same column indices.

------------------------------------------------------------------------

## 🔍 Key Insight

We process the columns **from left to right** and decide greedily
whether to keep or delete each column.

For adjacent string pairs `(strs[i], strs[i+1])`: - Some pairs may
already be confirmed as ordered based on previously kept columns. - A
new column is **invalid** if it causes any *unresolved* pair to violate
lexicographic order.

If keeping a column would break ordering for even one unresolved pair,
that column must be deleted.

------------------------------------------------------------------------

## 🧠 Algorithm Summary

1.  Maintain an array tracking which adjacent string pairs are already
    ordered.
2.  Iterate through columns from left to right:
    -   If the column breaks order for any unresolved pair → delete it.
    -   Otherwise, keep it and mark newly resolved pairs.
3.  Count how many columns were deleted.

This greedy approach guarantees the minimum number of deletions.

------------------------------------------------------------------------

## ⏱️ Complexity

-   **Time:** O(n × m), where
    -   `n` = number of strings\
    -   `m` = length of each string
-   **Space:** O(n)

Efficient for the given constraints.

------------------------------------------------------------------------
