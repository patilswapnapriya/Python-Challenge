# Day X: Find Largest Number – Notes

## 🔹 Concept
To find the **largest number** in a list:
1. Start by assuming the **first element** is the largest.
2. Traverse the list one element at a time.
3. If you find an element greater than the current largest, update it.
4. At the end, the variable holds the maximum value.

---

## 🔹 Step-by-Step Example
For `[3, 7, 2, 9, 5]`:
- Start: largest = 3
- Compare 7 → update largest = 7
- Compare 2 → no change
- Compare 9 → update largest = 9
- Compare 5 → no change
- Final Answer = 9 ✅

---

## 🔹 Solutions in Python

### ✅ 1. Using Loop (manual method)
```python
def find_largest(nums):
    largest = nums[0]  # assume first element is largest
    for n in nums:
        if n > largest:
            largest = n
    return largest
