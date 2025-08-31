

def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "main":
    test_numbers=[2,4,5,6,7,13,15,17,29]
    for num in test_numbers:
        print(f"{num} --> {is_prime(num)}")