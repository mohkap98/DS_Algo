# Bit Manipulation - Important Concepts for LeetCode

Bit manipulation is a powerful technique used in competitive programming and problem-solving on platforms like LeetCode. It allows you to perform operations at the binary level, often leading to optimized solutions.

## 📌 Key Bit Manipulation Concepts

### 1️⃣ Bitwise Operators
- `&` (AND): `a & b` sets bits to `1` only if both bits are `1`.
- `|` (OR): `a | b` sets bits to `1` if at least one bit is `1`.
- `^` (XOR): `a ^ b` sets bits to `1` if they are different.
- `~` (NOT): `~a` inverts all bits.
- `<<` (Left Shift): `a << n` shifts bits to the left, multiplying by `2^n`.
- `>>` (Right Shift): `a >> n` shifts bits to the right, dividing by `2^n`.

### 2️⃣ Checking If a Number is Power of Two
```python
 def isPowerOfTwo(n):
     return n > 0 and (n & (n - 1)) == 0
```

### 3️⃣ Counting Set Bits (Hamming Weight)
```python
 def countSetBits(n):
     count = 0
     while n:
         n &= (n - 1)  # Removes the rightmost 1-bit
         count += 1
     return count
```

### 4️⃣ Finding the Single Non-Repeating Element (XOR Trick)
```python
 def singleNumber(nums):
     result = 0
     for num in nums:
         result ^= num  # XOR cancels out duplicate numbers
     return result
```

### 5️⃣ Swapping Two Numbers Without Extra Space
```python
 def swap(a, b):
     a ^= b
     b ^= a
     a ^= b
     return a, b
```

### 6️⃣ Finding the Rightmost Set Bit (Lowest Set Bit)
```python
 def lowestSetBit(n):
     return n & -n  # Isolates the lowest set bit
```

### 7️⃣ Bitmasking for Subset Generation
```python
 def generateSubsets(arr):
     subsets = []
     n = len(arr)
     for mask in range(1 << n):
         subset = [arr[i] for i in range(n) if mask & (1 << i)]
         subsets.append(subset)
     return subsets
```

### 8️⃣ Checking If Two Numbers Have Opposite Signs
```python
 def oppositeSigns(x, y):
     return (x ^ y) < 0
```

## 🎯 Important LeetCode Problems on Bit Manipulation
1. **[Single Number](https://leetcode.com/problems/single-number/)** - XOR trick
2. **[Power of Two](https://leetcode.com/problems/power-of-two/)** - Checking if `n & (n-1) == 0`
3. **[Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)** - Counting set bits
4. **[Missing Number](https://leetcode.com/problems/missing-number/)** - XOR approach
5. **[Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)** - Finding common prefix
6. **[Reverse Bits](https://leetcode.com/problems/reverse-bits/)** - Bitwise reversal
7. **[Subsets](https://leetcode.com/problems/subsets/)** - Bitmasking

## 🛠️ Applications of Bit Manipulation
- Optimizing mathematical operations (multiplication, division, modulo)
- Efficient subset generation using bitmasking
- Data compression and encryption
- Memory-efficient boolean arrays (bitset)

Mastering bit manipulation is crucial for solving LeetCode problems efficiently and improving coding interview performance! 🚀

