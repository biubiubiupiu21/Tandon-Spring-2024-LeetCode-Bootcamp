class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        word_set = set(wordDict)
        
        # dp[i] will be True if s[:i] can be segmented into words in the wordDict
        dp = [False] * (len(s) + 1)
        dp[0] = True  # base case: empty string can always be segmented
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        
        return dp[-1]