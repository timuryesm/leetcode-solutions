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

### ✨ Python Reference Solution
```python
class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        last = -k - 1  # ensures the first 1 always passes the distance check
        for i, v in enumerate(nums):
            if v == 1:
                if i - last <= k:
                    return False
                last = i
        return True
```

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

## 🧪 Code Implementation

```python
class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        n = len(bits)

        while i < n - 1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1

        return i == n - 1
```

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

## 🧪 Code Implementation

```python
class Solution(object):
    def findFinalValue(self, nums, original):
        nums_set = set(nums)

        while original in nums_set:
            original *= 2

        return original
```

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

## 🧪 Code Implementation

```python
class Solution(object):
    def prefixesDivBy5(self, nums):
        res = []
        cur = 0  # current prefix modulo 5

        for b in nums:
            cur = (cur * 2 + b) % 5
            res.append(cur == 0)

        return res
```

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

## 🧪 Code Implementation

```python
class Solution(object):
    def minOperations(self, nums, k):
        total = sum(nums)
        return total % k
```

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
