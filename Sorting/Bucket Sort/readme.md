# Bucket Sort

## Introduction
**Bucket Sort** is a sorting algorithm that divides elements into multiple **buckets**, sorts each bucket individually (using another sorting algorithm like **insertion sort** or **quick sort**), and then concatenates the sorted buckets. It is efficient when the input data is **uniformly distributed** over a range.

## Algorithm
1. **Create Buckets**: Divide the input array into **n buckets**.
2. **Distribute Elements**: Assign each element to its appropriate bucket.
3. **Sort Each Bucket**: Sort elements within each bucket using a sorting algorithm.
4. **Concatenate Buckets**: Merge all sorted buckets to form the final sorted array.

## Time Complexity
| Case | Time Complexity |
|------|---------------|
| Best Case | O(n) |
| Average Case | O(n + k) |
| Worst Case | O(n^2) (if all elements go into one bucket) |

- `n` = Number of elements.
- `k` = Number of buckets.


## Applications
- Sorting **floating-point numbers** between `[0, 1]`.
- Distributing **grades or scores**.
- Efficient for **uniformly distributed data**.

## Limitations
- **Not efficient for non-uniform distributions**.
- **Choice of bucket count matters**.
- **Extra space required for buckets**.


