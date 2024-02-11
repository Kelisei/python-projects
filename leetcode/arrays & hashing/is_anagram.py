class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            dict_s = {}
            dict_t = {}
            for i in range(len(s)):
                dict_s[s[i]] = dict_s.get(s[i], 0) + 1
                dict_t[t[i]] = dict_t.get(t[i], 0) + 1
        return dict_t == dict_s
s = Solution()
s.isAnagram('sex', 'xes')