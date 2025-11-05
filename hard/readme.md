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
