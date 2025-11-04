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
