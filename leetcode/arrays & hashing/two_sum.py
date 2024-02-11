class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        number_indices = {} # Holds (number : index in the recieved list)
        for i, num in enumerate(nums):
            complement = target - num
            if complement in number_indices:
                return [number_indices[complement], i]
            else:
                number_indices[num] = i