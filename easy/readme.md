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
