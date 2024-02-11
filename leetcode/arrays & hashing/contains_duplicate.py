class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set = set()
        for num in nums:
            if not num in num_set:
                num_set.add(num)
            else:
                return True
        return False