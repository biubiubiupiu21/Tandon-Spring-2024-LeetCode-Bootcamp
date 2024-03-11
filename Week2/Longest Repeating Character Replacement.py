class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        maxF = 0
        n = len(s)
        char_count = {}
        start = 0
        max_length = 0

        for end in range(n):
            char_count[s[end]] = char_count.get(s[end], 0) + 1
            maxF = max(maxF,char_count[s[end]])

            if (end - start + 1) - maxF > k:
                char_count[s[start]] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        

        return max_length

