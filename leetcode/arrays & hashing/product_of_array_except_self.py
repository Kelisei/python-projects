"""Given an integer array nums, return an array answer such that answer[i] is equal to the product 
of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

    2 <= nums.length <= 105
    -30 <= nums[i] <= 30
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

# Logic: given a index i, we have to multiply all the indexes (0..i-1 indexes) getting the prefix 
# and then multiply all of the indexes (i+1..n) and getting the postfix
# then we multiply the prefixes and postfixes to get the result
# And we'll do it in O(n) without //
# HOW to get the prefixes?: start with 1 and for i in range(n) multiply it and in each iteration
# put them in the list
# HOW to get the postfixes: start with 1, and go in descending order, do the same as in the prefix
# except we multiply what it's in the array already.
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        print(res)
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] = res[i]*postfix
            postfix *= nums[i]
        return res


s = Solution()
print(s.productExceptSelf([-1, 1, 0, -3, 3]))
