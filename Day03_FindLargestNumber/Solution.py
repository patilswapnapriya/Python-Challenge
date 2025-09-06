def larget_number(n):
    """
    Check if a string is Palindrome.

    Args:
        n (str): Input string

    Returns:
        bool: True if n is Palindrome, False otherwise
    """
    # n=[3,5,6,8,9]
    unquie_num=list(set(n))
    unquie_num.sort()
    num_1=(unquie_num[-1])
    num_2=(unquie_num[-2])
    print("1st Largets Number",num_1)
    print("Second Largets Number",num_2)
            
    # 🔹 Testing the function
if __name__ == "__main__":
    print(larget_number([3,4,5,6,7]))
