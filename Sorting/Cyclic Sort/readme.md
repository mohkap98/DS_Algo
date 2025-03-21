# **Cyclic Sort Algorithm*

## 🚀 **Introduction**
Cyclic Sort is an in-place sorting algorithm used when dealing with numbers in a range **[1, N]**. It efficiently places each number at its correct index by swapping until all numbers are in order.

🔹 **Time Complexity:** `O(n)`  
🔹 **Space Complexity:** `O(1)`  
🔹 **Best Used For:** Finding missing or duplicate numbers in a range.

---

## 📌 **Algorithm Intuition**
1. **Iterate through the array**: For each number, check if it is at its correct position.
2. **Swap the number** to its correct position until all numbers are placed correctly.
3. **Move to the next index** and repeat the process.
4. **Repeat until the array is sorted** in `O(n)` time.

---

## 🎯 **Algorithm Steps**
1. Start with index `i = 0`.
2. If `arr[i]` is not at the correct index (`arr[i] != i + 1`), swap it with its correct position.
3. If `arr[i]` is already in the correct place, move `i` forward.
4. Repeat until the array is sorted.

---

## **💡 Example Walkthrough**
### **Input:** `arr = [3, 1, 5, 4, 2]`

🔄 **Step-by-step Swapping Process:**
```
Initial:  [3, 1, 5, 4, 2]
Step 1:   Swap 3 ↔ 5 → [5, 1, 3, 4, 2]
Step 2:   Swap 5 ↔ 2 → [2, 1, 3, 4, 5]
Step 3:   Swap 2 ↔ 1 → [1, 2, 3, 4, 5]
Final Sorted: [1, 2, 3, 4, 5]
```
✅ The array is sorted in **O(n)** time without extra space!

---

## 📌 **Cyclic Sort Python Implementation**
```python
from typing import List

def cyclic_sort(nums: List[int]) -> None:
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1
        if nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]  # Swap
        else:
            i += 1  # Move to next index

# Example usage
arr = [3, 1, 5, 4, 2]
cyclic_sort(arr)
print(arr)  # Output: [1, 2, 3, 4, 5]
```

---


