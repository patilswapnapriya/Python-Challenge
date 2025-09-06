# Notes: Prime Number Check

## Definition
- A **prime number** is greater than 1.
- It has **only 2 divisors**: 1 and itself.
- Examples: 2, 3, 5, 7, 11, 13…
- Non-prime (composite): 4, 6, 9, 12…

---

## Why use `range(2, int(n**0.5) + 1)`?
- To check divisibility, we only need to test numbers up to **√n**.
- If `n` has a divisor larger than √n, it must also have one smaller than √n.
- Example: 36 → factors pair up (2×18, 3×12, 6×6, 9×4…).
- Once we pass √36 = 6, factors start repeating.

### Example
For `n = 25`:
- √25 = 5
- We must check divisibility by [2, 3, 4, 5].
- Hence, we write:
  ```python
  range(2, int(n**0.5) + 1)
