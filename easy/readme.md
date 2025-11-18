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
