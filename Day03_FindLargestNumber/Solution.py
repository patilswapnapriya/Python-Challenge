def larget_number(n):
    """
    Return the largest number in the list with sort)
    """
    # n=[3,5,6,8,9]
    unquie_num=list(set(n))
    unquie_num.sort()
    num_1=(unquie_num[-1])
    num_2=(unquie_num[-2])
    print("First Largets Number",num_1)
    print("Second Largets Number",num_2)


def for_largets_numbers(nums):
    """
    Return the largest number in the list (without using max())
    """
    largest=nums[0]
    for i in nums:
        if i > largest:
            largest= i
    return largest
    # 🔹 Testing the function
if __name__ == "__main__":
    print(larget_number([3,4,5,6,7]))
    print(for_largets_numbers([2,4,5,7]))
