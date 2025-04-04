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


### 3️⃣ Counting Set Bits (Hamming Weight)
```python
 def countSetBits(n):
     count = 0
     while n:
         n &= (n - 1)  # Removes the rightmost 1-bit
         count += 1
     return count
```
- (1 << n) = 2^n . Generalised : n << x = n * 2^x

- Similarly, n >> x = n / 2^x

- if ( (x & (1 << i)) == 0 ) , then ith bit of x is set (i.e. 1)
  This will help you find subset using bit manipulation. 
  
- If we subtract a power of 2 number by 1 then all unset bits after the
  only set bit become set, and the set bit becomes unset.
  For example for 4 (100) and 16(10000), we get the following after subtracting 1 
      3 –> 011 
      15 –> 01111

   So, if( (n&(n-1)) == 0) - n is even
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

