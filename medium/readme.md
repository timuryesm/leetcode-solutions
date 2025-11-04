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
