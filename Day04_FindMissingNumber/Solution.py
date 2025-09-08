def missing_number_sorting(nums):
    """
    Return the largest number in the list with sort)
    """
    nums.sort()
    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1
    return len(nums)+1
    print("First Largets Number",num_1)


def for_missing_number(nums):
    """
    Return the largest number in the list (without using max())
    """
    n=len(nums)+1
    expected_sum= n * (n +1)//2
    acutal_sum=sum(nums)
    return expected_sum - acutal_sum
    # 🔹 Testing the function
def missing_number_binary(nums):
    """
    Return the largest number in the list (without using max())
    """
    left,right=0,len(nums)-1
    while left<= right:
        mid=(left+right)//2
        # At correct position: nums[mid] == mid+1
        if nums[mid]== mid+1:
            left= mid+1 # missing number on right side
        else:
            right= mid -1 # missing number on lrft side
    return left +1

    acutal_sum=sum(nums)
    return expected_sum - acutal_sum
    # 🔹 Testing the function
if __name__ == "__main__":
    print(missing_number_sorting([3,4,5,6,7]))
    print(for_missing_number([2,4,5,7]))
    print(missing_number_binary([1,2,4,5,7,9]))
