# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.

# A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.

 

# Example 1:

# Input: accounts = [[1,2,3],[3,2,1]]
# Output: 6
# Explanation:
# 1st customer has wealth = 1 + 2 + 3 = 6
# 2nd customer has wealth = 3 + 2 + 1 = 6
# Both customers are considered the richest with a wealth of 6 each, so return 6.

# Example 2:

# Input: accounts = [[1,5],[7,3],[3,5]]
# Output: 10
# Explanation: 
# 1st customer has wealth = 6
# 2nd customer has wealth = 10 
# 3rd customer has wealth = 8
# The 2nd customer is the richest with a wealth of 10.

# Example 3:

# Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
# Output: 17

 

# Constraints:

#     m == accounts.length
#     n == accounts[i].length
#     1 <= m, n <= 50
#     1 <= accounts[i][j] <= 100

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        actual = 0
        maximumWealth = 0
        for m in range(0, len(accounts)):
            for n in range(0, len(accounts[m])):
                actual += accounts[m][n]
            if(actual > maximumWealth):
                maximumWealth = actual
            actual = 0
        return maximumWealth

#!This algorithm is obviously not optimal because at the time I didn't know about "sum" which kills one loop, optimal below:

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximumWealth = 0
        for m in range(0, len(accounts)):
            actual = sum(accounts[m])
            if(actual > maximumWealth):
                maximumWealth = actual
        return maximumWealth

#!Super optimal:
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(sum(i) for i in accounts)

