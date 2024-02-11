"""
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]


Constraints:
    1 <= nums.length <= 105
    -104 <= nums[i] <= 104
    k is in the range [1, the number of unique elements in the array].
    It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's 
size.
"""
"""  First solution
from collections import Counter
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        cnt = Counter(nums)
        count = sorted(list(cnt.items()), key=lambda x: x[1], reverse=True)
        return [tupl[0] for tupl in count[0:k]]
"""  # (n log n)

from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        cnt = Counter(nums)
        return [
            number[0] for number in heapq.nlargest(k, cnt.items(), key=lambda x: x[1])
        ]


s = Solution()
print(s.topKFrequent([3, 0, 1, 0], 1))

# (n log k)
