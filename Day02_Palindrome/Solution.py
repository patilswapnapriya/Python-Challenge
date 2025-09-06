def palindrome_withslicing(s: str) -> bool:
    """
    Check if a string is Palindrome.

    Args:
        n (str): Input string

    Returns:
        bool: True if n is Palindrome, False otherwise
    """
    s=s.lower()  
    return s==s[::-1]            
    # 🔹 Testing the function
def reverse_withoutslicing(s: str):
    """
    Check if a string is Palindrome.

    Args:
        n (str): Input string

    Returns:
        bool: True if n is Palindrome, False otherwise
    """
    result="" 
    for ch in s:
        result =ch+result
    return result          
    # 🔹 Testing the function
if __name__ == "__main__":
    print(palindrome_withslicing("wow"))
    print(palindrome_withoutslicing("hello"))
