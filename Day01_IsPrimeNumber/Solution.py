def is_prime(n: int) -> bool:
    """
    Check if a number is prime.

    Args:
        n (int): Input number

    Returns:
        bool: True if n is prime, False otherwise
    """
    if n <= 1:
        return False # 0,1,and negatives are not prime

    # Only check up to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # If divisible by i, not prime
            return False
    return True


# 🔹 Testing the function
if __name__ == "__main__":
    test_numbers = [2, 3, 4, 9, 13, 25, 29]
    for num in test_numbers:
        print(f"{num} → {is_prime(num)}")
