def is_consecutive(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1] + 1:
            return False
    return True

nums = input("Enter a list of numbers (space-separated) to find if the list of numbers include consecutive integers or not: ").split()
nums = [int(num) for num in nums]

if is_consecutive(nums):
    print("The list contains consecutive integers.")
else:
    print("The list does not contain consecutive integers.")
