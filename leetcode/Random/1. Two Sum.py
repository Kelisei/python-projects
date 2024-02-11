# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]

 

# Constraints:

#     2 <= nums.length <= 104
#     -109 <= nums[i] <= 109
#     -109 <= target <= 109

#!To solve this we should use a hashmap, in this case it will store the number indices, with a foreach we iterate over the iterable object (the array) and we calculate the complement (being, in this case, the number necesary to calculate the target).
#!At the start it's empty, so we add the first number in the array to the dictionary, for example 2, then it comes 7 in the array, it so happens the target is 9 so 9-7 is equal to 2 which is in the dictionary, thus we have the result.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary to store the indices of each element in the array
        num_indices = {} 
        i = 0
        for num in nums: #!Foreach
            complement = target - num
            if complement in num_indices:
                # If the complement of the current number is found in the dictionary,
                # return the indices of the current number and the complement
                return [num_indices[complement], i]
            else:
                # If the complement is not found, add the current number and its index to the dictionary
                num_indices[num] = i
            i += 1

