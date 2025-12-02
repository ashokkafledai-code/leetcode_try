# Given an array of integers and a target number, return the indices of the two numbers that add up to the target. 
# Each input has exactly one solution, and the same element cannot be used twice.

def twoSum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in lookup:
            return [lookup[diff], i]
        lookup[num] = i
