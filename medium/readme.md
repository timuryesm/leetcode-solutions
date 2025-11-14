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
