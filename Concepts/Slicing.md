🔹 What is Slicing?

Slicing is a way to extract a portion of a sequence (string, list, tuple, etc.) using:

sequence[start:stop:step]


start → index to begin (inclusive)

stop → index to end (exclusive)

step → interval (default = 1)

🔹 String Slicing Examples
s = "python"

print(s[0:2])   # 'py'  → from index 0 to 1
print(s[2:5])   # 'tho' → from index 2 to 4
print(s[:4])    # 'pyth' → from start to index 3
print(s[3:])    # 'hon' → from index 3 to end
print(s[:])     # 'python' → full copy

🔹 Using Step
s = "abcdef"

print(s[::2])   # 'ace' → every 2nd char
print(s[1::2])  # 'bdf' → every 2nd char starting at index 1
print(s[::-1])  # 'fedcba' → reverse string


👉 This makes palindrome check super simple:

s == s[::-1]

🔹 List Slicing
nums = [0, 1, 2, 3, 4, 5, 6]

print(nums[2:5])   # [2, 3, 4]
print(nums[:3])    # [0, 1, 2]
print(nums[4:])    # [4, 5, 6]
print(nums[::-1])  # [6, 5, 4, 3, 2, 1, 0]

🔹 Negative Indexing

-1 → last element

-2 → second last element, and so on.

s = "world"
print(s[-3:])   # 'rld'
print(s[:-2])   # 'wor'

🔹 Edge Cases

Out-of-range indices don’t throw errors:

s = "hello"
print(s[0:100])  # 'hello'


Empty result when start > stop (with positive step):

print("python"[5:2])  # ''

🔹 Practical Tricks

Reverse a string/list:

s[::-1]


Get every 2nd/3rd element:

s[::2], s[::3]


Copy sequence:

s[:]
