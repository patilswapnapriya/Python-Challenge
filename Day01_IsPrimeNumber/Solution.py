
# Day01 to fine if the Number is Prime or Not
def is_prime(n):
    """
    Check if a number is prime.
    Args:
        n (int): Input number
    Returns:
        bool: True if n is prime, False otherwise
    """
    if n<=1:
        return False # 0, 1, and negatives are not prime

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False # if divisible by i or not.
    return True


if __name__ == "__main__":
    test_numbers=[2,4,5,6,7,13,15,17,29]
    for num in test_numbers:
        print(f"{num} --> {is_prime(num)}")